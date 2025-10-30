from typing import Literal
from typing_extensions import Annotated
import operator

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents import Document
from langchain_community.document_loaders import WikipediaLoader
from langchain_tavily import TavilySearch
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

# Use Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# --- STATE ---
class State(MessagesState):
    question: str
    answer: str
    context: Annotated[list, operator.add]


# --- NODE 1: SEARCH WEB ---
def search_web(state: State):
    """Retrieve documents from Tavily search."""
    tavily_search = TavilySearch(max_results=3)
    data = tavily_search.invoke({"query": state["question"]})
    search_docs = data.get("results", data)

    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in search_docs
        ]
    )
    return {"context": [formatted_search_docs]}


# --- NODE 2: SEARCH WIKIPEDIA ---
def search_wikipedia(state: State):
    """Retrieve documents from Wikipedia."""
    search_docs = WikipediaLoader(query=state["question"], load_max_docs=2).load()

    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
            for doc in search_docs
        ]
    )
    return {"context": [formatted_search_docs]}


# --- NODE 3: GENERATE ANSWER ---
def generate_answer(state: State):
    """Generate answer using the context and question."""
    question = state["question"]
    context = state["context"]

    system_prompt = f"Answer the question '{question}' using this context:\n{context}"
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content="Provide a detailed and factual answer."),
    ]

    response = model.invoke(messages)
    return {"answer": response.content, "messages": [response]}


# --- GRAPH DEFINITION ---
workflow = StateGraph(State)

# Add nodes
workflow.add_node("search_web", search_web)
workflow.add_node("search_wikipedia", search_wikipedia)
workflow.add_node("generate_answer", generate_answer)

# Define flow
workflow.add_edge(START, "search_wikipedia")
workflow.add_edge(START, "search_web")
workflow.add_edge("search_web", "generate_answer")
workflow.add_edge("search_wikipedia", "generate_answer")
workflow.add_edge("generate_answer", END)

# Compile
graph = workflow.compile()

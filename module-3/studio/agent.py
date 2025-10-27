from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

# ---------- Tool Functions ----------
def to_lower_upper_swap(text: str) -> str:
    """Change lowercase letters to uppercase and vice versa."""
    return text.swapcase()

def swap_punctuation(text: str) -> str:
    """Change commas to full stops and full stops to commas."""
    return text.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")

tools = [to_lower_upper_swap, swap_punctuation]

# ---------- LLM ----------
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# ---------- System Message ----------
sys_msg = SystemMessage(
    content="You are a helpful assistant that modifies text based on user instructions using the available tools."
)

# ---------- Node ----------
def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# ---------- Build Graph ----------
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# ---------- Compile Graph ----------
graph = builder.compile()

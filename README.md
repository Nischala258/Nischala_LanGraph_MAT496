# Nischala_LanGraph_MAT496

Module 0

Setup of API keys aside from Tavily API key as it is not used until module 4

Tweak: Model is changed to Gemini 2.5-flash from Chatgpt3.5 and invoke message is "hello earth" from user "Nischala"

# Module 1:
## Lesson 1:

Overview of what LangGraph is and how it can help us visualise and understand the flow of control of LLMs while showing how it can go from router to fully autonomous state with increasing agent's level of control over decisions.

## Lesson 2:

We get to learn what a graph is and how to invoke different states, nodes and edges. We also try out a simple graph invokation and see how decision takes place in them.

**Tweak:** Changed the graph nodes from happy and sad to grumpy and sleepy, while also adding my own name to it.

## Lesson 3:
Learned how to run studio as a project which opens a UI on the web browser and we can easily play and interact to make new threads and look how the decisions are made clearly in the graph interactive image provided on the url.

**Tweak:** Changed and tested graph outputs with several names.

## Lesson 4:
We got to implement a chain of messages assuming different roles, then we added a "divide function" as a tool and made some tool calls. We used messages as states and then used reducers to append messages. Made graphs using the messageStates and then tested our tool call.

**Tweak:** Messages were personalised along with tool changed from multiply to divide along with arguments used in tool call

## Lesson 5:
We got to implement toolnodes which work as a router to help us decide when and when not to use a tool using toolCondition. We tested it with divide tool and hello earth messages. We also tested the same thing in router as well.

**Tweak:** Multiply tool was changed to divide in studio as well as the notebook.

## Lesson 6:
We implement an agent by simply adding another edge back from tools to the assistant and see how multiple operations can be performed by just one single message hence increasding the control level of the agent. 

**Tweaks:** We replaced divide operation by subtract and changed the systemMessage. Made similar changes in studio file as well.

## Lesson 7: 
We learned and implemented checkpointers to save graph states to mimic giving our agent memory as a key-value store for graph states. The states achieved in the past can be stored as thread ids and later used to further assist the operations.

**Tweak:** changed divide operation to subtract along with the arguments used as well.


# Module 2: 
## Lesson 1: 
We learn how to make a typeDict and DataClass and how to pass them to state and invoke the Graph. We also learn how to do the above with Pydantic which can validate the data. 

**Tweak:** Changed mood to places (Mumbai and Delhi). 

## Lesson 2: 
We learn how InvalidErrorUpdate gives and error when there’s an ambiguity in the code. 
We use reducers to avoid errors and give instructions to the state. We can also custom design these reducer functions. We learnt about MessageState and add_messages (reducer) .
We see how we can use message ids to re write and remove messages. 

**Tweaks:**  Changed the variables and the operation. Changed the messages and the ids (from numbers to letters). 

## Lesson 3: 
We learn about PrivateState that is used to interact between nodes, but it not present in the output which is provided by the overallState. We can also use input and output filters to restrict what is seen in the output schema. 

**Tweaks:** Changed the variables and messages. 

## Lesson 4:
We learn how to filter messages using RemoveMessages to see only the last two messages and delete the rest.  We also learn about trimming which reduces the number of tokens that are passed to the LLM. 

**Tweaks:** Changed OpenAI to Gemini and GoogleAI. Changed the messages and ids. 

## Lesson 5:
We learn how to setup an assistant to summarize conversations when they get too long. This summary lives in state. We use a checkpointer to persist state through time. 

**Tweaks:** I changed the model to Gemini. The condition for summarization was changed. The messages and ids were changed. 

## Lesson 6:
We learn how to use checkpointers like SQlite which writes the conversations to the database in the system, which saves it in the external memory. 

**Tweaks:** Changed the model to Gemini and GoogleAI. Changed the thread id and messages. Changed the model in studio file as well. 


# Module 3
## Lesson 1:
We learn how to stream in two different ways. Values which stream the full state of the node and Updates which streams only the updates that are made to the node. We learn about .astream which the asynchronous version of streaming which streams model output as they are being generated. 

**Tweaks:** Changed the model from openAI to GoogleAI and Gemini. Made changes in the messages and ids. 

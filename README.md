# Nischala_LanGraph_MAT496

Module 0

Setup of API keys aside from Tavily API key as it is not used until module 4

Tweak: Model is changed to Gemini 2.5-flash from Chatgpt3.5 and invoke message is "hello earth" from user "Nischala"

# Lesson 1:
Overview of what LangGraph is and how it can help us visualise and understand the flow of control of LLMs while showing how it can go from router to fully autonomous state with increasing agent's level of control over decisions.

# Lesson 2:
We get to learn what a graph is and how to invoke different states, nodes and edges. We also try out a simple graph invokation and see how decision takes place in them.

Tweak: Changed the graph nodes from happy and sad to grumpy and sleepy, while also adding my own name to it.

# Lesson 3:
Learned how to run studio as a project which opens a UI on the web browser and we can easily play and interact to make new threads and look how the decisions are made clearly in the graph interactive image provided on the url.

Tweak: Changed and tested graph outputs with several names.

# Lesson 4:
We got to implement a chain of messages assuming different roles, then we added a "divide function" as a tool and made some tool calls. We used messages as states and then used reducers to append messages. Made graphs using the messageStates and then tested our tool call.

Tweak: Messages were personalised along with tool changed from multiply to divide along with arguments used in tool call

# Lesson 5:
We got to implement toolnodes which work as a router to help us decide when and when not to use a tool using toolCondition. We tested it with divide tool and hello earth messages. We also tested the same thing in router as well.

Tweak: Multiply tool was changed to divide in studio as well as the notebook.

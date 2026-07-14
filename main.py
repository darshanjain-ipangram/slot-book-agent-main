#fastapi endpoint
from fastapi import FastAPI
from model.model import chatrequest, chatresponse
from agent.graph import chatagent
from langchain_core.messages import HumanMessage

app = FastAPI(title="clinic slot booking agent")

agent = chatagent()
graph = agent.get_compiled_graph()

@app.post("/chat", response_model=chatresponse)
async def chat_endpoint(request: chatrequest) -> chatresponse:
    config = {"configurable": {"thread_id": request.session_id}}
    state = {"messages": [HumanMessage(content=request.user_message)]}
    
    result = await graph.ainvoke(state, config=config)
    
    last_message = result["messages"][-1]
    
    return chatresponse(
        session_id=request.session_id,
        user_message=last_message.content
    )

from pydantic.json_schema import Examples
from pydantic import BaseModel,Field
from typing import List,Optional,TypedDict
from datetime import datetime
from langgraph.graph.message import add_messages
from typing import Annotated


#FASTAPI ENDPOINT SCHEMA

class chatrequest(BaseModel):
    session_id:str
    user_message:str

class chatresponse(BaseModel):
    session_id:str
    user_message:str
    
#tool SCHEMAS

class check_availability(BaseModel):
    date:str=Field(
        description="date of appointment date YY-MM-DD",
        Examples=["2025-07-20"]
    )
class create_booking(BaseModel):
    date:str=Field(
        description="date of appointment date YY-MM-DD",
        Examples=["2025-07-20"]
    )
    name:str=Field(
        description="name of the patient",
        Examples=["Darshan"]
    )
    email:str=Field(
        description="email of the patient",
        Examples=["[EMAIL_ADDRESS]"]
    )
    reason:str=Field(
        description="reason for the appointment",
        Examples=["fever,headache,flu,follow-up checkup"]
    )
    

#graph state pydantic model

class GraphState(TypedDict):
    messages:Annotated[List, add_messages]




  
    

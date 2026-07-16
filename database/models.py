from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy import Text
class Conversation(Base):
    
    __tablename__ = "conversations" 
    id=Column(Integer,primary_key=True)
    session_id=Column(String(255),nullable=False,index=True)
    Human_message = Column(Text, nullable=False)
    AI_message = Column(Text, nullable=False)
    created_at=Column(DateTime(timezone=True),
    server_default=func.now())


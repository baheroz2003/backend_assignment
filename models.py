from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True)
    matrix = Column(String)
    result = Column(String)
    response_time = Column(Float)

from sqlalchemy import Column, Integer, String
from .database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,nullable=False)
    authors = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    year = Column(Integer, nullable=True)
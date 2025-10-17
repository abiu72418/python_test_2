from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class TodoModel(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

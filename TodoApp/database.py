from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # for database session
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABSE_URL = "sqlite:///./todos.db"

engine = create_engine(
    SQLALCHEMY_DATABSE_URL,
    connect_args = {"check_same_thread" : False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # to create database model
#The declarative_base() base class contains a MetaData object where newly defined Table objects are collected. This object is intended to be accessed directly for MetaData -specific operations. Such as, to issue CREATE statements for all tables: engine = create_engine('sqlite://') Base.

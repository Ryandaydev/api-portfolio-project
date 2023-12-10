"""Database configuration - Chapter 1 & 2"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Define the connection URL for our database
SQLALCHEMY_DATABASE_URL = "sqlite:///./fantasy_data.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)


#Create a sessionmaker with a connection to the engine and additional settings
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Create a base object that will be used to define Python classes
Base = declarative_base()

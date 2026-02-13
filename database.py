import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

os.environ.getenv("DB_URL")

engine = create_engine(os.getenv("DB_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

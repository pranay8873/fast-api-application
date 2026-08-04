from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


import os
from sqlalchemy import create_engine

# Fallback to local connection for local development
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/your_db")

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )
Base=declarative_base()


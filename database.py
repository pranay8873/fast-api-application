from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



# database_url = os.getenv("DATABASE_URL")
database_url = "mysql+pymysql://root:root@localhost:3306/criminal_records"
engine=create_engine(database_url)
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )
Base=declarative_base()


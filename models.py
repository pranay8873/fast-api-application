from sqlalchemy import Column,String,Integer,Boolean, column
from database import Base


class Criminal(Base):
    __tablename__="criminals"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Integer)
    gender=Column(String(10))   
    Fir_number=Column(String(100))

class Police(Base):
    __tablename__="polices"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Integer)
    gender=Column(String(10))
    role=Column(String(100))

class Lawyer(Base):
    __tablename__="lawyers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Integer)
    gender=Column(String(50))
    role=Column(String(50))

class Judge(Base):
    __tablename__="judges"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Integer)
    gender=Column(String(50))
    role=Column(String(50))

class app_developer(Base):
    __tablename__="app_developers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Integer)
    gender=Column(String(50))
    role=Column(String(50))
    

    




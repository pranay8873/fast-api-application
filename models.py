from sqlalchemy import Column,String,Integer,Boolean
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




from pydantic import BaseModel
from typing import Optional


class Criminal_Register(BaseModel):
    name: str
    age: int
    gender: str
    Fir_number: str

    class Config:
        from_attributes = True

class Criminal_Response(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    Fir_number: str

    class Config:
        from_attributes = True


class Police_Register(BaseModel):
    name: str
    age: int
    gender: str
    role: str

    class Config:
        from_attributes = True

class Police_Response(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    role: str

    class Config:
        from_attributes = True

class Lawyer_Register(BaseModel):
    name:str
    age:int
    gender:str
    role:str

    class Config:
        from_attributes = True

class Lawyer_Response(BaseModel):
    id:int
    name:str
    age:int
    gender:str
    role:str
    class Config:
        from_attributes = True

class Judge_Register(BaseModel):
    name:str
    age:int
    gender:str
    role:str
    class Config:
        from_attributes = True

class Judge_Response(BaseModel):
    id:int
    name:str
    age:int
    gender:str
    role:str
    class Config:
        from_attributes = True


class app_developer(BaseModel):
    name:str
    age:int
    gender:str
    role:str
    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import Optional


class Criminal(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str
    Fir_number: str

    class Config:
        from_attributes = True


class Police(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str
    role: str

    class Config:
        from_attributes = True
class lawywe(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str
    class Config:
        from_attributes = True

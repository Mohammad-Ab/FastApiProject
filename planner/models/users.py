from pydantic import BaseModel,EmailStr
from typing import Optional,List
from models.events import Event
from beanie import Document, Link

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
            "email": "fastapi@packt.com",
            "username": "strong!!!",
            "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }

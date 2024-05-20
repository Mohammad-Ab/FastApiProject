from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
        ):
            return cls(item=item)

    class Config:
        schema_extra = {
                "example":{
                    "id":1,
                    "item": "example schema"
                }
    
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example":{
                "item":"Read the next Chapter of this book!"
            }
        }

class TodoItems(BaseModel):
    
    todos: List[TodoItem]

    class Config:
        schema_extra = {
                "example":{
                    "todos":[
                            {
                                "item": "example schema 1" 
                            },
                            {
                                "item": "example schema 2"
                            }
                        ]
    
                }
        }

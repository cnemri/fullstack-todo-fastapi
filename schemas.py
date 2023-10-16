from pydantic import BaseModel


class ToDoRequest(BaseModel):
    name: str
    completed: bool = False


class ToDoResponse(BaseModel):
    id: int
    name: str
    completed: bool = False

    class Config:
        orm_mode = True

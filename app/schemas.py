from pydantic import BaseModel

class MemeBase(BaseModel):
    title: str
    url: str

class MemeCreate(MemeBase):
    pass

class Meme(MemeBase):
    id: int

    class Config:
        orm_mode = True

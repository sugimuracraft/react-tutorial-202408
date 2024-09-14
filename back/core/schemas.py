from pydantic import BaseModel


class EmptySchema(BaseModel):
    pass


class ListQuerySchema(BaseModel):
    count: int
    page: int

from pydantic import BaseModel

class FileSchema(BaseModel):
    id: int
    name: str
    filename: str
    path: str

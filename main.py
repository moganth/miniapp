from fastapi import FastAPI
import uvicorn

from api.api import router as file_router
from core.database import create_table

app = FastAPI()

create_table()

app.include_router(file_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

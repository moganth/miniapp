from fastapi import FastAPI
import uvicorn

from api.api import router as file_router
from core.database import create_table

app = FastAPI(openapi_url="/api1/openapi.json",
    docs_url="/api1/docs",
    redoc_url="/api1/redoc",
    # root_path="/gateway/plugin/project-139/moganth-plugin1/api/"
)

create_table()

app.include_router(file_router, prefix="/api1")

@app.get("/api1/home")
async def root():
    return {"message": "API1 Home"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

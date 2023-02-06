from fastapi import FastAPI
from typing import Union,Optional
from pydantic import BaseModel
from routers import item



app = FastAPI()
app.include_router(item.router)

@app.get("/")
def root():
    return {"msg":"welcome to root page"}

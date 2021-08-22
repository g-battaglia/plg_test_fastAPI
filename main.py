from typing import Optional
from fastapi import FastAPI
from functions import get_tabs

app = FastAPI()


@app.get("/")
def read_root():
    data = get_tabs()

    return data

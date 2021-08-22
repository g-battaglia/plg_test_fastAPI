from typing import Optional
from fastapi import FastAPI
from functions import get_tabs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    data = get_tabs()

    return data


@app.get("/1")
def read_root():
    data = get_tabs()[0]
    return data


@app.get("/2")
def read_root():
    data = get_tabs()[1]
    return data


@app.get("/3")
def read_root():
    data = get_tabs()[2]
    return data

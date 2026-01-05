from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import asyncio
import psutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    index_file = Path("static/index.html")
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "Index file not found"}

@app.get("/data")
def get_data():
    return {"cpu": psutil.cpu_percent(),
            "ram": psutil.virtual_memory().percent,
        }

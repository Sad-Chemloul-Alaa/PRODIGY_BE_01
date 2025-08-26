from fastapi import FastAPI
from routers import user
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()
app.include_router(user.router)
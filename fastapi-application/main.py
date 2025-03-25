from fastapi import FastAPI
from contextlib import asynccontextmanager
from api import router as api_router
from core.config import settings
from core.models import db_helper



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("dispouse engine")
    await db_helper.dispouse()


app = FastAPI(
    lifespan = lifespan,
)
app.include_router(api_router, prefix=settings.api.prefix)




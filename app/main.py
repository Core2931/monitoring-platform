from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings

# Lab 1.3: import the hospitals router
# Lab 1.6: import the debug router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lab 1.5: runs once at startup (before yield) and once at shutdown (after yield)
    # TODO(1.5): if settings.storage == "mongo":
    #   - create the Mongo client and keep it on app.state
    #   - create indexes
    yield
    # TODO(1.5): close the Mongo client


app = FastAPI(title=settings.app_name, lifespan=lifespan)

# TODO(1.3): include the hospitals router with prefix "/api/v1"
# TODO(1.6): include the debug router


# Lab 1.1 -------------------------------------------------------------
@app.get("/healthz", tags=["ops"])
async def healthz():
    # TODO(1.1): return {"status": "ok"}
    ...

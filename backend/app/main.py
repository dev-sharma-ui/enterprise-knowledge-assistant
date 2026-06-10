from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.users import router as users_router

from app.core.config import settings
from app.core.logger import logger


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.on_event("startup")
async def startup_event():

    logger.info(
        f"Starting {settings.APP_NAME} "
        f"in {settings.ENVIRONMENT} mode"
    )


app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():

    return {
        "message": f"{settings.APP_NAME} Running"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT
    }
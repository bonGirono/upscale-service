import uvicorn
from fastapi import FastAPI

from src.core import config
from src import upscale

app = FastAPI(
    title=config.PROJECT_TITLE,
    debug=config.DEBUG
)

app.include_router(upscale.router)


if __name__ == "__main__":
    config.MEDIA_PATH.mkdir(parents=True, exist_ok=True)
    config.UPLOAD_MEDIA_PATH.mkdir(parents=True, exist_ok=True)
    config.UPSCALE_MEDIA_PATH.mkdir(parents=True, exist_ok=True)

    uvicorn.run(
        app="main:app", port=config.SERVER_PORT,
        host=config.SERVER_HOST, reload=config.DEBUG,
        workers=config.WORKERS
    )

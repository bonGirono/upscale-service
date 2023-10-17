from starlette.config import Config
from pathlib import Path

config = Config(".env")

# uvicorn configs
PROJECT_TITLE = "Upscale service"
DEBUG = config("DEBUG", cast=bool, default=False)
SERVER_HOST = config("SERVER_HOST", default='127.0.0.1')
SERVER_PORT = config("SERVER_PORT", cast=int, default=8000)
WORKERS = config("WORKERS", cast=int, default=4)

# celery configs
CELERY_BROKER_URL = config("CELERY_BROKER_URL", default="redis://localhost:6379")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", default="redis://localhost:6379")

# base configs
BASE_DIR = Path(__file__).resolve().parent.parent.parent.absolute()
MEDIA_PATH = BASE_DIR / config("MEDIA_PATH", cast=str, default="media")
UPLOAD_MEDIA_PATH = MEDIA_PATH / 'upload'
UPSCALE_MEDIA_PATH = MEDIA_PATH / 'upscale'

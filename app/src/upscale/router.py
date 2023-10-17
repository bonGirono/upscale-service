from fastapi import APIRouter

from src.base.router import ViewSetRouter
from src.upscale.view import UpscaleView

router = APIRouter(prefix="/upscale", tags=["Upscale"])
router.include_router(ViewSetRouter(path="", view_class=UpscaleView))

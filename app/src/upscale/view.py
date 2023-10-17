import aiofiles
from fastapi import UploadFile, HTTPException, File

from src.core import config
from src.core.tasks import upscale2x
from src.core.utils import get_md5, get_file_extension


class UpscaleView:

    async def create(self, file: UploadFile = File(...)):
        content_type = file.content_type
        if content_type not in ["image/jpeg", "image/png", "video/mp4"]:
            raise HTTPException(status_code=400, detail="Invalid file type")

        try:
            content = file.file.read()
            file_path = str(config.UPLOAD_MEDIA_PATH / f'{get_md5(file.file)}.{get_file_extension(file.filename)}')
            async with aiofiles.open(file_path, 'wb') as f:
                await f.write(content)
            is_video = True if content_type == "video/mp4" else False
            upscale2x.delay(file_path, is_video)
            file.file.seek(0)

        except Exception as _:
            raise HTTPException(status_code=400, detail=f"File upload error")

        finally:
            file.file.close()

        return {"message": f"Successfully uploaded to upscale {file.filename}"}

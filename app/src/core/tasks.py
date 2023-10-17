import cv2
import numpy as np
from PIL import Image
from celery import Celery
from src.core import config

celery = Celery(config.PROJECT_TITLE)
celery.conf.broker_url = config.CELERY_BROKER_URL
celery.conf.broker_url = config.CELERY_BROKER_URL


class UpScale:
    file_path: str
    output_path: str

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.output_path = str(config.UPSCALE_MEDIA_PATH / config.Path(file_path).name)

    @staticmethod
    def __scale(image: Image.Image) -> tuple[int, int, Image.Image]:
        width, height = image.size
        pixels = ((x, y, image.getpixel((x, y))) for y in range(height) for x in range(width))
        new_image = Image.new(mode='RGB', size=(width * 2, height * 2))
        for x, y, pixel in pixels:
            up = image.getpixel((x, y - 1)) if y > 0 else pixel
            down = image.getpixel((x, y + 1)) if y < height - 1 else pixel
            left = image.getpixel((x - 1, y)) if x > 0 else pixel
            right = image.getpixel((x + 1, y)) if x < width - 1 else pixel

            left_up = left if left == up else pixel
            left_down = left if left == down else pixel
            right_up = right if right == up else pixel
            right_down = right if right == down else pixel

            sx, sy = x * 2, y * 2
            new_image.putpixel((sx, sy), left_up)
            if x < width: new_image.putpixel((sx + 1, sy), right_up)
            if y < height: new_image.putpixel((sx, sy + 1), left_down)
            if y < height and x < width: new_image.putpixel((sx + 1, sy + 1), right_down)

        return width * 2, height * 2, new_image

    @staticmethod
    def __scale_cv2_realisation(image: np.ndarray) -> np.ndarray:  # slower x2+ than pillow realisation [NOT USED]
        height, width, _ = image.shape
        print(width, height)
        pixels = ((x, y, image[y, x]) for x in range(width) for y in range(height))
        new_image = np.zeros((height * 2, width * 2, 3), np.uint8)
        for x, y, pixel in pixels:
            up = image[y - 1, x] if y > 0 else pixel
            down = image[y + 1, x] if y < height - 1 else pixel
            left = image[y, x - 1] if x > 0 else pixel
            right = image[y, x + 1] if x < width - 1 else pixel

            left_up = left if (left == up).all() else pixel
            left_down = left if (left == down).all() else pixel
            right_up = right if (right == up).all() else pixel
            right_down = right if (right == down).all() else pixel

            sx, sy = x * 2, y * 2
            new_image[sy, sx] = left_up
            if x < width: new_image[sy, sx + 1] = right_up
            if y < height: new_image[sy + 1, sx] = left_down
            if y < height and x < width: new_image[sy + 1, sx + 1] = right_down

        return new_image

    def image(self):
        with Image.open(self.file_path) as image:
            _, _, new_image = self.__scale(image)
            new_image.save(self.output_path)
            new_image.close()

    def video(self):
        video = cv2.VideoCapture(self.file_path)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        new_video = cv2.VideoWriter(self.output_path, fourcc, fps, (width * 2, height * 2))
        i = 0
        while video.isOpened():
            success, frame = video.read()
            if success:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                _, _, new_frame = self.__scale(Image.fromarray(image))
                new_video.write(cv2.cvtColor(np.array(new_frame), cv2.COLOR_RGB2BGR))
                new_frame.close()
                i += 1
            else:
                break
        cv2.destroyAllWindows()
        video.release()
        new_video.release()


@celery.task(name="upscale2x")
def upscale2x(file_path: str, is_video: bool = False) -> bool:
    try:
        upscale = UpScale(file_path)
        if is_video:
            upscale.video()
        else:
            upscale.image()

    except Exception as _:
        return False

    return True

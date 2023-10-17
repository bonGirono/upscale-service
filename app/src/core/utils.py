from hashlib import md5
from typing import BinaryIO


def get_bytes_size(bytes_: BinaryIO) -> int:
    bytes_.seek(0, 2)
    size = bytes_.tell()
    return size


def get_md5(bytes_: BinaryIO) -> str:
    _md5 = md5()
    for chunk in iter(lambda: bytes_.read(8192), b""):
        _md5.update(chunk)

    return _md5.hexdigest()


def get_file_extension(filename: str) -> str:
    return filename.split('.')[-1]

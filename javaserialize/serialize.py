import io

from .types import *
from .constants import *


def serialize_stream(obj, stream=None):
    if not stream:
        stream = io.BytesIO()
    stream.write(STREAM_MAGIC)
    stream.write(STREAM_VERSION)

    return stream


def serialize_bytes(obj) -> bytes:
    return serialize_stream(obj).read()

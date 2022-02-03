from typing import Union
from io import BytesIO

from .types import *
from .constants import *


def _serialize_str(s: Union[str, bytes], stream: BytesIO):
    if type(s) == str:
        s = s.encode('utf-8')
    if len(s) <= 0xffff:
        stream.write(TC_TYPES[str])
        # print((len(s) >> 8, len(s) >> 0))
        stream.write(bytes((len(s) >> 8, len(s) >> 0)))
    else:
        stream.write(bytes(
            (len(s) >> (56 - 8 * i) & 0xff for i in range(8))
        ))
        stream.write(TC_TYPES[longstr])
    pos = 0
    for i in range(len(s)):
        if s[i] >> 4 in (15, 16):
            # see javadoc /docs/api/java.base/java/io/DataInput.html
            raise ValueError()
        if s[i] == 0:
            stream.write(s[pos:i - 1])
            pos = i + 1
            stream.write(bytes((0xc0, 0x80)))
    stream.write(s[pos:])
    stream.flush()


_handles = {
    str: _serialize_str,
    bytes: _serialize_str,
}


def _serialize(obj, stream: BytesIO, unshared):
    if type(obj) not in _handles:
        pass
    _handles[type(obj)](obj, stream)


def serialize_stream(obj, stream: BytesIO = None):
    if not stream:
        stream = BytesIO()
    stream.write(STREAM_MAGIC)
    stream.write(STREAM_VERSION)
    _serialize(obj, stream, False)
    return stream


def serialize_bytes(obj) -> bytes:
    return serialize_stream(obj).read()

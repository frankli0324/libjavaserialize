from .types import *

MAX_BLOCK_SIZE = 1024
STREAM_MAGIC = bytes((0xac, 0xed))
STREAM_VERSION = bytes((0x00, 0x05))
TC_TYPES = {
    type(None): bytes((0x70,)),
    ref: bytes((0x71,)),
    classdesc: bytes((0x72,)),
    str: bytes((0x74,)),
    list: bytes((0x75,)),
    type(type(None)): bytes((0x76,)),  # Reference to Class # ?
    # BLOCKDATA: 0x77; ENDBLOCKDATA: 0x78
    reset: bytes((0x79,)),
    # BLOCKDATALONG: 0x7a
    wexception: bytes((0x7b,)),
    longstr: bytes((0x7c,)),
}

class ref:
    def __init__(self, obj):
        self.obj = obj


class classdesc:
    def __init__(self, cls):
        self.cls = cls


class reset:
    # reset stream
    pass


class wexception:
    # Exception during write.
    pass


class longstr(str):
    pass

class enum:
    # TODO: find a way to represent java style enumeration
    pass

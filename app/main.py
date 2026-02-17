import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")
    src = parts[1]
    dst = parts[2]
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))
    dirpath = os.path.dirname(dst)
    if dirpath:
        cur = ""
        for part in dirpath.split("/"):
            cur = os.path.join(cur, part) if cur else part
            if not os.path.exists(cur):
                os.mkdir(cur)
    with open(src, "rb") as fsrc:
        data = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(data)
    os.remove(src)

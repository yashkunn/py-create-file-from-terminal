import sys
import os
from datetime import datetime
from typing import Any


def create_directory(dirs: Any) -> None:
    path = os.path.join(*dirs)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")


def create_file(file_path: Any) -> None:
    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    print("Enter content lines (type 'stop' on a new line to finish):")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, mode) as file:
        if mode == "w":
            file.write(f"{timestamp}\n")
        else:
            file.write(f"\n{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")

    print(f"File created/updated: {file_path}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file.txt]")
        return

    dir_flag = "-d"
    file_flag = "-f"

    args = sys.argv[1:]

    if dir_flag in args:
        dir_index = args.index(dir_flag) + 1
        dirs = []
        while dir_index < len(args) and args[dir_index] not in [file_flag]:
            dirs.append(args[dir_index])
            dir_index += 1
        if dirs:
            create_directory(dirs)

    if file_flag in args:
        file_index = args.index(file_flag) + 1
        if file_index < len(args):
            file_name = args[file_index]
            file_path = os.path.join(*dirs, file_name) if dirs else file_name
            create_file(file_path)


if __name__ == "__main__":
    main()

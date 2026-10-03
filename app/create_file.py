import os
import sys
from datetime import datetime


def create_file() -> None:
    directories = []
    filename = None

    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1

            while i < len(args) and args[i] != "-f":
                directories.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1

            if i < len(args):
                filename = args[i]

        i += 1

    directory = os.path.join(*directories) if directories else "."

    os.makedirs(directory, exist_ok=True)

    if not filename:
        return

    filepath = os.path.join(directory, filename)

    lines = []
    number = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(f"{number} {line}")
        number += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file:
        file.write(f"{timestamp}\n")
        file.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    create_file()

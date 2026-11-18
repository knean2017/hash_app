import os
import sys
import mmh3

n = int(sys.argv[1])
s = int(sys.argv[2])

try:
    while True:
        text = input("Please enter the string: ")
        if text == "":
            continue

        bucket = mmh3.hash(text) % n + 1
        file_name = f"{bucket}.txt"

        number = 1
        while os.path.exists(f"{bucket}_{number}.txt"):
            file_name = f"{bucket}_{number}.txt"
            number += 1

        size = 0
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                size = len(f.read())

        if size > 0 and size + len(text) > s:
            file_name = f"{bucket}_{number}.txt"

        with open(file_name, "a", encoding="utf-8") as f:
            f.write(text)

        print(f"{text} added to {file_name}")
except (KeyboardInterrupt, EOFError):
    print()

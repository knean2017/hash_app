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
        file_name = str(bucket) + ".txt"

        f = open(file_name, "a")
        f.write(text)
        f.close()

        print(text + " added to " + file_name)
except (KeyboardInterrupt, EOFError):
    print()

import argparse
import sys

parser = argparse.ArgumentParser(
    prog="cat",
    description="Reads and prints a log file line by line, or from stdin if no file is provided.",
)

parser.add_argument("logfile", nargs="?", help="Path to the log file")
args = parser.parse_args()

if args.logfile:
    # read aut of file
    with open(args.logfile, "r", encoding="utf-16") as file:
        for line in file.readlines():
            print(line.replace("\x00", ""), end="")

else:
    # read aut of stdin
    for line in sys.stdin.read().splitlines():
        print(line)

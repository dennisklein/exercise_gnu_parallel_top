import argparse
import sys

parser = argparse.ArgumentParser(
    prog="cat",
    description="Reads and prints a log file line by line, or from stdin if no file is provided."
)

parser.add_argument("logfile", nargs="?", help="Path to the log file")
args = parser.parse_args()

if args.logfile:
    # read aut of file
    with open(args.logfile, "r", encoding="utf-16") as file:
        lines = file.readlines()
    
    for line in lines:
        cleaned_line = line.replace("\x00", "") 
        print(cleaned_line, end="")
    
else:
    # read aut of stdin
    lines = sys.stdin.read().splitlines()
    
    for line in lines:
        print(line)

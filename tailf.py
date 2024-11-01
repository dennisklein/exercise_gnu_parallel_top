import argparse

parser = argparse.ArgumentParser(
    prog="tailf",
    description="Reads and prints the last 10 lines of a file line by line evry 10 seconds"
)

parser.add_argument("logfile", nargs="?", help="Path to the log file")
args = parser.parse_args()

# read aut of file
with open(args.logfile, "r", encoding="utf-16") as file:
    for line in file.readlines():
        print(line.replace("\x00", ""), end="")
    

import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="reads and prints a log file line by line",
)

parser.add_argument("logfile")
args = parser.parse_args()

logfile = args.logfile

with open(logfile, "r", encoding="utf-16") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.replace("\x00", "")  # Entfernt alle Nullbytes
        print(cleaned_line, end="")

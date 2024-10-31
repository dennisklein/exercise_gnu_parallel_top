import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="reads and prints a log file line by line",
)

parser.add_argument("logfile")
args = parser.parse_args()

logfile = args.logfile



import argparse
import time
import os

# Argument parser setup
parser = argparse.ArgumentParser(
    prog="tailf",
    description="Reads and prints the last 10 lines of a file line by line every 10 seconds",
)
parser.add_argument("logfile", help="Path to the log file")
args = parser.parse_args()


# Function to clear the console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


try:
    with open(args.logfile, "r", encoding="utf-16") as file:

        lines = []

        while True:
            # Read new lines added to the file
            new_lines = file.readlines()
            print("noo")
            if new_lines:
                lines.extend(new_lines)
                print("jes")

            # Display only the last 10 lines
            last_10_lines = lines[-10:]

            # Clear the console
            clear_console()

            # Print each line
            for line in last_10_lines:
                print(line.replace("\x00", ""), end="")

            # Wait for 10 seconds
            time.sleep(10)
except FileNotFoundError:
    print(f"Error: The file '{args.logfile}' was not found.")
except IOError as e:
    print(f"Error reading the file '{args.logfile}': {e}")

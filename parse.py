import time
import os
import argparse

parser = argparse.ArgumentParser(
    prog="tailf",
    description="Reads and prints the last 10 lines of a file line by line every 10 seconds",
)

parser.add_argument("logfile", help="Path to the log file")
args = parser.parse_args()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def parse(input_line: str) -> dict:
    columns = input_line.split()
    parsed = {
        "sec": int(columns[0]),
        "host": columns[1],
        "starttime": time.gmtime(float(columns[2])),
        "jobRuntime": float(columns[3]),
        "send": int(columns[4]),
        "receive": int(columns[5]),
        "exitval": int(columns[6]),
        "signal": int(columns[7]),
        "command": " ".join(columns[8:]),
    }

    return parsed


try:
    with open(args.logfile, "r") as file:

        lines = []

        while True:
            new_lines = file.readlines()
            if new_lines:
                lines.extend(new_lines)

            last_10_lines = lines[-10:]

            clear_console()

            for line in last_10_lines:
                parsed_line = parse(line.replace("\x00", ""))

                for key, value in parsed_line.items():
                    print(f"Column {key}: {value}")

                print("-----------")

            time.sleep(10)
except FileNotFoundError:
    print(f"Error: The file '{args.logfile}' was not found.")
except IOError as e:
    print(f"Error reading the file '{args.logfile}': {e}")

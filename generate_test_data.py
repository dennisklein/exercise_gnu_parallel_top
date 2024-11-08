import random
import argparse

# Command Line Argument Parser
parser = argparse.ArgumentParser(
    prog="generate_test_data",
    description="Generates n lines of sleep() statements within the specified rang",
)

parser.add_argument(
    "-n", default=100, type=int, help="Number of lines to generate"
)
parser.add_argument(
    "-t",
    default="0.5-5",
    help="Range for sleep times, formatted as lower-upper",
)

# Initialisieren der Grenzen und Argumente
args = parser.parse_args()

lower_bound, upper_bound = map(float, args.t.split("-"))
lines = args.n


false_probability = 0.1

for i in range(lines):
    if random.random() < false_probability:
        print("false")
    else:
        print(
            "sleep " + str(round(random.uniform(lower_bound, upper_bound), 2))
        )

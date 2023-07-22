""" Accepting Arguments """
import sys
import argparse

name = sys.argv[1]

print(f"Hello {name}")

# ? run py (python3) 10_command_line_arguments.py acidrums 26


parser = argparse.ArgumentParser(description="This program prints the name of my dogs")

# parser.add_argument('-c', '--color', metavar='color',
#                     required=True, help='the color to search for')

# args = parser.parse_args()

# print(args.color)

# ? run py (python3) -c COLOR

parser.add_argument(
    "-c",
    "--color",
    metavar="color",
    required=True,
    choices={"green", "gold", "black"},
    help="the color to search for",
)

args = parser.parse_args()

print(args.color)

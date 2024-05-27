#!/usr/bin/env python3
"""
Author: Robert Cheadle <robert.cheadle01@gmail.com>
Date: 05-27-2024
Purpose: Say what up to arg
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Say what up to the input value")
    parser.add_argument(
        "-n", "--name", metavar="name", default="humanoid", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """Say what up to input string"""

    args = get_args()
    print("What up, " + args.name + "!")


if __name__ == "__main__":
    main()

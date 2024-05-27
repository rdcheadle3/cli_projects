#!/usr/bin/env python3
"""
Author : bobby <robert.cheadle01@gmail.com>
Date   : 2024-05-27
Purpose: Tell captain what you see
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Input what is seen',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Alert captain"""

    args = get_args()
    pos_arg = args.positional

    vowel = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

    if pos_arg.startswith(vowel):
        print(f'Ahoy, Captain, an {pos_arg} off the larboard bow!')
    else: print(f'Ahoy, Captain, a {pos_arg} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

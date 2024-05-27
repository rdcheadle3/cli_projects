#!/usr/bin/env python3 

import argparse

def main():
    parser = argparse.ArgumentParser(description='Say what up to the input value')
    parser.add_argument('-n', '--name', metavar='name', default='humanoid',
                    help='Name to greet')
    args = parser.parse_args()

    print('What up, ' + args.name + '!')

if __name__ == '__main__':
    main()

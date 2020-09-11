#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2020-09-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    if word[0] in "aeiou":
        article = "an"
    elif word[0] in "AEIOU":
        article = "An"
    elif word[0] != word[0].upper():
        article = "a"
    else:
        article = "A"
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()

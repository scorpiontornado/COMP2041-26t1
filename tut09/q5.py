#!/usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 9, Q3 (tags)
# Fetch specified web page and count the HTML tags in them
#
# To install requests:
# > python3 -m venv .venv
# > source .venv/bin/activate
# > pip3 install requests
#
# You'll need to re-run `source .venv/bin/activate` in each new terminal

from collections import Counter
from argparse import ArgumentParser

import requests
from bs4 import BeautifulSoup


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-f", "--frequency", action="store_true", help="print tags by frequency"
    )
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    response = requests.get(args.url)
    webpage = response.text.lower()

    soup = BeautifulSoup(webpage, "html5lib")

    tags = soup.find_all()
    names = [tag.name for tag in tags]

    tags_counter = Counter()
    for tag in names:
        tags_counter[tag] += 1

    if args.frequency:
        for tag, counter in reversed(tags_counter.most_common()):
            print(f"{tag} {counter}")
    else:
        for tag, counter in sorted(tags_counter.items()):
            print(f"{tag} {counter}")


if __name__ == "__main__":
    main()

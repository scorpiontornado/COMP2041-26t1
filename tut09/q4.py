#!/usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 9, Q3 (tags)
# Fetch specified web page and count the HTML tags in them

import sys, re, subprocess
from collections import Counter
from argparse import ArgumentParser


def main():
    # TODO: replace with argparse: support -f (frequency) and url
    parser = ArgumentParser()
    parser.add_argument(
        "-f", "--frequency", action="store_true", help="print tags by frequency"
    )
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    process = subprocess.run(
        ["wget", "-q", "-O-", args.url], capture_output=True, text=True
    )
    webpage = process.stdout.lower()

    # remove comments
    webpage = re.sub(r"<!--.*?-->", "", webpage, flags=re.DOTALL)

    # get all tags
    # note: use of capturing in re.findall returns list of the captured part
    tags = re.findall(r"<\s*(\w+)", webpage)

    # using collections.counter, alternatively can use a dict to count
    tags_counter = Counter()
    for tag in tags:
        tags_counter[tag] += 1

    # def get_second_item(x):
    #     return x[1]

    if args.frequency:
        # for tag, counter in reversed(tags_counter.most_common()):
        # for tag, counter in tags_counter.most_common()[::-1]:
        # for tag, counter in sorted(tags_counter.items(), key=get_second_item):
        for tag, counter in sorted(tags_counter.items(), key=lambda x: x[1]):
            print(f"{tag} {counter}")

    else:
        for tag, counter in sorted(tags_counter.items()):
            print(f"{tag} {counter}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 9, Q3 (tags)
# Fetch specified web page and count the HTML tags in them

import sys, re, subprocess
from collections import Counter


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    process = subprocess.run(["wget", "-q", "-O-", url], capture_output=True, text=True)
    webpage = process.stdout.lower()

    # webpage = """<!-- comment number one -->
    # blah
    # <!-- comment number two -->
    # """
    webpage = re.sub(r"<!--.*?-->", "", webpage, flags=re.DOTALL)

    tags = re.findall(r"<\s*(\w+)", webpage)

    # tags_counter = Counter()
    # for tag in tags:
    #     tags_counter[tag] += 1

    tags_counter = Counter(tags)

    for tag, count in sorted(tags_counter.items()):
        print(f"{tag} {count}")


if __name__ == "__main__":
    main()

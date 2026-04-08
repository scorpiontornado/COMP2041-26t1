#!/usr/bin/env python3

# To install requests:
# > python3 -m venv .venv
# > source .venv/bin/activate
# > pip3 install requests
#
# You'll need to re-run `source .venv/bin/activate` in each new terminal
import sys, subprocess, re, requests


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        exit(1)

    for url in sys.argv[1:]:
        # !!! DANGEROUS (vulnerable to command injection) !!!
        #     e.g.: ./q7.py 'https://www.unsw.edu.au; touch hello'
        # process = subprocess.run(
        #     f"wget -q -O- {url}", shell=True, capture_output=True, text=True
        # )

        # Safe from command injection (arguments passed directly to wget, not run in shell)
        process = subprocess.run(
            ["wget", "-q", "-O-", url], capture_output=True, text=True
        )

        webpage = process.stdout

        # res = requests.get(url)
        # webpage = res.text

        # Assume the digits of phone numbers may be separated by zero or more
        # spaces or hyphens ('-') and can contain between 8 and 15 digits inclusive.
        for num in re.findall(r"[\d \-]+", webpage):
            num = re.sub(r"\D", "", num)
            if len(num) >= 8 and len(num) <= 15:
                print(num)


if __name__ == "__main__":
    main()

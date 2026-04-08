#! /usr/bin/env python3


def main():
    d = {
        "key": "value",
        "Andrew": "green",
        "Anne": "red",
        "John": "blue",
    }
    print_dict(d)


def print_dict(dictionary):
    for key, val in dictionary.items():
        print(f"[{key}] => {val}")


if __name__ == "__main__":
    main()

#! /usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 7, Q6
#
# "Modify the head program from the previous question so that, as well
# as handling an optional -n argument to specify how many lines, it also
# handles multiple files on the command line and displays the first n
# lines from each file, separating them by a line of the form ==>
# FileName <===."

# ./q6.py
# ./q6.py -5
# ./q6.py filename filename2
# ./q6.py -5 filename filename2
# ./q6.py -5 filename -

import sys, itertools

n_lines = 10
if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
    # TODO: error handling - invalid command line arg
    arg = sys.argv.pop(1)
    n_lines = int(arg[1:])

if len(sys.argv) == 1:
    sys.argv.append("-")

for filename in sys.argv[1:]:
    try:
        print(f"==> {filename} <==")

        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        # for i, line in enumerate(stream):
        #     if i >= n_lines:
        #         break
        #     sys.stdout.write(line)

        for line in itertools.islice(stream, n_lines):
            sys.stdout.write(line)

        if stream != sys.stdin:
            stream.close()
    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")

#! /usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 7, Q8
#
# "Modify the cat program from the previous question so that it also
# accepts a -v command line option to display all characters in the file
# in printable form.
#
# In particular, end of lines should be shown by a $ symbol (useful for
# finding trailing whitespace in lines) and all control characters
# (ascii code less than 32) should be shown as ^X (where X is the
# printable character obtained by adding the code for 'A' to the control
# character code). So, for example, tabs (ascii code 9) should display
# as ^I."

### Version 2: using str.translate() ###
import sys

number = False
verbose = False

while len(sys.argv) > 1 and sys.argv[1].startswith("-"):
    arg = sys.argv.pop(1)
    arg = arg[1:]
    if arg == "n":
        number = True
    elif arg == "v":
        verbose = True

if len(sys.argv) == 1:
    sys.argv.append("-")

counter = 1
for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:

            if verbose:
                trans = str.maketrans(
                    {i: "^" + chr(i + ord("A") - 1) for i in range(32) if i != 10}
                )
                line = line.translate(trans).replace("\n", "$\n")

            if number:
                sys.stdout.write(f"{counter:6}  {line}")
            else:
                sys.stdout.write(line)
            counter += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")

#!/usr/bin/env sh

# COMP2041 26T1, W11B Tutorial 10, Q5
#
# A script that emails each of the 50,000 source (.c) files in /usr/src/linux
# to Andrew (andrewt@unsw.edu.au), each as an attachment to a separate email.
# The source files may be anywhere in a directory tree than goes 10+ levels deep.

# directory=/usr/src/linux
directory=/Users/nicholas/Developer/

# Assumes pathnames don't contain whitespace

# for c_file in $(find "$directory" -type f -name "*.c")
# do
#     echo mutt -s "C for you"  -a "$c_file" -- andrewt@unsw.edu.au
# done

find "$directory" -type f -name "*.c" \
    -exec echo mutt -s "C for you"  -a "{}" -- andrewt@unsw.edu.au \;

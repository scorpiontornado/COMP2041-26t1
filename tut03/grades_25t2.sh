#! /usr/bin/env dash

# COMP2041 tut03 q12
#
# Implement a shell script, grades.sh, that reads a sequence of (studentID,
# mark) pairs from its standard input, and writes (studentID, grade) pairs to
# its standard output. The input pairs are written on a single line, separated
# by spaces, and the output should use a similar format. The script should also
# check whether the second value on each line looks like a valid mark, and
# output an appropriate message if it does not. The script can ignore any extra
# data occurring after the mark on each line.

while read -r id mark _; do
    echo -n "$id "

    if [ "$mark" -eq "$mark" ] 2> /dev/null && [ "$mark" -ge 0 ] && [ "$mark" -le 100 ]; then
        if   [ "$mark" -lt 50 ]; then
            echo FL
        elif [ "$mark" -lt 65 ]; then
            echo PS
        elif [ "$mark" -lt 75 ]; then
            echo CD
        elif [ "$mark" -lt 85 ]; then
            echo DN
        else
            echo HD
        fi
    else
        echo "?? ($mark)" >& 2
    fi
done

### V2, using case ###
# #! /usr/bin/env dash

# while read -r id mark _; do
#     echo -n "$id "

#     if [ "$mark" -eq "$mark" ] 2> /dev/null && [ "$mark" -ge 0 ] && [ "$mark" -le 100 ]; then
#         case "$mark" in
#             [0-9]|[1-4][0-9])
#                 echo "FL"
#                 ;;
#             5[0-9]|6[0-4])
#                 echo "PS"
#                 ;;
#             6[5-9]|7[0-4])
#                 echo "CR"
#                 ;;
#             7[5-9]|8[0-4])
#                 echo "DN"
#                 ;;
#             *)
#                 echo "HD"
#                 ;;
#         esac
#     else
#         echo "?? ($mark)"
#     fi
# done

### Starter code ###
# #!/bin/sh
# while read id mark
# do
#     # ... insert mark/grade checking here ...
# done

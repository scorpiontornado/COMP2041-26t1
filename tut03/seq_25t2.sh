#! /usr/bin/env dash

# COMP2041 tut03 q4
#
# Implement a shell script called seq.sh for writing sequences
# of integers onto its standard output, with one integer per line. The script
# can take up to three arguments, and behaves as follows:
# - seq.sh LAST writes all numbers from 1 up to LAST, inclusive.
# - seq.sh FIRST LAST writes all numbers from FIRST up to LAST, inclusive.
# - seq.sh FIRST INCREMENT LAST writes all numbers from FIRST to LAST in steps
#   of INCREMENT, inclusive; that is, it writes the sequence FIRST, FIRST +
#   INCREMENT, FIRST + 2*INCREMENT, ..., up to the largest integer in this
#   sequence less than or equal to LAST.

# $# is the number of cmd line args
case $# in
    1)
        # 1 argument -> last of range
        first=1
        increment=1
        last=$1
        ;;
    2)
        # 2 arguments -> first and last
        first=$1
        increment=1
        last=$2
        ;;
    3)
        # 3 arguments -> first, increment, last
        first=$1
        increment=$2
        last=$3
        ;;
    *)
        # Else (not 1, 2, or 3)
        # >& 2 redirects to stderr, exit 1 indicates failure
        echo "Usage: $0 [FIRST [INCREMENT]] LAST" >& 2
        exit 1
esac

# Check values are integers
if [ "$first" -eq "$first" ] 2> /dev/null; then
    :
else
    echo "$0: Error <FIRST> must be an integer" >& 2
    exit
fi

if [ "$increment" -eq "$increment" ] 2> /dev/null; then
    if [ "$increment" -gt 0 ]; then
        :
    else
        echo "$0: Error <INCREMENT> must be positive" >& 2
        exit
    fi
else
    echo "$0: Error <INCREMENT> must be an integer" >& 2
    exit
fi

if [ "$last" -eq "$last" ] 2> /dev/null; then
    if [ "$last" -gt "$first" ]; then
        :
    else
        echo "$0: Error <LAST> must be greater than <FIRST>" >& 2
        exit
    fi
else
    echo "$0: Error <LAST> must be an integer" >& 2
    exit
fi

i="$first"
last="$1"

while [ "$i" -le "$last" ]
do
    echo "$i"
    i=$(( i + increment ))
done

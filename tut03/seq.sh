#! /usr/bin/env dash

if test $# -eq 1
then
    CURRENT=1
    LAST="$1"
else
    CURRENT="$1"
    LAST="$2"
fi

if test "$FIRST" -eq "$FIRST" 2> /dev/null
then
    :
else
    echo "$0: Error <FIRST> must be an integer" >&2
    exit
fi

while test $CURRENT -le $LAST; do
    echo $CURRENT
    CURRENT=$((CURRENT + 1))
done

# echo $?
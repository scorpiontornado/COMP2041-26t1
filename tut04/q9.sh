#!/bin/dash

if [ $# -ne 1 ] && ! [ "$1" -eq "$1" ] 2> /dev/null || [ "$1" -lt 0 ]; then
    echo "Usage: $0 <positive-number>"
    exit 2
fi

number="$1"

if [ "$number" -eq 1 ]; then
    echo "$number is not prime"
    exit 1
fi

# check numbers while i * i <= $number
i=2
while [ $((i * i)) -le "$number" ]; do
    if [ $((number % i)) -eq 0 ]; then 
        echo "$number is not prime"
        exit 1
    fi
    i=$((i + 1))
done

echo "$number is prime"
exit 0

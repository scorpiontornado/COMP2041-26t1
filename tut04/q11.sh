#! /bin/dash

if test $# = 0; then
    echo "Usage $0: <program>" >&2
    exit 1
fi

for program in "$@"; do
    found=''

    # echo "$PATH" |
    # tr ':' '\n' |
    # while read directory; do

    directories=$(echo "$PATH" | tr ':' '\n')
    # TODO: spaces in directory names?
    for directory in $directories; do
        filepath="$directory/$program"
        if [ -x "$filepath" ]; then
            ls -ld "$filepath"`
            found=1
            break
        fi
    done
    if [ -z "$found" ]; then
        echo "$program not found"
    fi
done

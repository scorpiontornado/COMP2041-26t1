#! /usr/bin/env dash

# COMP2041 26T1
# Tutorial 5, Q6
#
# "Write a shell script extract.sh that, when given one or more archive files as
# command line arguments, will use the correct program to extract the files."

if [ $# -eq 0 ]; then
    echo "Usage: $0 <file> [<file> ...]"
    exit 2;
fi

status=0

for archive in "$@"; do
    if [ ! -f "$archive" ]; then
        echo "$0: error: '$archive' is not a file" >&2
        status=1
        continue
    fi

    case "$archive" in
        *.tar)  tar xf "$archive" ;;
        *.zip)  unzip "$archive" ;;
        *.rar)  rar x "$archive" ;;
        *)
            echo "$0: error: format not recognised for '$archive'" >&2
            status=1
        ;;
    esac
done

exit $status

#!/bin/dash

# Command-line arguments, number of arguments, and the first argument,
# respectively ($0, the program name, isn't included in $@ or $#)
# echo $@
# echo $#
# echo $1

for file in $@; do
    if [ ! -f "$file" ]; then
        continue
    fi
    temporary_file=$(mktemp)

    sed -E 's/COMP2041/COMP2042/g; s/COMP9044/COMP9042/g' "$file" > "$temporary_file" && mv "$temporary_file" "$file"

    rm -f "$temporary_file"
done

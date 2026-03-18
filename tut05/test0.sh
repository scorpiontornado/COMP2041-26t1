#! /usr/bin/env/ dash

# ==============================================================================
# test0.sh
# Test the turnip-submit command.
#
# Written by: Nicholas Langford <z5487536@ad.unsw.edu.au>
# Date: 2026-03-18
# For COMP2041/9044 Assignment 1
# ==============================================================================


# Add the current directory to the PATH so scripts
# can still be executed from it after we cd
PATH="$PATH:$(pwd)"

# Create a temporary directory for the test and retrieve the provided test files
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1
2041 fetch turnip

# Create a temporary directory for the reference and retrieve the provided test files
ref_dir="$(mktemp -d)"
cd "$ref_dir" || exit 1
2041 fetch turnip

actual_stdout="$(mktemp)"
actual_stderr="$(mktemp)"
expected_stdout="$(mktemp)"
expected_stderr="$(mktemp)"

trap 'rm "$actual_stdout" "$actual_stderr" "$expected_stdout" "$expected_stderr" -r "$test_dir" "$ref_dir"' INT HUP QUIT TERM EXIT

cd "$test_dir" || exit 1
turnip-add lab01_multiply multiply.tests > "$actual_stdout" 2> "$actual_stderr"
actual_exit_code=$?

cd "$ref_dir" || exit 1
2041 turnip-add lab01_multiply multiply.tests  > "$expected_stdout" 2> "$expected_stderr"
expected_exit_code=$?

if ! diff "$actual_stdout" "$expected_stdout" > /dev/null 2> &1; then
    echo "Failed test - stdout differs"
    diff "$actual_stdout" "$expected_stdout"
    exit 1
fi

if ! diff "$actual_stderr" "$expected_stderr" > /dev/null 2> &1; then
    echo "Failed test - stderr differs"
    diff "$actual_stderr" "$expected_stderr"
    exit 1
fi

if [ "$actual_exit_code" -ne "$expected_exit_code" ]; then
    echo "Failed test - exit code differs"
    echo "Expected: $expected_exit_code"
    echo "Got: $actual_exit_code"
    exit 1
fi

# Make a submission
cd "$test_dir" || exit 1
turnip-submit lab01_multiply z5487536 multiply.sh > "$actual_stdout" 2> "$actual_stderr"
actual_exit_code=$?

cd "$ref_dir" || exit 1
2041 turnip-add lab01_multiply z5487536 multiply.sh > "$expected_stdout" 2> "$expected_stderr"
expected_exit_code=$?

if ! diff "$actual_stdout" "$expected_stdout" > /dev/null 2> &1; then
    echo "Failed test - stdout differs"
    diff "$actual_stdout" "$expected_stdout"
    exit 1
fi

if ! diff "$actual_stderr" "$expected_stderr" > /dev/null 2> &1; then
    echo "Failed test - stderr differs"
    diff "$actual_stderr" "$expected_stderr"
    exit 1
fi

if [ "$actual_exit_code" -ne "$expected_exit_code" ]; then
    echo "Failed test - exit code differs"
    echo "Expected: $expected_exit_code"
    echo "Got: $actual_exit_code"
    exit 1
fi


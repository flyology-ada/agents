#!/bin/sh

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
detector=$script_dir/../scripts/check-power-profile.sh
fixture_path=$script_dir/bin
failures=0

run_case() {
    test_case=$1
    expected_status=$2
    expected_profile=$3
    expected_reduced=$4
    expected_source=$5

    output=$(TEST_CASE=$test_case PATH="$fixture_path:$PATH" "$detector")
    status=$?
    expected_output=$(printf \
        'os=macos\ndetector=pmset\nprofile=%s\nreduced_performance=%s\npower_source=%s\n' \
        "$expected_profile" "$expected_reduced" "$expected_source")

    if [ "$status" -ne "$expected_status" ] || [ "$output" != "$expected_output" ]; then
        printf 'FAIL: %s\nexpected status: %s\nactual status: %s\nexpected output:\n%s\nactual output:\n%s\n' \
            "$test_case" "$expected_status" "$status" "$expected_output" "$output" >&2
        failures=$((failures + 1))
    else
        printf 'PASS: %s\n' "$test_case"
    fi
}

run_case selected-high 0 high-power false "AC Power"
run_case battery-low 10 low-power true "Battery Power"
run_case selected-automatic 0 automatic false "AC Power"
run_case unknown-powermode 2 unknown unknown "AC Power"
run_case legacy-high 0 high-power false "AC Power"
run_case legacy-low 10 low-power true "AC Power"
run_case legacy-automatic 0 automatic false "AC Power"
run_case legacy-conflict 2 unknown unknown "AC Power"
run_case missing-profile 2 unknown unknown "AC Power"
run_case missing-source 2 unknown unknown unknown

if [ "$failures" -ne 0 ]; then
    printf '%s test case(s) failed\n' "$failures" >&2
    exit 1
fi

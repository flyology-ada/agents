#!/bin/sh

# Apple documents Automatic, Low Power, and High Power as the macOS power
# modes: https://support.apple.com/101613
detect_macos() {
    if ! command -v system_profiler >/dev/null 2>&1; then
        emit_result macos system_profiler unknown unknown unknown
        return 2
    fi

    active=$(
        LC_ALL=C system_profiler SPPowerDataType 2>/dev/null |
            awk '
                function report_source(    profile) {
                    if (!reported && current) {
                        if (low && !high)
                            profile = "low-power"
                        else if (high && !low)
                            profile = "high-power"
                        else if (!low && !high && (saw_low || saw_high))
                            profile = "automatic"
                        else
                            profile = "unknown"

                        print source "|" profile
                        reported = 1
                    }
                }

                /^      [^[:space:]][^:]*:$/ {
                    report_source()
                    source = $0
                    sub(/^[[:space:]]+/, "", source)
                    sub(/:$/, "", source)
                    current = low = high = saw_low = saw_high = 0
                    next
                }

                /^[[:space:]]+Current Power Source: Yes$/ { current = 1 }
                /^[[:space:]]+Low Power Mode:/ {
                    saw_low = 1
                    if ($NF == "Yes")
                        low = 1
                }
                /^[[:space:]]+High Power Mode:/ {
                    saw_high = 1
                    if ($NF == "Yes")
                        high = 1
                }

                END { report_source() }
            '
    )

    if [ -z "$active" ]; then
        emit_result macos system_profiler unknown unknown unknown
        return 2
    fi

    power_source=${active%%|*}
    profile=${active#*|}

    case "$profile" in
        low-power)
            emit_result macos system_profiler "$profile" true "$power_source"
            return 10
            ;;
        automatic | high-power)
            emit_result macos system_profiler "$profile" false "$power_source"
            return 0
            ;;
        *)
            emit_result macos system_profiler unknown unknown "$power_source"
            return 2
            ;;
    esac
}

# powerprofilesctl documents `get` as printing the active profile:
# https://gitlab.freedesktop.org/upower/power-profiles-daemon
# The fallback values are standardized by the Linux sysfs ABI:
# https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-platform_profile
detect_linux() {
    profile=
    detector=

    if command -v powerprofilesctl >/dev/null 2>&1; then
        profile=$(powerprofilesctl get 2>/dev/null | awk 'NF { print $1; exit }')
        if [ -n "$profile" ]; then
            detector=powerprofilesctl
        fi
    fi

    if [ -z "$profile" ] && [ -r /sys/firmware/acpi/platform_profile ]; then
        profile=$(awk 'NF { print $1; exit }' /sys/firmware/acpi/platform_profile)
        if [ -n "$profile" ]; then
            detector=platform_profile
        fi
    fi

    if [ -z "$profile" ]; then
        emit_result linux unavailable unknown unknown unknown
        return 2
    fi

    case "$profile" in
        power-saver | low-power | cool | quiet)
            emit_result linux "$detector" "$profile" true unknown
            return 10
            ;;
        balanced | balanced-performance | performance)
            emit_result linux "$detector" "$profile" false unknown
            return 0
            ;;
        *)
            emit_result linux "$detector" "$profile" unknown unknown
            return 2
            ;;
    esac
}

emit_result() {
    printf 'os=%s\ndetector=%s\nprofile=%s\nreduced_performance=%s\npower_source=%s\n' \
        "$1" "$2" "$3" "$4" "$5"
}

case "$(uname -s 2>/dev/null)" in
    Darwin)
        detect_macos
        exit $?
        ;;
    Linux)
        detect_linux
        exit $?
        ;;
    *)
        emit_result unsupported unavailable unknown unknown unknown
        exit 2
        ;;
esac

#!/usr/bin/env python3


"""log parsing module"""

import sys
import re
import signal

# Initialize variables
TOTAL_SIZE = 0
STATUS_CODES = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
LINE_COUNT = 0

# Regular expression to match the input format
PATTERN = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    r'\[.+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Print the current statistics."""
    print(f'File size: {TOTAL_SIZE}')
    for code in sorted(STATUS_CODES.keys()):
        if STATUS_CODES[code] > 0:
            print(f"{code}: {STATUS_CODES[code]}")
    sys.stdout.flush()


def signal_handler(sig, frame):
    """Handle CTRL+C interrupt."""
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


def main():
    """Main function to process input and compute metrics."""
    global TOTAL_SIZE, LINE_COUNT

    for line in sys.stdin:
        match = re.match(PATTERN, line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            TOTAL_SIZE += file_size
            if status_code in STATUS_CODES:
                STATUS_CODES[status_code] += 1

            LINE_COUNT += 1

            if LINE_COUNT % 10 == 0:
                print_stats()

    # Print final stats if the total number of lines is not a multiple of 10
    if LINE_COUNT % 10 != 0:
        print_stats()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""A script for parsing and processing HTTP request logs."""

import re

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def main():
    """Starts the log parser to read input and compute statistics."""
    line_count = 0

    try:
        while True:
            line = input()
            update_stats(line)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
    except (KeyboardInterrupt, EOFError):
        print_statistics()


def parse_input(input_line):
    """Extracts sections of a line from an HTTP request log.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: A dictionary containing the status code and file size, or None if the line is invalid.
    """
    pattern = (
        r"(?P<ip>\S+)\s*"
        r"-\s*\[(?P<date>[^\]]+)\]\s*"
        r'"(?P<request>[^"]+)"\s*'
        r"(?P<status_code>\d{3})\s*"
        r"(?P<file_size>\d+)"
    )
    match = re.fullmatch(pattern, input_line.strip())
    if match:
        return {
            "status_code": match.group("status_code"),
            "file_size": int(match.group("file_size")),
        }
    return None


def print_statistics():
    """Prints the accumulated statistics of the HTTP request log."""
    global total_size, status_codes
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def update_stats(line):
    """Updates the stats from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the stats.
    """
    global total_size, status_codes
    line_info = parse_input(line)
    if line_info:
        status_code = line_info["status_code"]
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += line_info["file_size"]


if __name__ == "__main__":
    main()

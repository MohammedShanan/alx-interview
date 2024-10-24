#!/usr/bin/python3
"""A script for parsing and processing HTTP request logs."""

import re


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


def print_statistics(total_size, status_codes):
    """Prints the accumulated statistics of the HTTP request log.

    Args:
        total_size (int): The total file size processed.
        status_codes (dict): The counts of each status code encountered.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def update_stats(line, total_size, status_codes):
    """Updates the stats from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the stats.
        total_size (int): The current total file size.
        status_codes (dict): The current counts of status codes.

    Returns:
        tuple: Updated total size and status codes.
    """
    line_info = parse_input(line)
    if line_info:
        status_code = line_info["status_code"]
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += line_info["file_size"]
    return total_size, status_codes


def main():
    """Starts the log parser to read input and compute statistics."""
    line_count = 0
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

    try:
        while True:
            line = input()
            total_size, status_codes = update_stats(line, total_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()

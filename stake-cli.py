#!/usr/bin/env python3
import argparse

# Define version number
VERSION = "0.1.13"

def main():
    parser = argparse.ArgumentParser(description="Stake Blockchain CLI")

    # Add CLI arguments
    parser.add_argument("-v", "--version", action="version", version=f"Stake v{VERSION}", help="Show version number")

    args = parser.parse_args()

if __name__ == "__main__":
    main()

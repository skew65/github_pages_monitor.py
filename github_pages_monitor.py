#!/usr/bin/env python

import argparse
import requests
import os

# File to store the previous version of the website's content
previous_file = "previous_content.html"

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Monitor changes in GitHub Pages websites.")
parser.add_argument("urls", nargs="+", help="URLs of the GitHub Pages websites to monitor")
args = parser.parse_args()

# Iterate over each URL
for url in args.urls:
    # Request the HTML content of the website
    response = requests.get(url)
    new_content = response.text

    # Load the previous content from the file
    try:
        with open(previous_file, "r") as file:
            previous_content = file.read()
    except FileNotFoundError:
        previous_content = ""

    # Compare the previous and new content to find the new text
    if new_content != previous_content:
        new_text = new_content.replace(previous_content, "")
        print(f"New text found in {url}:")
        print(new_text)

        # Update the previous content file with the new content
        with open(previous_file, "w") as file:
            file.write(new_content)
    else:
        print(f"No new text found in {url}.")

# Make the script executable
os.chmod(__file__, 0o755)

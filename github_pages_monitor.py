#!/usr/bin/env python

import sys
import requests
import os

# File to store the previous version of the website's content
previous_file = "previous_content.html"

# Check if the URL argument is provided
if len(sys.argv) < 2:
    print("Please provide the URL of the GitHub Pages website as a command-line argument.")
    sys.exit(1)

# Extract the URL from the command-line argument
url = sys.argv[1]

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
    print("New text found:")
    print(new_text)

    # Update the previous content file with the new content
    with open(previous_file, "w") as file:
        file.write(new_content)
else:
    print("No new text found.")

# Make the script executable
os.chmod(__file__, 0o755)

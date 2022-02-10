#! /usr/bin/python3
# ssnScrubber.py - Removes SSN information when detected in copy.
import pyperclip
import re

text = str(pyperclip.paste())

# Regex for finding SSNs in string.

ssnRegex = re.compile(r'''(
    (\d\d\d)+   # First part of SSN, area number.
    (-)+        # seperator
    (\d\d)+     # Second part of SSN, group number.
    (-)+        # seperator
    (\d\d\d\d)+ # Final part of SSN, serial number.
)''',re.VERBOSE)

# Find matches in clipboard text.

matches = []
for groups in ssnRegex.findall(text):
    ssnNum = '-'.join(['XXX', 'XX', groups[5]])
    matches.append(ssnNum)

# Print it to the screen.
if len(matches) > 0:
    # pyperclip.copy('\n'.join(matches))
    print("PII detected in the clipboard.")
    print('\n'.join(matches))
    print("SSN\'s scrubbed.")
else:
    print('No PII/SSN\'s detected.')
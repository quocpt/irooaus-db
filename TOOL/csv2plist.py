#!/usr/bin/env python3

"""csv2plist

Convert CSV to PLIST file.
**Require Python 3

The first row of CSV works as the key rows
Each row in the csv file will convert into a dictionary with key rows.

For example:
CSV:
    key1,key2,key3
    val1,val2,val3
    valA,valB,valC
PYTHON:
    [
        {
            'key1': 'val1',
            'key2': 'val2',
            'key3': 'val3'
        },
        {
            'key1': 'valA',
            'key2': 'valB',
            'key3': 'valC'
        }
    ]
PLIST:
    <array>
        <dict>
            <key>key1</key><string>val1</string>
            <key>key2</key><string>val2</string>
            <key>key3</key><string>val3</string>
        </dict>
        <dict>
            <key>key1</key><string>valA</string>
            <key>key2</key><string>valB</string>
            <key>key3</key><string>valC</string>
        </dict>
    </array>
"""
import sys
import csv
import plistlib
import os

def main():
    # Get csv file path from argument
    try:
        csv_file = sys.argv[1]
    except IndexError:
        print('Where\'s input file?')
        return 1

    # Read file in. Use utf-8 encoding with Python 3
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            # Check python documentation about csv.DictReader
            csv_reader = csv.DictReader(f)
            # Make reader become result list
            result = list(csv_reader)
    except IOError:
        print('Invalid file path')
        return 2

    # Generate plist file path from csv file path
    # Original: /Users/someone/example.csv
    # Output: /Users/someone/example.plist
    plist_file = os.path.splitext(csv_file)[0] + '.plist'
    # Write
    plistlib.writePlist(result, plist_file)

    return 0

if __name__=="__main__":
    sys.exit( main() )
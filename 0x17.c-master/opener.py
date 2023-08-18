#!/usr/bin/python3
import dis
import sys

with open('crackme4', 'rb') as file:
    magic = file.read(4)  # Read the magic number (4 bytes)
    timestamp = file.read(4)  # Read the timestamp (4 bytes)
    code = file.read()  # Read the bytecode

with open('disassembled_code.txt', 'w') as output_file:
    original_stdout = sys.stdout
    sys.stdout = output_file
    try:
        dis.dis(code)
    finally:
        sys.stdout = original_stdout

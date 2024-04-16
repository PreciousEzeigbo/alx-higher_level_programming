#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints to stdout"""


def read_file(filename=""):
    """The function that reads the file and prints to stduot"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            #  Print the contents to stduot
            print(line)

#!/usr/bin/python3
"""Print text with blank lines after selected punctuation."""


def text_indentation(text):
    """Print text with two newlines after each '.', '?' or ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    index = 0
    while index < len(text):
        if text[index] in ".?:":
            line = text[start:index + 1].strip()
            if line:
                print("\n".join(part.strip() for part in line.splitlines()))
                print()
            index += 1
            while index < len(text) and text[index].isspace():
                index += 1
            start = index
        else:
            index += 1

    line = text[start:].strip()
    if line:
        print("\n".join(part.strip() for part in line.splitlines()), end="")

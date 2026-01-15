#!/usr/bin/env python3

def islower(c):
    """Checks for lowercase character."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

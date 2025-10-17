# tuilibpy/textpro.py - Helps render headers, footers, and misc text in the terminal
# (C) Copyright 2025 Ben Daws

import sys
import os
import math

def _is(obj, *values):
    for v in values:
        if obj == v:
            return True
    
    return False

# Note: width=0 means that the width will be set to the terminal's width.
def write(text, anchor="left", spacer=" ", width=0):
    realWidth = 0

    if width != 0:
        realWidth = width
    else:
        tw, _ = os.get_terminal_size()
        realWidth = tw

    if not _is(anchor, "left", "right", "center"):
        return
    
    prefix = ""
    suffix = ""

    if realWidth < len(text):
        realWidth = len(text)

    match anchor:
        case "left":
            suffix = spacer

            for _ in range(len(text), realWidth):
                suffix += spacer[0]
            
            prefix = ""
        case "right":
            for _ in range(len(text), realWidth):
                prefix += spacer[0]
            
            prefix += spacer

            suffix = ""
        case "center":
            each = math.floor((realWidth - len(text)) / 2)

            for _ in range(each):
                prefix += spacer
            
            for _ in range(each):
                suffix += spacer

    sys.stdout.write(f"{prefix}{text}{suffix}\n")
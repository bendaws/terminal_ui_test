# tuilibpy/infobox.py - Very pretty box in your terminal
# (C) Copyright 2025 Ben Daws

import sys
import math

# Needed for substring stuff
# Uses "clean" splitting so words are not seperated (in theory)
def split_string_by_chars(text, max_length):
    lines = []
    current_line = []
    current_length = 0

    words = text.split()

    for word in words:
        word_length_with_space = len(word) + (1 if current_line else 0)

        if current_length + word_length_with_space > max_length:
            if current_line:
                lines.append(" ".join(current_line))
            
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += word_length_with_space

    if current_line:
        lines.append(" ".join(current_line))

    return lines

def _is(obj, *values):
    for v in values:
        if obj == v:
            return True
    
    return False

# Write an infobox to the screen with the provided text and dimensions.
def write(title, text, width = 80, height=5, anchorTitle = "left", ansiStylingTitle = "\033[1;34m", ansiStylingText = "\033[0m"):
    # Validate arguments
    if not _is(anchorTitle.lower(), "left", "right", "center"):
        return
    
    writtenHeight = 0
    
    if len(title) > (width - 4):
        # Shorten the title to fit width constraints
        allowedCharacters = width - 7
        sys.stdout.write(f"= {ansiStylingTitle}{title[:allowedCharacters]}\033[0m... =\n")
    else:
        # Good enough
        # We also apply anchoring settings here

        match anchorTitle.lower():
            case "left":
                sys.stdout.write(f"= {title} ")

                # Fill in the whitespace
                for _ in range((width - 4) - len(title)):
                    sys.stdout.write("=")
                
                # We're done
                sys.stdout.write("=\n")
            case "right":
                # This is the same as "left", but in reverse
                for _ in range((width - 4) - len(title)):
                    sys.stdout.write("=")
                
                sys.stdout.write(f" {ansiStylingTitle}{title}\033[0m =\n")
            case "center":
                eachSide = math.floor(((width) - len(title)) / 2) - 2
                writing = "="

                for _ in range(eachSide):
                    writing += "="
                
                writing += f" {ansiStylingTitle}{title}\033[0m "

                for _ in range(eachSide):
                    writing += "="
                
                if len(writing) < width:
                    # make sure we fill the space
                    writing += "="
                
                sys.stdout.write(f"{writing}=\n")
    
    writtenHeight += 1
    
    if str.find(text, "\n"):
        # Text has newlines so we will respect those constraints
        for subs in str.split(text, "\n"):
            # Check fitting
            if len(subs) > width - 4:
                # Not enough space

                for ssubs in split_string_by_chars(subs, width - 4):
                    if len(ssubs) == width - 4:
                        # no scaling needed
                        sys.stdout.write(f"| {ansiStylingText}{ssubs}\033[0m")
                    else:
                        sys.stdout.write(f"| {ansiStylingText}{ssubs}\033[0m")

                        for _ in range((width - 4) - len(ssubs)):
                            sys.stdout.write(" ")

                    sys.stdout.write(" |\n")
                
            else:
                sys.stdout.write(f"| {ansiStylingText}{subs}\033[0m")

                for _ in range((width - 4) - len(subs)):
                    sys.stdout.write(" ")
                
                sys.stdout.write(" |\n")
            
            writtenHeight += 1
    else:
        # Do it yourself buddy
        for subs in split_string_by_chars(text, width - 4):
            if len(subs) == width - 4:
                # no scaling needed
                sys.stdout.write(f"| {ansiStylingText}{subs}\033[0m")
            else:
                sys.stdout.write(f"| {ansiStylingText}{subs}\033[0m")

                for _ in range((width - 4) - len(subs)):
                    sys.stdout.write(" ")

            sys.stdout.write(" |")
            writtenHeight += 1

    if writtenHeight < height:
        for _ in range(height - writtenHeight):
            sys.stdout.write("|")

            for _ in range(width - 2):
                sys.stdout.write(" ")
            
            sys.stdout.write("|\n")
    
    # Ending bottom bar
    for _ in range(width):
        sys.stdout.write("=")
    
    sys.stdout.write("\n")
    sys.stdout.flush()

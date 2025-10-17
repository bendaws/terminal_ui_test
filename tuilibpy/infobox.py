import sys

# Needed for substring stuff
def split_string_by_chars(text, n):
    result = []

    for i in range(0, len(text), n):
        result.append(text[i:i+n])

    return result

# Write an infobox to the screen with the provided text and dimensions.
def write(title, text, width = 30):
    if len(title) > (width - 4):
        # Shorten the title to fit width constraints
        allowedCharacters = width - 7
        sys.stdout.write(f"= {title[:allowedCharacters]}... =\n")
    else:
        # Good enough
        sys.stdout.write(f"= {title} ")

        # Fill in the whitespace
        for _ in range((width - 4) - len(title)):
            sys.stdout.write("=")
        
        # We're done
        sys.stdout.write(" =\n")
    
    if str.find(text, "\n"):
        # Text has newlines so we will respect those constraints
        for subs in str.split(text, "\n"):
            # Check fitting
            if len(subs) > width - 4:
                # Not enough space

                for ssubs in split_string_by_chars(subs, width - 4):
                    if len(ssubs) == width - 4:
                        # no scaling needed
                        sys.stdout.write(f"| {ssubs}")
                    else:
                        sys.stdout.write(f"| {ssubs}")

                        for _ in range((width - 4) - len(ssubs)):
                            sys.stdout.write(" ")

                    sys.stdout.write(" |")
                
            else:
                sys.stdout.write(f"| {subs}")

                for _ in range((width - 4) - len(subs)):
                    sys.stdout.write(" ")
                
                sys.stdout.write(" |")
    else:
        # Do it yourself buddy
        for subs in split_string_by_chars(text, width - 4):
            if len(subs) == width - 4:
                # no scaling needed
                sys.stdout.write(f"| {subs}")
            else:
                sys.stdout.write(f"| {subs}")

                for _ in range((width - 4) - len(subs)):
                    sys.stdout.write(" ")

            sys.stdout.write(" |")
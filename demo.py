import tuilibpy.infobox

tuilibpy.infobox.write(
    title = "Welcome to tuilibpy!",
    text = "tuilibpy is a simple Python library designed to make TUIs simple, fast, and readable without needing the thought that normal TUI development does.",
    width = 80,
    height = 5, # This will only take effect if the text fits inside of the infobox,
                # otherwise, the height will be moved to fit all of the text.
    anchorTitle = "center",

    ansiStylingTitle = "\033[1;34m"
)
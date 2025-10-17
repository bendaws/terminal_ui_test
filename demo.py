import tuilibpy.infobox
import tuilibpy.textpro
import tuilibpy.terminalutils

tuilibpy.terminalutils.hide_cursor()
tuilibpy.terminalutils.clear_screen()

tuilibpy.infobox.write(
    title = "Welcome to tuilibpy!",
    text = "tuilibpy is a simple Python library designed to make TUIs simple, fast, and readable without needing the thought that normal TUI development does. You can see usage examples here.",
    width = 80,
    height = 5, # This will only take effect if the text fits inside of the infobox,
                # otherwise, the height will be moved to fit all of the text.
    anchorTitle = "center",

    ansiStylingTitle = "\033[1;34m"
)

tuilibpy.textpro.write(
    text = "\033[1;34mPress enter to continue\033[0m",
    anchor = "center",
    spacer = " ",
    width = 90
)

input()
tuilibpy.terminalutils.clear_screen()

tuilibpy.infobox.write(
    title = "Element: Infobox",
    text = "The infobox displays a title and text.\nYou can include newlines (\\n), tabs (\\t), and you can even customize the ANSI styling of the text through (ansiStylingTitle) and (ansiStylingText).\n\nYou can customize the anchoring of the title, as you will see in the next examples:",
    width = 80,
    anchorTitle = "center",

    ansiStylingTitle = "\033[1;32m"
)

tuilibpy.textpro.write(
    text = "\033[1;34mPress enter to continue\033[0m",
    anchor = "center",
    spacer = " ",
    width = 90
)

input()
tuilibpy.terminalutils.clear_screen()

tuilibpy.infobox.write(
    title = "anchorTitle = \"left\"",
    text = "This is the default.",
    width = 80,
    anchorTitle = "left",
    height = 1,
    ansiStylingTitle = "\033[1;32m"
)

tuilibpy.infobox.write(
    title = "anchorTitle = \"center\"",
    text = "The title is centered",
    width = 80,
    anchorTitle = "center",
    height = 1,
    ansiStylingTitle = "\033[1;32m"
)

tuilibpy.infobox.write(
    title = "anchorTitle = \"right\"",
    text = "Text is on the right.",
    width = 80,
    anchorTitle = "right",
    height = 1,
    ansiStylingTitle = "\033[1;32m"
)

tuilibpy.textpro.write(
    text = "\033[1;34mPress enter to continue\033[0m",
    anchor = "center",
    spacer = " ",
    width = 90
)

input()
tuilibpy.terminalutils.clear_screen()

tuilibpy.infobox.write(
    "tuilibpy.textpro",
    "The text displayed below is created using TextPro, which can anchor regular printing in the console the same as you would an infobox.",
    50,
    1,
    "center"
)

tuilibpy.textpro.write(
    text = "\033[1;32mI am TextPro\033[0m",
    anchor = "center",
    spacer = " ",
    width = 60
)

tuilibpy.textpro.write(
    text = "\033[1;32mI'm on the left'\033[0m",
    anchor = "left",
    spacer = " ",
    width = 60
)

tuilibpy.textpro.write(
    text = "\033[1;32mI'm on the right'\033[0m",
    anchor = "right",
    spacer = " ",
    width = 60
)

input()
tuilibpy.terminalutils.clear_screen()

tuilibpy.infobox.write(
    title = "tuilibpy",
    text = "This was a short demo of all the features implemented by tuilibpy.\n\nSource: https://github.com/bendaws/tuilibpy\n\nThank you!\n\t- Ben",
    width = 100,
    height = 1,
    anchorTitle = "center"
)

tuilibpy.terminalutils.show_cursor()
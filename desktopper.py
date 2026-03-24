#! /usr/bin/python3

from easygui import *

DIR = "~/.local/share/applications"

values = multenterbox(
    title = "desktopper",
    msg = "",
    fields= ["Display name:", "Path to executable:", "Path to icon:"]
)

name = values[0]
path = values[1]
icon = values[2]

filename = DIR + "/" + name + ".desktop"
content = """[Desktop Entry]
Name={}
Type=Application
Exec={}
Icon={}
""".format(name, path, icon)

file = open(filename, "x")
with open(filename, "w") as f:
    f.write(content)
msgbox("Done!")
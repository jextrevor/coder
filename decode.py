from pynput import keyboard
import clipboard
import re
controller = keyboard.Controller()
string = clipboard.paste()
binarystring = ""
outstring = ""
characters = [8203,8291]
pattern = re.compile(r".{1,16}")
for char in string:
    if ord(char) == 128:
        binarystring += "0"
    elif ord(char) == 129:
        binarystring += "1"
binarychunks = pattern.findall(binarystring)
for chunk in binarychunks:
    charcode = int(chunk,2)
    outstring += unichr(charcode)
clipboard.copy(outstring)

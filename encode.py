from pynput import keyboard
controller = keyboard.Controller()
string = ""
binaryout = ""
outstring = ""
characters = [8203,8291]
yes = False
def on_press(key):
    global yes
    yes = True

def on_release(key):
    global yes
    global shift, string
    if key == keyboard.Key.backspace:
        pass
    elif key == keyboard.Key.end:
        return False
    elif key == keyboard.Key.space:
        string += " "
        controller.press(keyboard.Key.backspace)
        controller.release(keyboard.Key.backspace)
    elif yes == True:
        try:
            string += key.char
            print ord(key.char)
        except:
            pass
        controller.press(keyboard.Key.backspace)
        controller.release(keyboard.Key.backspace)
    return True

def unicodetype(character):
    controller.press(keyboard.Key.ctrl_l)
    controller.press(keyboard.Key.shift_l)
    controller.press("u")
    controller.release("u")
    controller.release(keyboard.Key.shift_l)
    controller.release(keyboard.Key.ctrl_l)
    controller.type("{0:04x}".format(character))
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
for char in string:
    binaryout += "{0:016b}".format(ord(char))
print binaryout
for char in binaryout:
    if char == "0":
        unicodetype(characters[0])
    else:
        unicodetype(characters[1])

#convert the string to invisible characters
#type the invisible characters
controller.type(":)")
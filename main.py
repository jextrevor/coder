from pynput import keyboard

controller = keyboard.Controller()
shift = False
string = ""
def on_press(key):
    global shift
    if key == keyboard.Key.shift:
        shift = True

def on_release(key):
    global shift, string
    if key == keyboard.Key.backspace:
        pass
    elif key == keyboard.Key.enter:
        return False
    elif key == keyboard.Key.shift:
        shift = False
    elif key == keyboard.Key.space:
        string += " "
        controller.press(keyboard.Key.backspace)
        controller.release(keyboard.Key.backspace)
    else:
        try:
            string += key.char
        except:
            pass
        controller.press(keyboard.Key.backspace)
        controller.release(keyboard.Key.backspace)
    return True

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
controller.type(string)
controller.type(":)")
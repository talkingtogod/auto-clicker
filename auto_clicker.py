import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener

# delay and button to click (change if needed)
delay = 0.1  
button = Button.left 

start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.mouse = Controller()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)  
                time.sleep(self.delay)  
            time.sleep(0.01)

click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if not click_thread.running:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        return False  # stops listener bla bla (after stopping auto clicker the cmd closes!)

with Listener(on_press=on_press) as listener:
    listener.join()

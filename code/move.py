# '''   To comment out on Mac
import RPi.GPIO as GPIO
# from EmulatorGUI import GPIO
import state as state
import cache as c
import time


cache = c.Cache()

pins = [
    {'pin': 23, 'color': 'white', 'mode': 1, 'partner': 24, 'wheel': "back_left"},
    {'pin': 24, 'color': 'white', 'mode': 2, 'partner': 23, 'wheel': "back_left"},
    {'pin': 17, 'color': 'blue', 'mode': 1, 'partner': 27, 'wheel': "back_right"},
    {'pin': 27, 'color': 'blue', 'mode': 2, 'partner': 17, 'wheel': "back_right"},
    {'pin': 5, 'color': 'yellow', 'mode': 2, 'partner': 6, 'wheel': "front_left"},
    {'pin': 6, 'color': 'yellow', 'mode': 1, 'partner': 5, 'wheel': "front_left"},
    {'pin': 12, 'color': 'green', 'mode': 2, 'partner': 16, 'wheel': "front_right"},
    {'pin': 16, 'color': 'green', 'mode': 1, 'partner': 12, 'wheel': "front_right"}
]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in pins:
    GPIO.setup(pin['pin'], GPIO.OUT, initial=0)
    

def set_wheel(wheel: str, mode: int, state: int):
    for pin in pins:
        if pin.get('wheel') == wheel and (pin.get('mode') == mode or mode == 0):
            GPIO.output(pin.get('pin'), state)         
    

def toggle_mode(mode: int, state: int):
    pin_nums = [pin['pin'] for pin in pins if pin['mode'] == mode or mode == 0]
    for pin_num in pin_nums:
        GPIO.output(pin_num, state)
    

def forward():
    cache.update_state(state.Forward())
    update()
    

def backward():
    cache.update_state(state.Backward())
    update()


def brake():
    cache.update_state(state.Stationary())
    update()
    

def left():
    cache.update_state(state.Left())
    update()
 
 
def right():
    cache.update_state(state.Right())
    update()


def update():
    # print(f"->{cache.stack}<-")
    current_state = cache.get_state()
    # print(f"current_state: {current_state}")
    wheels = {
        "front_right": current_state.front_right,
        "back_right": current_state.back_right,
        "front_left": current_state.front_left,
        "back_left": current_state.back_left
        }
    for name, wheel in wheels.items():
        set_wheel(name, 0, 0)
        if wheel == "forward":
            set_wheel(name, 1, 1)
        elif wheel == "stationary":
            set_wheel(name, 0, 0)
        elif wheel == "backward":
            set_wheel(name, 2, 1)

        
if __name__ == '__main__':
    toggle_mode(0, 0)   # emergency kill switch

# '''

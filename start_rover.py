from pynput import keyboard
from subprocess import run, CompletedProcess


# Hijacks escape key to execute script
def monitor():
    try:
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.esc:
                    return
    except KeyboardInterrupt:
        print("\ninput no longer monitored\n")
        exit(0)


try:
    while True:
        monitor()
        rc: CompletedProcess = run("./rover")
except KeyboardInterrupt:
    print("\ninput no longer monitored\n")
    exit(0)



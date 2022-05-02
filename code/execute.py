import command as commands
import test as test
import state as state
import pygame
import subprocess
import move as move

screen: pygame.display


# executes a valid command by parsing it then using one of the below functions
def execute(command: commands.Command):
    if command.command is None:
        return command.command
    try:
        string = globals()[command.command](command)
        # print(string)
        return string
    except KeyError:
        return None


# functions
def forward(command: commands.Command):
    move.forward()
    return "driving forward"


def backward(command: commands.Command):
    move.backward()
    return "driving backward"


def left(command: commands.Command):
    move.left()
    return "turning left"


def right(command: commands.Command):
    move.right()
    return "turning right"


def picture(command: commands.Command):
    return "snapping picture"


def video(command: commands.Command):
    return "taking video"


def save(command: commands.Command):
    subprocess.run(['echo', 'saving stuff'])
    return "saving files locally"


def brake(command: commands.Command):
    move.brake()
    return "applying brakes"


def display(command: commands.Command = None):
    message = None
    background_color = (255, 255, 255)
    background_image = pygame.image.load('images/republic2.jpg')
    screen.fill(background_color)
    screen.blit(background_image, [0, 0])
    messages = {
        "1": "Keep calm: help is on the way",
        "2": "Take deep breaths"
    }
    try:
        message = messages.get(str(chr(command.input_integer)))
    except ValueError:
        message = messages.get("space")
    font = pygame.font.Font('freesansbold.ttf', 50)
    if message is not None:
        text = font.render(message, True, (0, 0, 0), (255, 255, 255))
        box = text.get_rect()
        box.center = (820 // 2, 680 // 2)
        screen.blit(text, box)
    pygame.display.update()
    return "displaying content"


if __name__ == "__main__":
    # tests
    test.test(execute(commands.Command(ord("w"))), "driving forward")
    test.test(execute(commands.Command(ord("s"))), "driving backward")
    test.test(execute(commands.Command(ord("d"))), "turning right")
    test.test(execute(commands.Command(ord("a"))), "turning left")
    test.test(execute(commands.Command(ord("x"))), "saving files locally")
    test.test(execute(commands.Command(ord("c"))), "snapping picture")
    test.test(execute(commands.Command(ord("v"))), "taking video")
    test.test(execute(commands.Command(1073742049)), "applying brakes")



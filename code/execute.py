import command as commands
import state as state
import test as test
import move as move


# executes a valid command by parsing it then using one of the below functions
def execute(command: commands.Command):
    if command.command is None:
        return command.command
    try:
        string = globals()[command.command]()
        # print(string)
        return string
    except KeyError:
        return None


# functions
# TODO: finalize and implement functions
def forward():
    move.forward()
    return "driving forward"


def backward():
    move.backward()
    return "driving backward"


def left():
    move.left()
    return "turning left"


def right():
    move.right()
    return "turning right"


def picture():
    return "snapping picture"


def video():
    return "taking video"


def save():
    return "saving files locally"


def brake():
    move.brake()
    return "applying brakes"


def display():
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



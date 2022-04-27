from datetime import datetime
import valid as valid
import test as test


class Command:
    # accepts a string as an argument, will autofill a timestamp and parse a command from inputted string
    def __init__(self, input_integer: int):
        self.timestamp = datetime.now()
        self.input_integer = input_integer
        self.command = parse_command(input_integer)

    def __str__(self):
        try:
            return f"\n{str(self.timestamp)} | {chr(self.input_integer)} -> {str(self.command)}"
        except ValueError:
            return f"\n{str(self.timestamp)} | {str(translate(self.input_integer))} -> {str(self.command)}"
        except TypeError:
            return f"\n{str(self.timestamp)} | unrecognized command "

    def set_command(self, command_string):
        self.command = command_string

    def get_command(self):
        return self.command

    def get_time(self):
        return self.timestamp


def translate(input_integer):
    translation = {
        1073742049: "shift",
        1073741881: "caps",
        32: "space"
    }
    return translation.get(input_integer)


def parse_command(input_integer):
    # checks if command string correlates with recognized command, if so, returns command, else returns None
    special_key = translate(input_integer)
    try:
        return valid.commands(chr(input_integer))
    except ValueError:
        return valid.commands(special_key)


if __name__ == "__main__":
    # tests
    test.test(Command(ord("w")).command, "forward")
    test.test(Command(ord("d")).command, "right")
    test.test(Command(ord("i")).command, "display")
    test.test(Command(ord("y")).command)
    test.test(Command(ord("5")).command)
    test.test(Command(20).command)


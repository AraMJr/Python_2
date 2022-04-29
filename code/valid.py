import pygame


def translate(key) -> int:
    special = {
        pygame.K_SPACE: 32,
        pygame.K_LSHIFT: 10,
        pygame.K_TAB: 9,
        pygame.K_ESCAPE: 200
    }
    # print(key, special.get(key))
    return special.get(key)


# checks if command string is recognized and returns it if so, otherwise returns None
def commands(input_string):
    # TODO: finalize valid commands and keys
    valid_commands = {
        "w": "forward",
        "s": "backward",
        "a": "left",
        "d": "right",
        "x": "save",
        "c": "picture",
        "v": "video",
        "j": "save",
        "k": "picture",
        "l": "video",
        "shift": "brake",
        "i": "display",
        "space": "display",
    }
    try:
        return valid_commands.get(input_string)
    except KeyError:
        return None


import command as commands
import execute as execute
import valid as valid
import pygame
# import camera


# def initialize():
#     camera.initialize()


def run_rover():
    pygame.font.init()
    background_color = (255, 255, 255)
    background_image = pygame.image.load('/home/pi/Code/egen-310-rover/images/republic2.jpg')
    # background_image = pygame.image.load('images/republic2.jpg')
    screen = pygame.display.set_mode((820, 680))
    execute.screen = screen
    pygame.display.set_caption('rover')
    screen.fill(background_color)
    screen.blit(background_image, [0, 0])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            output = None
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord("p")):
                print()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                special = valid.translate(event.key)
                # print(special)
                if special is None:
                    command = commands.Command(event.key)
                else:
                    command = commands.Command(special)
                print(f"{command} pressed")
                output = execute.execute(command)
            elif event.type == pygame.KEYUP:
                special = valid.translate(event.key)
                if special is None:
                    command = commands.Command(event.key)
                else:
                    command = commands.Command(special)
                print(f"{command} depressed")
                output = execute.execute(command)
            if output is not None:
                print("->" + output + "<-")


if __name__ == "__main__":
    try:
        # camera.initialize()
        run_rover()
    except KeyboardInterrupt:
        print("force quit program")



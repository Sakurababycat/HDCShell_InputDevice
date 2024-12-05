import os
import pygame


COMMON_REFIX = 'hdc shell uinput -M '
MOUSEBUTTON_MAP = {
    pygame.BUTTON_LEFT: 0,
    pygame.BUTTON_MIDDLE: 2,
    pygame.BUTTON_RIGHT: 1,
}


def handleMouseMove(x: int, y: int):
    os.system(COMMON_REFIX + f' -m {x} {y}')


def handleMouseDown(x: int, y: int, button: int):
    button = MOUSEBUTTON_MAP.get(button, 0)
    os.system(COMMON_REFIX + f' -d {button} {x} {y}')


def handleMouseUp(x: int, y: int, button: int):
    button = MOUSEBUTTON_MAP.get(button, 0)
    os.system(COMMON_REFIX + f' -u {button} {x} {y}')

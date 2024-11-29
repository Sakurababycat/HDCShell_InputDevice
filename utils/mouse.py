import os

COMMON_REFIX = 'hdc shell uinput -M '
MOUSEBUTTON_MAP = {
    1: 0,
    2: 2,
    3: 1
}


def handleMouseMove(x: int, y: int):
    os.system(COMMON_REFIX + f' -m {x} {y}')


def handleMouseDown(x: int, y: int, button: int):
    button = MOUSEBUTTON_MAP.get(button, 0)
    os.system(COMMON_REFIX + f' -d {button} {x} {y}')


def handleMouseUp(x: int, y: int, button: int):
    button = MOUSEBUTTON_MAP.get(button, 0)
    os.system(COMMON_REFIX + f' -u {button} {x} {y}')

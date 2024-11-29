import pygame
import sys
import utils.mouse as mouse
import utils.keyboard as keyboard

# 初始化 Pygame
pygame.init()

# 设置窗口大小
window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mouse and Keyboard Event Capture")

# 捕获鼠标不让鼠标离开窗口范围
pygame.event.set_grab(True)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
            if event.key == pygame.K_q:
                running = False
            keyboard.handleKeyDown(event.key)

        elif event.type == pygame.KEYUP:
            print(f"Key released: {pygame.key.name(event.key)}")
            keyboard.handleKeyUp(event.key)
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse moved to {event.pos}")
            mouse.handleMouseMove(event.pos[0], event.pos[1])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} pressed at {event.pos}")
            mouse.handleMouseDown(event.pos[0], event.pos[1], event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse button {event.button} released at {event.pos}")
            mouse.handleMouseUp(event.pos[0], event.pos[1], event.button)

    # 填充背景颜色
    screen.fill((255, 255, 255))
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()

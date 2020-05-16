import pygame

# Variables
screen_width = 1280
screen_height = 960

# Colors
back_color = (200, 200, 200)


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

while True:


    pygame.display.flip()
    clock.tick(60)
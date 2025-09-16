import pygame

# Init
pygame.init()

# Creating Screen
screen = pygame.display.set_mode((800, 600))

# Console Screen Title w/ Icon
pygame.display.set_caption("Runner")
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# Player Image
runner_image = [

]

# Player
player_image = pygame.image.load()
playerX = 0
playerY = 100

def player():
    screen.blit(player_image, (playerX, playerY))

# Starting with the game
running = True

while running:

    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
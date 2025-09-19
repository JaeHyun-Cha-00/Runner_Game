import pygame

# Init
pygame.init()

# Creating Screen
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

# Console Screen Title w/ Icon
pygame.display.set_caption("Runner")
icon = pygame.image.load("assets/img/running/fighter_run_0017.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

# Player Running Image
running_image = [
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0017.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0018.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0019.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0020.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0021.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0022.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0023.png"), 0.5),
    pygame.transform.scale_by(pygame.image.load("assets/img/running/fighter_run_0024.png"), 0.5)
]

# Player
playerX = 0
playerY = 200

# Level
level = 1
level_dist = 7200
player_speed = 2
cumulative_dist = 0

frame_index = 0

def player(img, x, y):
    screen.blit(img, (playerX, playerY))


# Starting with the game
running = True

while running:
    # Background
    screen.fill((255,255,255))

    # Land
    pygame.draw.line(screen, (0, 0, 0), (0, 390), (7200, 390), 3)

    # Exiting the Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #
    cumulative_dist += player_speed
    if cumulative_dist >= level_dist:
        running = False

    frame_index += 0.2

    if frame_index >= len(running_image):
        frame_index = 0

    current_image = running_image[int(frame_index)]

    player(current_image, playerX, playerY)

    pygame.display.update()
    clock.tick(60)
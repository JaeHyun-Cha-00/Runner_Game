import pygame
import random

# Init
pygame.init()

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

frame_index = 0

# Level
level = 1
level_dist = 7200
player_speed = 2
cumulative_dist = 0

def player(img, x, y):
    screen.blit(img, (playerX, playerY))

# Obstacles
obstacles_speed = 6
obstacles_min_gap = 300
obstacles_max_gap = 700
obstacles_width = 40
obstacles_height = 80
obstacles = []
next_obstacle_spawn = random.randint(obstacles_min_gap, obstacles_max_gap)

def spawn_obstacles():
    x = 800 + random.randint(0,200)
    y = 390 - obstacles_height
    return pygame.Rect(x, y, obstacles_width, obstacles_height)

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

    # Cumulative distanace checking
    cumulative_dist += player_speed
    if cumulative_dist >= level_dist:
        running = False

    frame_index += 0.2

    if frame_index >= len(running_image):
        frame_index = 0

    current_image = running_image[int(frame_index)]

    next_obstacle_spawn -= obstacles_speed
    if next_obstacle_spawn <= 0:
        obstacles.append(spawn_obstacles())
        next_obstacle_spawn = random.randint(obstacles_min_gap, obstacles_max_gap)

    # Create Obstacle using Loop
    for obs in obstacles[:]:
        obs.x -= obstacles_speed
        pygame.draw.rect(screen, (0, 0, 0), obs)

        if obs.right < 0:
            obstacles.remove(obs)

    # If player collides with obstacles
    player_rect = current_image.get_rect(topleft=(playerX, playerY))
    if any(player_rect.colliderect(obs) for obs in obstacles):
        print("Game Over")
        running = False

    # Create player
    player(current_image, playerX, playerY)

    pygame.display.update()
    clock.tick(60)
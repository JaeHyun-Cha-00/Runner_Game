import pygame
import random

from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y, FPS,
    LEVEL_DIST, PLAYER_X, PLAYER_SPEED,
    OBSTACLE_SPEED, OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP, OBSTACLE_WIDTH, OBSTACLE_HEIGHT,
    JUMP_HEIGHT, JUMP_GRAVITY,
)
from player import Player
from obstacle import Obstacle
from assets import running_images, jumping_images

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Runner")
icon = pygame.image.load("assets/img/running/fighter_run_0017.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

# --- Initial Player location ---
PLAYER_HEIGHT = running_images[0].get_height() # 256
player_start_y = GROUND_Y - PLAYER_HEIGHT + 66
player = Player(running_images, PLAYER_X, player_start_y, anim_speed=0.2)

# --- Obstacles ---
obstacles: list[Obstacle] = []
next_spawn = random.randint(OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP)

# --- Cumulative Distance Checking / Jumping Checking ---
cumulative_dist = 0
jumping = False
jump_v = 0

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Use Space Key to Jump
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Only jump when the player is at the floor
            on_ground = (abs(player.y - player_start_y) < 0.5)
            if on_ground and not jumping:
                jumping = True
                jump_v = JUMP_HEIGHT / 3

    # Level Complete
    cumulative_dist += PLAYER_SPEED
    if cumulative_dist >= LEVEL_DIST:
        print("Level Complete!")
        running = False

    player.update()

    # JUMPING
    if jumping:
        player.y -= jump_v
        jump_v -= JUMP_GRAVITY      # Added Gravity
        # After Jumping is done
        if player.y >= player_start_y:
            player.y = player_start_y
            jumping = False
            jump_v = 0

    # Player
    player.draw(screen)

    # Create Obstacles
    next_spawn -= OBSTACLE_SPEED
    if next_spawn <= 0:
        x = SCREEN_WIDTH + random.randint(0, 200)
        y = GROUND_Y - OBSTACLE_HEIGHT
        obstacles.append(Obstacle(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_SPEED))
        next_spawn = random.randint(OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP)

    # Obstacle movements
    player_rect = player.rect()
    for obs in obstacles[:]:
        obs.update()
        obs.draw(screen)

        if obs.off_screen():
            obstacles.remove(obs)
            continue

        if player_rect.colliderect(obs.rect):
            print("Game Over!")
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
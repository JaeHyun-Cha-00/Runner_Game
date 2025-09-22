import pygame
import random

from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y, FPS,
    LEVEL_DIST, PLAYER_SPEED,
    OBSTACLE_SPEED, OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP, OBSTACLE_WIDTH, OBSTACLE_HEIGHT
)
from player import Player
from obstacle import Obstacle
from assets import running_images

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Runner")
icon = pygame.image.load("assets/img/running/fighter_run_0017.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

player = Player(running_images)

obstacles: list[Obstacle] = []
next_spawn = random.randint(OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP)

cumulative_dist = 0
running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cumulative_dist += PLAYER_SPEED
    if cumulative_dist >= LEVEL_DIST:
        print("Level Complete!")
        running = False

    player.update()
    player.draw(screen)

    next_spawn -= OBSTACLE_SPEED
    if next_spawn <= 0:
        x = SCREEN_WIDTH + random.randint(0, 200)
        y = GROUND_Y - OBSTACLE_HEIGHT
        obstacles.append(Obstacle(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_SPEED))
        next_spawn = random.randint(OBSTACLE_MIN_GAP, OBSTACLE_MAX_GAP)

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
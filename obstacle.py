import pygame

class Obstacle:
    def __init__(self, x, y, w, h, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def off_screen(self) -> bool:
        return self.rect.right < 0
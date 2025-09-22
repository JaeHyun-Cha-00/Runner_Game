import pygame
from settings import PLAYER_X, PLAYER_Y, ANIM_SPEED

class Player:
    def __init__(self, images, x=PLAYER_X, y=PLAYER_Y):
        self.images = images
        self.x = x
        self.y = y
        self.frame_index = 0.0

    def update(self):
        self.frame_index += ANIM_SPEED
        if self.frame_index >= len(self.images):
            self.frame_index = 0.0

    def draw(self, screen):
        img = self.images[int(self.frame_index)]
        screen.blit(img, (self.x, self.y))

    def rect(self) -> pygame.Rect:
        img = self.images[int(self.frame_index)]
        return img.get_rect(topleft=(self.x, self.y))
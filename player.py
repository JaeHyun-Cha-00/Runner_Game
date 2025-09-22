import pygame

class Player:
    def __init__(self, images, x, y, anim_speed = 0.2):
        self.images = images
        self.x = x
        self.y = y
        self.frame_index = 0.0
        self.anim_speed = anim_speed

    def update(self):
        self.frame_index += self.anim_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0.0

    def draw(self, screen):
        img = self.images[int(self.frame_index)]
        screen.blit(img, (self.x, self.y))

    def rect(self) -> pygame.Rect:
        img = self.images[int(self.frame_index)]
        return img.get_rect(center=(self.x, self.y))
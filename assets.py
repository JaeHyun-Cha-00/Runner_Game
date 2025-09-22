import pygame

def load_scaled(path, scale=0.5):
    return pygame.transform.scale_by(pygame.image.load(path), scale)

running_images = [load_scaled(f"assets/img/running/fighter_run_{i:04}.png") for i in range(17,25)]
jumping_images = [load_scaled(f"assets/img/jumping/fighter_jump_{i:04}.png") for i in range(43,48)]
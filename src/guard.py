import pygame.sprite

from settings import *

class Guard(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('src','images','guard_test.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 400
        self.collision_sprites = collision_sprites


    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction


    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

        # Boundary checks
        self.rect.x = max(0, min(WINDOW_WIDTH, self.rect.x))
        self.rect.y = max(0, min(WINDOW_HEIGHT - 50, self.rect.y))


    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top

    def update(self, dt):
        self.input()
        self.move(dt)
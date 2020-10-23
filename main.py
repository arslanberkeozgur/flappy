import pygame
import random
import os

pygame.display.set_caption('Flappy')

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FLAPPY = pygame.transform.scale(pygame.image.load('flappy.png'), (64,64))
rotated_flappies = [pygame.transform.rotate(FLAPPY, i) for i in range(-70, 80, 10)]

PIPE = pygame.transform.scale(pygame.image.load('pipe.png'), (120, 700))

FPS = 60
clock = pygame.time.Clock()


class Background:
    def __init__(self, pos):
        self.position = pos
        self.img = pygame.transform.scale(pygame.image.load('background.png').convert(), (900, 800))
        self.speed = 2

    def move(self):
        self.position -= self.speed
        if self.position < -900:
            self.position = 900

    def speed_increase(self):
        self.speed += 1

    def draw(self):
        WIN.blit(self.img, (self.position, 0))


class Pipe:

    def __init__(self, x, y, flip):
        self.x = x
        self.y = y
        self._hitbox = []
        self._speed = 0
        if flip == 0:
            self.img = PIPE
        else:
            self.img = pygame.transform.flip(PIPE, False, True)

    @property
    def hitbox(self):
        self._hitbox = [[self.x, self.x + self.img.get_width()], [self.y], [self.y, self.y + self.img.get_height()]]
        return self._hitbox

    @property
    def speed(self):
        self._speed = BG1.speed
        return self._speed

    def re_move(self):
        if self.x < -120:
            pipes.remove(self)
        self.x -= self.speed

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))


class Flappy:
    def __init__(self):
        self.x = 200
        self.y = 400
        self.vy = 0
        self.ay = 0
        self._hitbox = []
        self.img = rotated_flappies

    @property
    def hitbox(self):
        self._hitbox = [[self.x, self.x + self.img.get_width()],[self.y, self.y + self.img.get_height()]]
        return self._hitbox

    def draw(self):
        WIN.blit(self.img[rotation//2], (self.x, self.y))

    def move(self):
        if not fall:
            self.ay = -0.2
            self.vy = 6
            self.vy += self.ay
            self.y -= self.vy
        if fall:
            self.ay = 0.1
            self.vy += self.ay
            self.y += self.vy




BG1 = Background(0)
BG2 = Background(900)
flappy = Flappy()
pipes = []


def main():
    run = True
    initialize = True

    global rotation
    rotation = 0
    global fall
    fall = True

    pygame.time.set_timer(pygame.USEREVENT, 10000)

    def draw():
        BG1.draw()
        BG2.draw()

        flappy.draw()

        if pipes:
            for pipe in pipes:
                pipe.draw()

        pygame.display.update()

    def pipe_generator():
        pipes.append(Pipe(WIDTH, random.randrange(300,700), 0))
        pipes.append(Pipe(WIDTH, random.randrange(pipes[len(pipes) - 1].y - 1300, pipes[len(pipes) - 1].y - 900 ), 1))

    while run:
        clock.tick(FPS)

        BG1.move()
        BG2.move()

        flappy.move( )

        if initialize:
            pipe_generator()
            initialize = False

        if pipes:
            if pipes[len(pipes) - 1].x < 240:
                pipe_generator()
            for pipe in pipes:
                pipe.re_move()

        if not fall:
            rotation += 1
            if rotation == 23:
                fall = True
        elif fall:
            if rotation > 0:
                rotation -= 1

        draw()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rotation = 0
                    fall = False
            if event.type == pygame.USEREVENT:
                BG1.speed_increase()
                BG2.speed_increase()


main()


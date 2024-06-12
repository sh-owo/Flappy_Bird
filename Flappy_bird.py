import pygame
import sys
import random

WIDTH = 600
HEIGHT = 800

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")

class Bird():
    def __init__(self):
        self.x = 30
        self.y = 30
        self.color = (255,200,0)
        self.vel = 0
        self.gravity = 0.2
        self.jump_height = -5

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x, self.y), 10)

    def update(self):
        self.vel += self.gravity
        self.y += self.vel

        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vel = 0

        if self.y < 0:
            self.y = 0
            self.vel = 0

    def jump(self):
        self.vel += self.jump_height

class Pipe():
    def __init__(self):
        self.top = random.randint(50, 550)
        self.bottom = self.top + 150
        self.x = WIDTH
        self.w = 30
        self.speed = 4
        self.color = (0,240,0)

    def draw(self):
        pygame.draw.rect(screen,self.color, (self.x, 0, self.w, self.top))
        pygame.draw.rect(screen, self.color, (self.x, self.bottom, self.w, HEIGHT - self.bottom))

    def update(self):
        self.x -= self.speed

    def outrange(self):
        return self.x < -self.w
    
def main():

    bird = Bird()
    score = 0
    pipes = []

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                bird.jump()

        bird.update()

        if len(pipes) > 0 and pipes[0].x <- pipes[0].w:
            pipes.pop(0)
            score += 1

        if len(pipes) < 5:
            if random.randint(0, 20) == 0:
                new_pipe = Pipe()
                pipes.append(new_pipe)
                if len(pipes) > 1 and pipes[-1].x - pipes[-2].x + 100 > pipes[-1].top - pipes[-1].bottom:
                    pipes.pop(-1)
        
        for pipe in pipes:
            pipe.update()

        for pipe in pipes:
            if bird.x + 10 > pipe.x and bird.x - 10 < pipe.x + pipe.w:
                if bird.y - 10 < pipe.top or bird.y + 10 >pipe.bottom:
                    running = False

        screen.fill(WHITE)

        bird.draw()

        for pipe in pipes:
            pipe.draw()

        font = pygame.font.Font(None, 20)
        text = font.render(f"Score : {score}", True, BLACK)
        screen.blit(text,(10,10))

        pygame.display.flip()
        clock.tick(60)

    font = pygame.font.Font(None, 20)
    text = font.render(f"Score : {score}", True, BLACK)
    screen.blit(text,(WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

if __name__ =='__main__':
    main()

pygame.quit()
sys.exit()
    

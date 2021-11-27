from pygame import *
from pygame.sprite import spritecollide

font.init()
font1 = font.SysFont("Arial", 35)
lose1 = font1.render("Игрок 1 слит", True, (180, 0, 0))
lose2 = font1.render("Игрок 2 слит", True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 660:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 660:
            self.rect.y += self.speed


player_1 = Player_1("sword.png", 1, 540, 120, 400, 15)
player_2 = Player_2("sword.png", 1800, 540, 120, 400, 15) 
ball = GameSprite("ball.png", 500, 400, 120, 400, 15)


window = display.set_mode((1920,1050))
display.set_caption("Ping Pong")
background = transform.scale(image.load("windows-xp.jpg"), (1920,1050))

clock = time.Clock()
FPS = 60

game = True
finish = False

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background,(0,0))

        player_1.update()
        player_1.reset()

        player_2.update()
        player_2.reset()

        ball.update()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 1000 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
        speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    
    if ball.rect.x > 1870:
        finish = True
        window.blit(lose2, (200, 200))    



        clock.tick(FPS)
    display.update()
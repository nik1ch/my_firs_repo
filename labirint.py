from pygame import *
 
win_width = 1280
win_height = 720
display.set_caption("Лабиринт")
window = display.set_mode((1280, 720))
background = transform.scale(image.load('way_4.png'), (1280, 720))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0 
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)
 
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
 
    def update(self):
        if self.rect.x <= 420:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()
 
 
barriers = sprite.Group()
 
bullets = sprite.Group()
 
monsters = sprite.Group()
 
# 1 - направо налево, 2 - вверх вниз, чем больше тем ниже, 3 - ширина, 4 - высота

w1 = GameSprite('wall.jpg', 300, 150, 25, 600)
w2 = GameSprite('wall.jpg', 100, 150, 200, 25)
w3 = GameSprite('wall.jpg', 100, 400, 200, 25)
w4 = GameSprite('wall.jpg', 0, 550, 200, 25)
w5 = GameSprite('wall.jpg', 0, 270, 200, 25)
w6 = GameSprite('wall.jpg', 500, 0, 25, 250)
w7 = GameSprite('wall.jpg', 500, 370, 25, 220)
w8 = GameSprite('wall.jpg', 500, 370, 200, 25)
w9 = GameSprite('wall.jpg', 500, 570, 200, 25)
w10 = GameSprite('wall.jpg', 675, 170, 25, 200)
w11 = GameSprite('wall.jpg', 675, 570, 25, 200)
w12 = GameSprite('wall.jpg', 675, 150, 450, 25)
w13 = GameSprite('wall.jpg', 1100, 170, 25, 400)
w14 = GameSprite('wall.jpg', 675, 290, 320, 25)
w15 = GameSprite('wall.jpg', 970, 300, 25, 270)
w16 = GameSprite('wall.jpg', 800, 570, 195, 25)
w17 = GameSprite('wall.jpg', 780, 445, 25, 150)


barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)



# 1 - направо налево, 2 - вверх вниз, чем больше тем ниже, 3 - ширина, 4 - высота

packman = Player('hero.png', 10, win_height - 80, 80, 80, 0, 0)
final_sprite = GameSprite('pac-1.png', win_width - 450, win_height - 270, 100, 100)


monster1 = Enemy('cyborg.png', 200, 310, 80, 80, 0)
monster2 = Enemy('cyborg.png', 200, 50, 80, 80, 0)
monster3 = Enemy('cyborg.png', 550, 630, 80, 80, 0)
monster4 = Enemy('cyborg.png', 500, 630, 80, 80, 0)
monster5 = Enemy('cyborg.png', 450, 630, 80, 80, 0)
monster6 = Enemy('cyborg.png', 400, 630, 80, 80, 0)
monster7 = Enemy('cyborg.png', 350, 630, 80, 80, 0)
monster8 = Enemy('cyborg.png', 550, 280, 80, 80, 0)
monster9 = Enemy('cyborg.png', 700, 70, 80, 80, 0)
monster10 = Enemy('cyborg.png', 750, 70, 80, 80, 0)
monster11 = Enemy('cyborg.png', 800, 70, 80, 80, 0)
monster12 = Enemy('cyborg.png', 850, 70, 80, 80, 0)
monster13 = Enemy('cyborg.png', 900, 70, 80, 80, 0)
monster14 = Enemy('cyborg.png', 950, 70, 80, 80, 0)
monster15 = Enemy('cyborg.png', 1000, 70, 80, 80, 0)
monster16 = Enemy('cyborg.png', 1050, 70, 80, 80, 0)
monster17 = Enemy('cyborg.png', 700, 210, 80, 80, 0)
monster18 = Enemy('cyborg.png', 750, 210, 80, 80, 0)
monster19 = Enemy('cyborg.png', 800, 210, 80, 80, 0)
monster20 = Enemy('cyborg.png', 850, 210, 80, 80, 0)
monster21 = Enemy('cyborg.png', 900, 210, 80, 80, 0)
monster22 = Enemy('cyborg.png', 550, 480, 80, 80, 0)
monster23 = Enemy('cyborg.png', 600, 480, 80, 80, 0)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)
monsters.add(monster7)
monsters.add(monster8)
monsters.add(monster9)
monsters.add(monster10)
monsters.add(monster11)
monsters.add(monster12)
monsters.add(monster13)
monsters.add(monster14)
monsters.add(monster15)
monsters.add(monster16)
monsters.add(monster17)
monsters.add(monster18)
monsters.add(monster19)
monsters.add(monster20)
monsters.add(monster21)
monsters.add(monster22)
monsters.add(monster23)


finish = False

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0

    if not finish:
        window.blit(background,(0,0))

        packman.update()
        bullets.update()
        packman.reset()
        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()

        if not(sprite.groupcollide(monsters, bullets, True, True)):
            monsters.update()
            monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)

        if sprite.spritecollide(packman, monsters, False):
            finish = True
            img = image.load('game_over.jpg')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window = display.set_mode((win_width, win_height))
            back = (0, 0, 0)
            window.blit(transform.scale(img, (win_height * d, win_height)), (250, 40))

        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = image.load('cool.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    display.update()

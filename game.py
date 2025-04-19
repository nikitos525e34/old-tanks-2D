from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("гра у квача")
bg = transform.scale(image.load("1-56.jpg"),(win_width, win_height))

x1 = 100
y1 = 300

x2 = 300
y2 = 300


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, heidth, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, heidth))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# нові класи-спадкоємці
class Player(GameSprite):
    def update(self, key_up, key_down, key_left, key_right):
        keys = key.get_pressed()
        if keys[key_left]:
            self.rect.x -= self.speed
        if keys[key_right]:
            self.rect.x += self.speed
        if keys[key_up]:
            self.rect.y -= self.speed
        if keys[key_down]:
            self.rect.y += self.speed



sprite1 = Player("T64_5.gif", 100, 100, 120, 50, 5)
sprite2 = Player("tank2.png", 200, 100, 120, 50, 5)

run = True
clock = time.Clock()
FPS = 60
speed = 5

while run:
    window.blit(bg, (0, 0))
    sprite1.reset()
    sprite2.reset()

    sprite1.update(K_UP, K_DOWN, K_LEFT, K_RIGHT)
    sprite2.update(K_w, K_s, K_a, K_d)

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
from pygame import *
win_width = 900
win_height = 700
wall_size = 50
window = display.set_mode((win_width, win_height))
display.set_caption("гра у квача")
bg = transform.scale(image.load("1-56.jpg"), (win_width, win_height))

x1 = 50
y1 = 100

x2 = win_width - 150
y2 = win_height - 100


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


class Wall(GameSprite):
    def __init__(self, wall_img, player_x, player_y):
        super().__init__(wall_img, player_x, player_y, wall_size, wall_size, 0)

    def stop_tank(self):
        pass


class StoneWall(Wall):
    def __init__(self, player_x, player_y):
        super().__init__("stone-wall.jpg", player_x, player_y)


class BrickWall(Wall):
    def __init__(self, player_x, player_y):
        super().__init__("brick-wall.png", player_x, player_y)


sprite1 = Player("T64_5.gif", x1, y1, 120, 50, 5)
sprite2 = Player("tank2.png", x2, y2, 120, 50, 5)

# код для створення стінок
# створення рамки
stone_walls = sprite.Group()
width_stone_walls = win_width // wall_size
height_stone_walls = win_height // wall_size

x = 0
y = 0
for i in range(width_stone_walls):
    stone_wall = StoneWall(x, y)
    stone_walls.add(stone_wall)
    x += wall_size

x = 0
y = win_height - wall_size
for i in range(width_stone_walls):
    stone_wall = StoneWall(x, y)
    stone_walls.add(stone_wall)
    x += wall_size

x = 0
y = 0
for i in range(width_stone_walls):
    stone_wall = StoneWall(x, y)
    stone_walls.add(stone_wall)
    y += wall_size

x = win_width - wall_size
y = 0
for i in range(width_stone_walls):
    stone_wall = StoneWall(x, y)
    stone_walls.add(stone_wall)
    y += wall_size

# створення рандомних кам'яних стін перешкод
stone_wall = StoneWall(350, 150)
stone_walls.add(stone_wall)


# створення цегляних перешкод
brick_walls = sprite.Group()
brick_wall = BrickWall(50, 150)
brick_walls.add(brick_wall)
brick_wall = BrickWall(100, 150)
brick_walls.add(brick_wall)
brick_wall = BrickWall(150, 150)
brick_walls.add(brick_wall)
brick_wall = BrickWall(200, 150)
brick_walls.add(brick_wall)

x



run = True
clock = time.Clock()
FPS = 60
speed = 5

while run:
    window.blit(bg, (0, 0))
    sprite1.reset()
    sprite2.reset()

    sprite1.update(K_w, K_s, K_a, K_d)
    sprite2.update(K_UP, K_DOWN, K_LEFT, K_RIGHT)

    stone_walls.draw(window)
    brick_walls.draw(window)

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
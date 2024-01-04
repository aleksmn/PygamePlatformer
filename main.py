import pygame as pg
import pytmx

pg.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 670
FPS = 80
TILE_SCALE = 3

class Platform(pg.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()

        self.image = pg.transform.scale(image, (width * TILE_SCALE, height * TILE_SCALE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SCALE
        self.rect.y = y * TILE_SCALE


class Player(pg.sprite.Sprite):
    def __init__(self, map_width, map_height):
        super(Player, self).__init__()

        self.image = pg.Surface((50, 50))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.center = (200, 100)  # Начальное положение персонажа

        # Начальная скорость и гравитация
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 2
        self.is_jumping = False
        self.map_width = map_width * TILE_SCALE
        self.map_height = map_height * TILE_SCALE

    def update(self, platforms):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and not self.is_jumping:
            self.jump()

        if keys[pg.K_a]:
            self.velocity_x = -10
        elif keys[pg.K_d]:
            self.velocity_x = 10
        else:
            self.velocity_x = 0

        new_x = self.rect.x + self.velocity_x
        if 0 <= new_x <= self.map_width - self.rect.width:
            self.rect.x = new_x

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # for platform in platforms:

        #     if platform.rect.collidepoint(self.rect.с):
        #         self.rect.bottom = platform.rect.top
        #         self.velocity_y = 0
        #         self.is_jumping = False

        #     if platform.rect.collidepoint(self.rect.midtop):
        #         self.rect.top = platform.rect.bottom
        #         self.velocity_y = 0

        #     if platform.rect.collidepoint(self.rect.midright):
        #         self.rect.right = platform.rect.left

        #     if platform.rect.collidepoint(self.rect.midleft):
        #         self.rect.left = platform.rect.right

    # def jump(self):
    #     self.velocity_y = -45
    #     self.is_jumping = True

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Платформер")
        self.clock = pg.time.Clock()
        self.is_running = False

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.tmx_map = pytmx.load_pygame("maps/level-1.tmx")

        self.map_pixel_width = self.tmx_map.width * self.tmx_map.tilewidth * TILE_SCALE
        self.map_pixel_height = self.tmx_map.height * self.tmx_map.tileheight * TILE_SCALE

        self.player = Player(self.map_pixel_width, self.map_pixel_height)
        self.all_sprites.add(self.player)

        for layer in self.tmx_map:
            for x, y, gid in layer:
                tile = self.tmx_map.get_tile_image_by_gid(gid)

                if tile:
                    # self.screen.blit(tile, (x * self.tmx_map.tilewidth, y * self.tmx_map.tileheight))
                    platform = Platform(tile, x * self.tmx_map.tilewidth, y * self.tmx_map.tileheight,
                                        self.tmx_map.tilewidth, self.tmx_map.tileheight)

                    self.all_sprites.add(platform)
                    self.platforms.add(platform)

        self.run()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(60)
        pg.quit()
        quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

    def update(self):
        self.player.update(self.platforms)

        self.camera_x = self.player.rect.x - SCREEN_WIDTH // 2
        self.camera_y = self.player.rect.y - SCREEN_HEIGHT // 2

        self.camera_x = max(0, min(self.camera_x, self.map_pixel_width - SCREEN_WIDTH))
        self.camera_y = max(0, min(self.camera_y, self.map_pixel_height - SCREEN_HEIGHT))


    def draw(self):
        self.screen.fill("light blue")
        
        self.all_sprites.draw(self.screen)

        pg.display.flip()


if __name__ == "__main__":
    game = Game()
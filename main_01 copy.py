import json

import pygame as pg
import pytmx

pg.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 80
TILE_SCALE = 1.5

font = pg.font.Font(None, 36)


class Platform(pg.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()

        self.image = pg.transform.scale(image, (width * TILE_SCALE, height * TILE_SCALE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SCALE
        self.rect.y = y * TILE_SCALE



class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Платформер")
        self.level = 1

        self.setup()


    def setup(self):
        self.collected_coins = 0
        self.mode = "game"
        self.clock = pg.time.Clock()
        self.is_running = False

        self.background = pg.image.load("background.png")

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.tmx_map = pytmx.load_pygame("maps/level1.tmx")

        for layer in self.tmx_map:
            if layer.name == "platforms":
                for x, y, gid in layer:
                    tile = self.tmx_map.get_tile_image_by_gid(gid)
                    
                    if tile:
                        platform = Platform(tile, 
                                            x * self.tmx_map.tilewidth, 
                                            y * self.tmx_map.tileheight, 
                                            self.tmx_map.tilewidth, 
                                            self.tmx_map.tileheight)
                        
                        self.all_sprites.add(platform)
                        self.platforms.add(platform)

        self.run()


    def run(self):
        self.is_running = True
        while self.is_running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            pg.display.flip()
        pg.quit()
        quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

    def update(self):
        ...

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.all_sprites.draw(self.screen)




if __name__ == "__main__":
    game = Game()
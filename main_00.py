import json

import pygame as pg
import pytmx

pg.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 80
TILE_SCALE = 1.5

font = pg.font.Font(None, 36)


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
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))


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
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))



        


if __name__ == "__main__":
    game = Game()

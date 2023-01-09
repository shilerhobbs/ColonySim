
import sys

import pygame as pg
import pytmx
import pyscroll


def update(dt):

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def draw(screen):

    screen.fill((0, 0, 0))

    pg.display.flip()



def runGame():

    pg.init()

    fps = 60.0
    fpsClock = pg.time.Clock()


    width, height = 640, 480
    screen = pg.display.set_mode((width, height))


    #Main Loop
    dt = 1 / fps
    while True:
        update(dt)
        draw(screen)

        dt = fpsClock.tick(fps)



runGame()
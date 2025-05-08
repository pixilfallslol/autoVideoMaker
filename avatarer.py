import pygame
import os
import math
import random
import argparse

W_W = 1280
W_H = 720
clock = pygame.time.Clock()
FPS = 60
startingWidth = 510
startingHeight = 520
endingWidth = 590
endingHeight = 600
scriptAudioFile = "script.wav"
st = pygame.time.get_ticks()
TIME_BEFORE_NEXT_IMAGE = 5
newImg = False

parser = argparse.ArgumentParser()
params = ["-music","--songFile"]
parser.add_argument(params[0],params[1],type=str)
args = parser.parse_args()
musPath = args.songFile

pygame.init()
screen = pygame.display.set_mode((W_W,W_H))

fontTiny = pygame.font.SysFont("Comic sans MS", 18)
fontSmall = pygame.font.SysFont("Comic sans MS", 23)
font18 = pygame.font.SysFont("Comic sans MS", 19)
font36 = pygame.font.SysFont("Comic sans MS", 38)

playMusic = True

song = pygame.mixer.Sound(musPath)
script = pygame.mixer.Sound(scriptAudioFile)
song.set_volume(0.2)
script.set_volume(1.0)

def drawPixil():
    print("STARTED")
    pixilImgs = ["imgs/smile","imgs/thumbs","imgs/suprised","imgs/scream"]
    pixilImgsLoaded = pygame.image.load(pixilImgs[0]+".png")
    ct = pygame.time.get_ticks()
    dur = 1000
    t = (ct-st)/dur
    t = max(0,min(t,1))
    w = cosInterExtreme(startingWidth,endingWidth,t)
    h = cosInterExtreme(startingHeight,endingHeight,t)
    if newImg:
        w = cosInterExtreme(startingWidth,endingWidth,t)
        h = cosInterExtreme(startingHeight,endingHeight,t)
    pixilImgsLoaded = pygame.transform.scale(pixilImgsLoaded,(int(w),int(h)))
    screen.blit(pixilImgsLoaded,(W_W//2,W_H//5))

def playSounds():
    script.play()
    song.play()
    
def cosInterExtreme(a,b,x):
    x2 = 1
    if x < 0.2:
        x2 = 0
    elif x >= 0.2 and x < 0.8:
        prog = (x-0.2)/0.6
        x2 = 0.5-0.5*math.cos(prog*math.pi)
    else:
        x2 = 1
    return a+(b-a)*x2

running = True
playSounds()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")
    drawPixil()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
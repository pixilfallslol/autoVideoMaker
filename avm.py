import pygame
import numpy as np
import ffmpeg
import os

pygame.init()

W_W = 640
W_H = 360

screen = pygame.display.set_mode((W_W, W_H))
clock = pygame.time.Clock()

PIXIL_IMAGE = pygame.image.load("PixilYap.png")
font = pygame.font.Font("comic.ttf", 36)

captions = [
    "If the captions are showing.",
    "Then this project is working like wonders.",
    "Well if the captions arent showing.",
    "Thats a problem."
    "Although a simple fix."
    "I would prefer that this work on the first try."
]

def drawBackground(screen, tileSize):
    screenWidth, screenHeight = screen.get_size()
    cols = screenWidth // tileSize + 2
    rows = screenHeight // tileSize
    for row in range(rows):
        for col in range(cols):
            color = (0, 0, 255) if (row + col) % 2 == 0 else (0, 0, 0)
            x = col * tileSize
            y = row * tileSize
            pygame.draw.rect(screen, color, (x, y, tileSize, tileSize))

def cosineInterpolation(start, end, t):
    return start + (end - start) * (1 - np.cos(t * np.pi)) / 2

def renderFrame(frameNumber, totalFrames, tileSize):
    screen.fill((0, 0, 0))
    drawBackground(screen, tileSize)
    
    t = (frameNumber / totalFrames) * 2
    t = t - np.floor(t)
    
    startY = W_H / 2 + 100 - PIXIL_IMAGE.get_height() / 2
    endY = W_H / 2 + 80 - PIXIL_IMAGE.get_height() / 2
    y = cosineInterpolation(startY, endY, t) if t < 0.5 else cosineInterpolation(endY, startY, t - 0.5)

    x = W_W / 2 - PIXIL_IMAGE.get_width() / 2
    screen.blit(PIXIL_IMAGE, (int(x), int(y)))

    captionIndex = (frameNumber // (totalFrames // len(captions))) if captions else 0
    if captionIndex < len(captions):
        captionText = captions[captionIndex]
        textSurface = font.render(captionText, True, (255, 255, 255))
        box_width = textSurface.get_width() + 40
        box_height = textSurface.get_height() + 20
        pygame.draw.rect(screen, (100, 100, 100), (20, W_H - 60, box_width, box_height))
        screen.blit(textSurface, (40, W_H - 50))

    pygame.image.save(screen, f"output/frame_{frameNumber:04d}.png")
    pygame.display.flip()

def exportVideo():
    ffmpeg.input('output/frame_%04d.png', framerate=60).output('output_video.mp4').run()

def main():
    os.makedirs('output', exist_ok=True)
    totalFrames = len(captions) * 60
    tileSize = 50
    for frameNumber in range(totalFrames):
        renderFrame(frameNumber, totalFrames, tileSize)
        clock.tick(60)
    exportVideo()
    pygame.quit()

if __name__ == "__main__":
    main()

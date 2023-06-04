import pygame
import os

#Initialiser
pygame.init()
pygame.mixer.init()

#Fenster Settings
FPS = 60
SCREEN_WIDTH= 1400
SCREEN_HEIGHT= 900

pygame.display.set_caption("Parachute Game")
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

#Background Bild
game_pictures= os.path.dirname(__file__)
background= pygame.image.load(os.path.join( game_pictures,'game_pictures/backgroundColorForest.png' ))
image_background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))

#music
pygame.mixer.init()

background_music= pygame.mixer.music.load("music/POL-net-bots-short.wav")
pygame.mixer.music.play(-1)
#Lautstärke 
pygame.mixer.music.set_volume(0)

# Colors & Fonts
white = (255, 255, 255)
RED= 255,0,0
BLACK = 0,0,0
GRAU= 92, 82, 82
Light_GREY= 194, 186, 186
font = pygame.font.SysFont("hipssthetic", 24)

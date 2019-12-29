import pygame
import os
from playlist import playlist
import random
pygame.init()
speed = 2
screen_width = 600
screen_height = 600
letter_size = screen_width/8
# min_prime = letter_size/speed + 20
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(109, 209, 222)
BLACK = pygame.Color(0,  0,  0)
RED = pygame.Color(255, 0, 0)
GOLD = pygame.Color(255,215,0)
score = -1
GREEN = pygame.Color(0, 255, 0)
GRAY = pygame.Color(100, 100, 100)

C_MENU = pygame.Color(54, 57, 63)
marge = 20

limit = 300
perfectlimit = 400
deadlimit = 500
delta = 0

bool_a = False
w_x = 500

font = pygame.font.SysFont("Times New Roman, Arial", 50)
TxMenu = font.render("MENU", True, WHITE)
Txspace = font.render("[PRESS ESPACE]", True, WHITE)
size_menu = 100
menu_x = screen_width / 2 - size_menu/2 + ((size_menu - TxMenu.get_rect().width) / 2)
menu_y = (size_menu - TxMenu.get_rect().height) / 2
posMenu = (menu_x, menu_y)
dif =Txspace.get_rect().width - TxMenu.get_rect().width
pospace = (menu_x - dif/2, menu_y + 200)

music = pygame.mixer.music

music.set_volume(0.2)
music_start = True
bulleSound = pygame.mixer.Sound("bruitage/bulle.wav")
whouv = pygame.mixer.Sound("bruitage/whouv.wav")
soundError = pygame.mixer.Sound("bruitage/error.wav")
perfSound = pygame.mixer.Sound("bruitage/perfSound.wav")
bulleSound.set_volume(0.6)
soundError.set_volume(0.04)
perfSound.set_volume(0.5)

w_y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (w_x, w_y)
screen = pygame.display.set_mode([screen_width, screen_height])


clock = pygame.time.Clock()
end = False
c_color = BLACK

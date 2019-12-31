import pygame
import os
from playlist import playlist
from color import *
import random
pygame.init()
speed = 2
screen_width = 600
screen_height = 600
letter_size = screen_width/8
# min_prime = letter_size/speed + 20
marge = 20
score = -1
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

music.set_volume(0.4)
music_start = True
bulleSound = pygame.mixer.Sound("bruitage/bulle.wav")
whouv = pygame.mixer.Sound("bruitage/whouv.wav")
soundError = pygame.mixer.Sound("bruitage/error.wav")
perfSound = pygame.mixer.Sound("bruitage/perfSound.wav")
bulleSound.set_volume(0.6)
soundError.set_volume(0.04)
perfSound.set_volume(0.8)

w_y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (w_x, w_y)
screen = pygame.display.set_mode([screen_width, screen_height])


clock = pygame.time.Clock()
end = False
c_color = BLACK

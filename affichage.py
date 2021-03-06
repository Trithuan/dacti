from settings import *
from threading import Timer
import pygame

def clear(color):
	pygame.draw.rect(screen, color, (0, 0, screen_width/2, screen_height))
	r = (color.r + 25) % 255
	g = (color.g + 25) % 255
	b = (color.b + 25) % 255
	color2 = pygame.Color(r,g,b)
	pygame.draw.rect(screen, color2, (screen_width/2, 0, screen_width/2, screen_height))
	

def drawlines(height, color):
	pygame.draw.line(screen, color, (0, height), (screen_width, height))

def drawrect(height, large, color):
	pygame.draw.rect(screen, color, (0, height- large/2, screen_width, large))


def displaycol(game):
	for col in game.col:
		pygame.draw.rect(screen, GRAY, (col*letter_size, 0, letter_size, screen_height))


def displayscore(ThisGame):
	txScore = font.render("score : "+str(ThisGame.score), True, WHITE)
	screen.blit(txScore, (10, screen_height - txScore.get_rect().height))


def bg_black(ThisGame):
	bgblaked = Timer(1, ThisGame.black, args = (BLACK,))
	bgblaked.start()


def displaylives(ThisGame):
	rad = 20
	for x in range(ThisGame.life):
		pygame.draw.circle(screen, GREEN, (int(x*rad*3 + 30), int(rad + 20)), rad)
def displayletter(ThisGame):
	for fLetter in ThisGame.lettre_list:
		pygame.draw.rect(screen, fLetter.color, (fLetter.x, fLetter.y, fLetter.width, fLetter.height))
		lettre = font.render(fLetter.key, True, BLACK)
		f_x = fLetter.x + (fLetter.width - lettre.get_rect().width)/2
		f_y = fLetter.y + (fLetter.height - lettre.get_rect().height)/2
		fpos = (f_x, f_y)
		screen.blit(lettre, fpos)


def display(ThisGame):
	displaycol(ThisGame)
	drawlines(limit, RED)
	drawlines(deadlimit, RED)
	drawrect(perfectlimit, ThisGame.marge, GOLD)
	displayletter(ThisGame)
	displaylives(ThisGame)
	displayscore(ThisGame)
import pygame
import sys
from keyboard import Keyboard, alphabet
from keyboard import stoped


def k_event():
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.unicode == " ":
                stoped.append(True)
            for alpha in alphabet:
                if events.key == alphabet[alpha]:
                    Keyboard[alpha] = True
        elif events.type == pygame.KEYUP:
            for alpha in alphabet:
                if events.key == alphabet[alpha]:
                    Keyboard[alpha] = False


def stop_event():
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.unicode == " ":
                return True
            else:
                return False
    return False


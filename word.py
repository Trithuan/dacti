import random
from keyboard import *
from fallingKey import FallingKey
import codecs

with codecs.open('data.txt', 'r', encoding='utf8') as f:
    word_list = f.read().split()
def pop_key(game, w, h, finger):
	# TODO: mot aparrait prédéfinis comme partition
	# TODO: charger partition depuis mémoire
	# TODO: enlever les globaux
	if game.new_mot:
		game.mot = random.choice(word_list)
		game.new_mot = False
		game.numlettre = 0
	delay = random.random()
	if len(game.lettre_list) < 20 and delay < 0.1 and game.delay_min < 0:
		# #alpha = random.choice(keys)
		# index_finger = random.randint(0, 7)
		# index_letter = random.randint(0, len(finger[index_finger]) - 1)
		# alpha = finger[index_finger][index_letter]
		alpha = game.mot[game.numlettre]
		buf_lettre = FallingKey(alpha, game.key_col, w, h, game.speed)
		game.numlettre += 1
		if game.numlettre >= len(game.mot):
			game.new_mot = True
			print(" ")
		for lettre in game.lettre_list:
			if lettre.key == buf_lettre.key:
				buf_lettre.first = False
		game.lettre_list.append(buf_lettre)
		game.delay_min = game.frequence
	else:
		if game.numlettre == 0:
			game.delay_min -= 0.7
		else:
			game.delay_min -= 2
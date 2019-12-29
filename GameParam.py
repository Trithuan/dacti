from keyboard import finger
from fallingKey import FallingKey
from keyboard import Keyboard
import random
from threading import Timer


def get_finger(a):
	for x in range(len(finger)):
		for y in range(len(finger[x])):
			if finger[x][y] == a:
				return x
	return -1


class GameParam:
	def __init__(self, bgcolor, key_col, lettersize, marge, speed):
		self.bgcolor = bgcolor
		self.clickable = []
		self.letter_size = lettersize
		self.key_col = key_col
		self.switch = True
		self.lettre_list = []
		self.t_count = 0
		self.count = 0
		self.speed = speed
		self.lettersize = lettersize
		self.frequence = self.lettersize/self.speed + 20
		self.score = 0
		self.miss = False
		self.music_start = False
		self.pause = False
		self.menu = True
		self.end = False
		self.life = 3
		self.col = []
		self.delay_min = self.frequence
		self.marge = marge
		self.canclick = True
		self.hold = False

	def offlimit(self, key, red, green, gold, limit, deadlimit, perfmilit, sound1, sound2):
		marge = 20
		# TODO: validation animation disparaitre rapide
		# TODO: marge d'erreur et perfect timing
		if limit - key.height < key.y < deadlimit:
			if key.clicked:
				if key.perfect:
					key.color = gold
				else:
					key.color = green
			else:
				key.color = red
			if key.nosibling and not key.clicked:
				key.mustclick = True
			else:
				key.mustclick = False
			if self.canclick:
				self.checkclick(key, sound1, sound2, perfmilit, gold)
			if not key.clickable:
				self.clickable.append(key)
				key.clickable = True

		else:
			key.mustclick = False
			if key in self.clickable:
				self.clickable.remove(key)

		if key.y > deadlimit:
			self.lettre_list.remove(key)
			for lettre in self.lettre_list:
				if key.key == lettre.key:
					lettre.first = True
					break

	def enableclick(self):
		self.canclick = True

	def waitclick(self):
		wait = Timer(1, self.enableclick)
		wait.start()

	def checkclick(self,letter, sound1, sound2, perfmilit, gold):
		marge = 10
		if Keyboard[letter.key]:
			if letter.unused and letter.first:
				if not letter.clicked:
					if perfmilit - marge < letter.y + letter.height/2 < perfmilit + marge:
						sound1.play()
						self.score += 2
						letter.perfect = True
					else:
						sound2.play()
						self.score += 1
					letter.clicked = True
					letter.mustclick = False
					letter.unused = False
					for lettre in self.lettre_list:
						if lettre.key == letter.key and not lettre.first:
							lettre.first = True
							letter.first = False
							lettre.unused =  False
							break
					self.waitclick()
				elif not letter.lost:
					self.miss = True
					letter.lost = True
				delta = 0
		else:
			for lettre in self.lettre_list:
				if lettre.key == letter.key:
					lettre.unused = True

	def checkmiss(self, key, deadlimit):
		if key.y > deadlimit and not key.clicked:
			self.count += 1
			# print(count,"t'es nul")
			self.miss = True

	def black(self, color):
		self.bgcolor = color

	def accel(self, sound):
		self.t_count += 1
		if self.t_count > 1200:
			sound.play()
			self.speed += 0.2
			self.frequence = self.letter_size/self.speed + 20
			self.t_count = 0
			print("speed : ", self.speed)
			return True
		else:
			return False

	def bgmusic(self, music, stoped):
		if len(stoped):
			if stoped[0] and not self.menu:
				music.fadeout(1000)

	def pop_key(self, w, h):
		# TODO: mot aparrait prédéfinis comme partition
		# TODO: charger partition depuis mémoire
		# TODO: enlever les globaux
		delay = random.random()
		if len(self.lettre_list) < 20 and delay < 0.1 and self.delay_min < 0:
			# alpha = random.choice(keys)
			index_finger = random.randint(0, 7)
			index_letter = random.randint(0, len(finger[index_finger]) - 1)
			alpha = finger[index_finger][index_letter]
			buf_lettre = FallingKey(alpha, self.key_col, w, h, self.speed)
			for lettre in self.lettre_list:
				if lettre.key == buf_lettre.key:
					buf_lettre.first = False
			self.lettre_list.append(buf_lettre)
			self.delay_min = self.frequence
		else:
			self.delay_min -= 1

	def col_light(self):
		self.col = []
		for alpha in Keyboard:
			wellclicked = False
			if Keyboard[alpha]:
				for letter in self.clickable:
					if letter.key == alpha:
						wellclicked = True
						break
					else:
						wellclicked = False
				if not wellclicked and not self.hold:
					self.miss = True
					self.hold = True
					self.waitwell()
				self.col.append(get_finger(alpha))

	def waitwell(self):
		wait = Timer(1, self.unhold)
		wait.start()

	def unhold(self):
		self.hold = False

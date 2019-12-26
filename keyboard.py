Keyboard = {}
finger = []
alphabet = {'a': 113, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 59, 'n': 110, 'o': 111, 'p': 112, 'q': 97, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 122, 'x': 120, 'y': 121, 'z': 119, 'ç': 57, 'à': 48, 'è': 55}
keys = list(alphabet.keys())
stoped = []
finger.append(['a', 'q', 'w'])
finger.append(['z', 's', 'x'])
finger.append(['e', 'd', 'c'])
finger.append(['r', 'f', 'v', 't', 'g', 'b'])
finger.append(['y', 'h', 'n', 'u', 'j', 'è'])
finger.append(['i', 'k'])
finger.append(['o', 'l', 'ç'])
finger.append(['p', 'm', 'à'])
# finger.append(['a'])
# finger.append(['z'])
# finger.append(['e'])
# finger.append(['r'])
# finger.append(['u'])
# finger.append(['i'])
# finger.append(['o'])
# finger.append(['p'])
for alpha in alphabet:
    Keyboard[alpha] = False


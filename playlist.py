from os import walk

playlist = []
for (dirpath, dirnames, filenames) in walk('music'):
	playlist.extend(filenames)
	break
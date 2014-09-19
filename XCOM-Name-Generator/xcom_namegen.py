import random
import sys

# Setting this to True puts every name in every country rather than randomly sorting them
MIRROR = False

# Xcom countries (you probably shouldn't edit this)
COUNTRIES = ['Am', 'Rs', 'Ch', 'In', 'Af', 'Mx', 'Ab', 'En', 'Fr', 'Gm', 'Au', 'It', 'Jp', 'Is', 'Es', 'Gr', 'Nw', 'Ir', 'Sk', 'Du', 'Sc', 'Bg']

def main():
	global MIRROR, COUNTRIES
	# Figure out name files
	input_file = 'names.txt'
	output_file = 'XComNameList.ini'
	if len(sys.argv) > 1:
		input_file = sys.argv[1]
	if len(sys.argv) > 2:
		output_file = sys.argv[2]
	# Parse input file and randomize
	lines = [line.strip() for line in open(input_file)]
	random.shuffle(lines)
	# Sort names into countries
	names = {}
	for c in COUNTRIES:
		names[c] = []
	for i, l in enumerate(lines):
		if l.strip():
			if MIRROR:
				for c in COUNTRIES:
					names[c].append(l.strip())
			else:
				names[COUNTRIES[i % len(COUNTRIES)]].append(l.strip())
	# Output to ini file
	f = open(output_file, 'w')
	f.write('[XComGame.XGCharacterGenerator]\r\n')
	for c in COUNTRIES:
		f.write('m_arr' + c + 'MFirstNames=\r\n')
		f.write('m_arr' + c + 'FFirstNames=\r\n')
		random.shuffle(names[c])
		for n in names[c]:
			f.write('m_arr' + c + 'LastNames=' + n + '\r\n')
	f.write('\r\n[IniVersion]\r\n0=1367645963.000000\r\n\r\n')
	return 0

if __name__ == '__main__':
	status = main()
	sys.exit(status)
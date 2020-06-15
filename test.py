from os import listdir
import numpy as np
import sys, os

# reading user input file
user_input = sys.argv[1]
list = []
fp = open(user_input, 'r')
for line in fp.readlines():
	clean = line.decode('iso-8859-14').encode('utf8').strip('\n')
	list.append(clean)

calc = open('calc.txt').read().split('+++')

normal_prob_dict = {}
normal_tmp = calc[0].split(',,,')
normal_tmp.remove('')
for line in normal_tmp:
	y = line.split(':::')
	normal_prob_dict[y[0]] = y[1]

mal_prob_dict = {}
mal_tmp = calc[1].split(',,,')
mal_tmp.remove('')
for line in mal_tmp:
        y = line.split(':::')
        mal_prob_dict[y[0]] = y[1]

normal_class_prob = float(calc[2].split(':::')[0])
mal_class_prob = float(calc[2].split(':::')[1])
normal_total_words = float(calc[2].split(':::')[2])
mal_total_words = float(calc[2].split(':::')[3])
uniq_words = float(calc[2].split(':::')[4])

no_normal = 0.0
no_mal = 0.0
for line in list:
	elements = line.split(',,11,,')
	elements.remove('')

	normal_like = normal_class_prob
	for element in elements:
		if element in normal_prob_dict:
			normal_like *= float(normal_prob_dict[element])
		else:
			normal_like *= (1.0) / (normal_total_words + uniq_words + 1)

	mal_like = mal_class_prob
	for element in elements:
		if element in mal_prob_dict:
			mal_like *= float(mal_prob_dict[element])
		else:
			mal_like *= (1.0) / (mal_total_words + uniq_words +1)

	if normal_like > mal_like:
		no_normal += 1
		print "normal:" , normal_like, ">", mal_like 
	else:
		no_mal += 1
		print "mal:" , mal_like, ">=", normal_like

print 'Normal:', "{0:.0%}".format((no_normal)/(no_normal+no_mal)), '| Mal:', "{0:.0%}".format((no_mal)/(no_normal+no_mal))


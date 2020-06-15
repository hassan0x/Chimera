from os import listdir
import numpy as np
import sys, os

normaldir = './Normal'
maldir = './Malicious'
normalfiles = []
malfiles = []

for file in listdir(normaldir):
	if '-train90.txt' in file:
		normalfiles.append(normaldir + '/' + file)

for file in listdir(maldir):
	if '-train90.txt' in file:
		malfiles.append(maldir + '/' + file)

print "List of normal files:", normalfiles
print "List of malicious files:", malfiles

normal_data = []
mal_data = []

for file in normalfiles:
	fp = open(file, 'r')
	for line in fp.readlines():
		clean = (line.decode('iso-8859-14').encode('utf8')).strip('\n')
		normal_data.append(clean)

for file in malfiles:
	fp = open(file, 'r')
	for line in fp.readlines():
		clean = (line.decode('iso-8859-14').encode('utf8')).strip('\n')
		mal_data.append(clean)

normal_dict = {}
mal_dict = {}

for line in normal_data:
	elements = line.split(',,11,,')
	for element in elements:
		if element in normal_dict:
			normal_dict[element] += 1
		else:
			normal_dict[element] = 1

for line in mal_data:
        elements = line.split(',,11,,')
        for element in elements:
                if element in mal_dict:
                        mal_dict[element] += 1
                else:
                        mal_dict[element] = 1

del normal_dict['']
del mal_dict['']

normal_prob_dict = {}
mal_prob_dict = {}
normal_total_words = sum(normal_dict.values())
mal_total_words = sum(mal_dict.values())

tmpp = normal_dict.copy()
tmpp.update(mal_dict)
uniq_words = len(tmpp.keys())

normal_class_prob = float(len(normal_data)) / (len(normal_data) + len(mal_data))
mal_class_prob = float(len(mal_data)) / (len(normal_data) + len(mal_data))

print "total number of words in normal:", normal_total_words
print "total number of words in mal:", mal_total_words
print "uniq words:", uniq_words
print "normal class probability:", normal_class_prob
print "mal class probability:", mal_class_prob

for word,count in normal_dict.items():
	prob = float(count + 1) / (normal_total_words + uniq_words + 1)
	normal_prob_dict[word] = prob

for word,count in mal_dict.items():
        prob = float(count + 1) / (mal_total_words + uniq_words + 1)
        mal_prob_dict[word] = prob

fp = open('calc.txt', 'w')
for word,prob in normal_prob_dict.items():
	fp.write(word + ':::' + str(prob) + ',,,')

fp.write('+++')

for word,prob in mal_prob_dict.items():
        fp.write(word + ':::' + str(prob) + ',,,')

fp.write('+++')

fp.write(str(normal_class_prob) + ':::' + str(mal_class_prob) + ':::' + str(normal_total_words) + ':::' + str(mal_total_words) + ':::' + str(uniq_words))

print "data written to calc.txt"

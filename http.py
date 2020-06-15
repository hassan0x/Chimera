from scapy.all import *
from os import listdir
import sys, os

dirs = ['./Normal','./Malicious']
files = []

print "Enumerating files ......"
for dir in dirs:
	for file in listdir(dir):
		if file.find('.pcap') == len(file) - 5:
			files.append(dir + '/' + file)

print "Files are:", files

for file in files:
	print "Reading file: ", file
	packets = rdpcap(file)

	raw_packets = []
	for packet in packets:
		if packet.haslayer(TCP):
			if packet[TCP].sport == 80 or packet[TCP].dport == 80:
				if packet.haslayer(Raw):
					raw_packets.append(packet)

	http_packets = []
	for packet in raw_packets:
		http = packet[Raw].load
		if '\r\n\r\n' in http and 'HTTP/' in http:
			tmp = http.split('\r\n\r\n')[0]
			http_packets.append(tmp)

	http_headers = []
	for packet in http_packets:
		tmp = packet.split('\r\n')[1:]
		http_headers.append(tmp)


	print "Total length of data in the file is", len(http_headers)
	train_headers = http_headers[0:int(len(http_headers)*0.9)]
	test_headers = http_headers[int(len(http_headers)*0.9):]

	# write the 90% of data to the training data file
	print "Writing 90% of data to file: ", file[:len(file)-5] + '-train90.txt, (', len(train_headers), ')'
	fp = open(file[:len(file)-5]+'-train90.txt', 'w')
	for line in train_headers:
		for value in line:
			tmp1 = value.split(': ')[0].lstrip()
			tmp2 = value.split(': ')[1].lstrip()
			fp.write(tmp1 + ':"' + tmp2 + '",,11,,')
		fp.write('\n')
	fp.close()

	# write the 10% of data to the testing data file
        print "Writing 10% of data to file: ", file[:len(file)-5] + '-test10.txt, (', len(test_headers), ')'
        fp = open(file[:len(file)-5]+'-test10.txt', 'w')
        for line in test_headers:
                for value in line:
                        tmp1 = value.split(': ')[0].lstrip()
                        tmp2 = value.split(': ')[1].lstrip()
                        fp.write(tmp1 + ':"' + tmp2 + '",,11,,')
                fp.write('\n')
	fp.close()

# Chimera
### Threat hunting tool based on machine learning

This tool can predict the malicious http traffic from the normal http traffic based on the naive bayes algorithm

This tool is consists of three parts:
  - the preprocessing data part.
  - the trainning part.
  - the testing part.
  
## Preprocessing Part
the tool can take a .pcap file and extract from it all the http headers and divided this http headers to 90% to the training data and 10% to the testing data, just you need to put your normal pcap files in the Normal Directory and the malicious ones in the Malicious Directory.

```
python http.py
```

then you will find inside the Normal Directory the normal http headers, and inside the Malicious Directory the malicious http headers, and they both are divided to 90% to the trainning data and 10% to the testing data.

![alt text](https://github.com/hassan0x/Chimera/blob/master/http.png?raw=true)

## Training Part
the tool then take the normal and malicious training data and perform the naive bayes theory on them (we implemented the naive bayes theory from the scratch to absulotely fit our trainning model and to increase the success rate).

```
python traing.py
```

you will find a new file called calc.txt which contains all the calculation of the trainning model (probability of normal http headers, probability of malicious http headers, number of total normal words, number of total malicious words, uniq words, probability of normal class and probality of malicious class), and we will use this file and all these calculations in the testing phase.

![alt text](https://github.com/hassan0x/Chimera/blob/master/train.png?raw=true)

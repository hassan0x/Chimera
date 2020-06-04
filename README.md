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
python train.py
```

you will find a new file called calc.txt which contains all the calculation of the trainning model (probability of normal http headers, probability of malicious http headers, number of total normal words, number of total malicious words, uniq words, probability of normal class and probality of malicious class), and we will use this file and all these calculations in the testing phase.

![alt text](https://github.com/hassan0x/Chimera/blob/master/train.png?raw=true)

## Testing Part
then the tool take the user input file that he want to test against the trainning model, and load the training model from calc.txt and perform the testing and calculations between this two, where the tool predict to which class this test case belong.

```
python test.py Normal/normal-test10.txt
```
![alt text](https://github.com/hassan0x/Chimera/blob/master/test1.png?raw=true)

```
python test.py Malicious/malicious-test10.txt
```
![alt text](https://github.com/hassan0x/Chimera/blob/master/test2.png?raw=true)

as you can see we performing the calculations and predictions on the remaining test data that we divided in the first and we don't know the types of these tests and we don't include it in our training model, so this test data are unknown to us.

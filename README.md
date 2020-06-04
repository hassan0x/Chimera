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

## Training Part

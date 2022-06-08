str= "X-DSPAM-Confidence: 0.8475"

position = str.find(':')
print(pos)
line = str[pos + 2]
print(line)
value = float(line)
print(value)
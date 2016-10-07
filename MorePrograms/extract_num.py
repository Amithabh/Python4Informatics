text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find('0')
fpos = text.find('5')
print(float(text[ipos:fpos+1]))

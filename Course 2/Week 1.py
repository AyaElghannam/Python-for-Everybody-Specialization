##chapter 6

text = "X-DSPAM-Confidence:    0.8475"
begin = text.find(':')
end = text.find('5')
Required = text[begin + 5:end + 1]
print(float(Required))

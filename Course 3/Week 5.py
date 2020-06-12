import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#data Read Using Beautifulsoap
url = input('Enter URL: ')
soup = urllib.request.urlopen(url, context=ctx)
data = soup.read()

#formating data to be python readable
tree = ET.fromstring(data)
comment = tree.findall('comments/comment')

#Summantion of couts
sumcomm = 0

for num in comment :
    sumcomm = sumcomm + int(num.find('count').text)

print('Sum:', sumcomm)

##ex1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sumnum = list()
tagNum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    
    #Not Required
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

    #Required
    x = tag.contents[0]
    sumnum.append(int(x))
    tagNum = tagNum + 1
    
print('Count', tagNum)
print('Sum', sum(sumnum))


#ex2
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))

while(count>0):
    tags = soup('a')
    links=[]
    
    for tag in tags:
        links.append(tag.get('href')) 

    retrieve_link = links[position - 1]
    print('Retrieve link:', retrieve_link)
    html = urllib.request.urlopen(retrieve_link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count-1

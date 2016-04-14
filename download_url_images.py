import re
import urllib2
import urllib

url = 'http://' + raw_input("Please enter your url: ")

page_source = urllib2.urlopen(url)
page_source = page_source.read()

extensions_wanted = ['.png', '.jpg', '.jpeg', '.bmp']

matches = re.findall(r'\ssrc="([^"]+)"', page_source)
images = []

for i in matches:
    if i.endswith(tuple(extensions_wanted)):
        if i.startswith('http'):
            images.append(i)
        else:
            images.append(url + i)

urllib.urlretrieve(images[0], images[0].split('/')[-1])

for i in images:
    urllib.urlretrieve(i, i.split('/')[-1])
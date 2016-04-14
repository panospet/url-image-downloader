import os
import re
import urllib2
import urllib


def ask_user_for_url():
    input_url = raw_input("Please enter your url: ")
    if not input_url.startswith('http'):
        full_url = 'http://' + input_url
    else:
        full_url = input_url
    return full_url, input_url


def is_url_up(full_url):
    if urllib.urlopen(full_url).getcode() == 200:
        return True
    else:
        return False


url, input_url = ask_user_for_url()
while not is_url_up(url):
    print "The url you gave is DOWN!!"
    url, input_url = ask_user_for_url()

page_source = urllib2.urlopen(url)
page_source = page_source.read()

extensions_wanted = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']

matches = re.findall(r'\ssrc="([^"]+)"', page_source)
images = []

for i in matches:
    if i.endswith(tuple(extensions_wanted)):
        if i.startswith('http'):
            images.append(i)
        else:
            images.append(url + i)

if not os.path.exists(input_url):
    os.makedirs(input_url)

for i in images:
    urllib.urlretrieve(i, input_url + '/' + i.split('/')[-1])

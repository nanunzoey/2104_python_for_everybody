import urllib.request
import urllib.parse
import urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)

sum = 0

uh = urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved', len(data), 'charaters')

try:
    js = json.loads(data)
except:
    js = None

counts = js['comments']

for c in counts:
    c = c['count']
    sum += c

print("Count: ", len(counts))
print("Sum: ", sum)

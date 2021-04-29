import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl


url = input('Enter location: ')

sum = 0

print('Retrieving', url)
xml = urllib.request.urlopen(url).read()

print('Retrieved', len(xml), 'charaters')
tree = ET.fromstring(xml)

counts = tree.findall('.//count')
for count in counts:
    count = int(count.text)
    sum += count

print("Count: ", len(counts))
print("Sum: ", sum)

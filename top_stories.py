import pandas as pd 
import requests
import xml.etree.ElementTree as ET

url = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'

# creating HTTP response object from given url
resp = requests.get(url)

# saving the xml file
with open('top_stories.xml', 'wb') as f:
    f.write(resp.content)


# create element tree object
tree = ET.parse('top_stories.xml')

# get root element
root = tree.getroot()

# create empty list for news items
top_stories = []

# iterate news items
for item in root.findall('./channel/item'):

    # iterate child elements of item
    for child in item:
        if child.tag == 'title':
            top_stories.append(child.text.replace('Top story - ',''))

df = pd.DataFrame(top_stories,columns=['Top Story'])
# df.head()
df.to_csv('/home/kesha/BHM/Top_story.csv')

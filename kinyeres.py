from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com'

response = urlopen(url).read()

soup = BeautifulSoup(response)

print soup.html.head.title.string
print ""

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = url + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        print person_soup.find("span", attrs={"class": "email"}).string

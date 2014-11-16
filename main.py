from bs4 import BeautifulSoup

import requests

url = "www.cs.dartmouth.edu/~scot/cs10/syllabus.html"

r  = requests.get("http://" +url)

data = r.text


r.encoding = unicode


soup = BeautifulSoup(data)

#for link in soup.find_all('a'):
    #print(link.get('href'))
    
print soup.find('a')


print soup.find('a').get('href')




########################################

first_url = soup.find_all('a')[3].get('href')
print first_url
a = requests.get(first_url)

a.encoding = unicode

data_first = a.text

soup_first = BeautifulSoup(data_first)

print soup.find('a').get('href')
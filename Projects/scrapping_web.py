from bs4 import BeautifulSoup
import requests
url = ("https://www.kuvendikosoves.org/shq/deputetet/")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
for each_div in soup.findAll('h4',{'class':'name'}):
    print (str(each_div)[17:][0:-5])
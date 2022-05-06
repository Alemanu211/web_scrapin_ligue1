import requests
from bs4 import BeautifulSoup

from lxml import etree

#Function to Find the element from the Xpath
def Xpath(url,path):
  Dict_Headers = ({'User-Agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
      (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
      'Accept-Language': 'en-US, en;q=0.5'})
  # Gets the requried data https browser's address bar
  webPage = requests.get(url,Dict_Headers)
  # Creating a soup Object from the html content
  Scraping = BeautifulSoup(webPage.content, "html.parser") 
  # Conveting Soup object to etree object for Xpath processing
  documentObjectModel = etree.HTML(str(Scraping)) 
  return (documentObjectModel.xpath(path)[0].text)


#Extraction des données de la page
url='https://www.ligue1.fr/calendrier-resultats'
path = '/html/body/main/div[3]/div[2]/div/div[2]/ul[3]/li/a/div[1]/div/span[1]' #Changer val du ul

print(Xpath(url,path))














# r = requests.get('https://www.ligue1.fr/calendrier-resultats')
r = requests.get('https://www.ligue1.fr/calendrier-resultats?seasonId=2021-2022&matchDay=6')
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='calendar-widget-container')
teams = s.find_all('div', class_ = 'club home')
team_name = s.find_all('span')

for team in team_name:
    print(team.text)

import requests
from bs4 import BeautifulSoup

MAIN_URL = 'https://pl.wikipedia.org/wiki/'

def scrap_cities():

    cities = []

    page = requests.get(MAIN_URL + 'Miasta_w_Polsce')
    soup = BeautifulSoup(page.content, 'html.parser')

    cities_from_wiki = soup.findAll('div',style="-moz-column-count:3; -webkit-column-count:3; column-count:3;")

    for section in cities_from_wiki:
        for city in section.findAll('li'):
            cities.append(city.find('a').contents[0])

    return cities

def scrap_city_details(cities):

    cities_detailed = {}

    for city in cities[0]:

        page = requests.get(MAIN_URL + city)
        soup = BeautifulSoup(page.content,'html.parser')

        city_info = soup.find('table',{'class':'infobox'})
        city_info = city_info.findAll('tr')[0]

        print(city_info)


def save_cities(page):
    pass

def get_all_cities():
    pass

def get_city():
    pass


#id = 1stTab_wrapper
#id = 1stTab
#tr

if __name__ == '__main__':

    cities = scrap_cities()
    scrap_city_details(cities)

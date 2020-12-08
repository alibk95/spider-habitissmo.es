import requests
from bs4 import BeautifulSoup



class Spider:
    def __init__(self):
        self.article = str()
        self.base_url = "https://empresas.habitissimo.es/"

    @staticmethod
    def get_highlevel_categories() -> list:
        return ['construccion', 'reformas', 'mudanzas', 'obras-menores', 'instaladores', 'mantenimiento', 'tiendas']

    @staticmethod
    def build_highlevel_urls(self):
        categories = Spider().get_highlevel_categories()
        url_list = []
        for cat in categories:
            url_list.append(self.base_url+cat)
        return url_list

    


if __name__ == '__main__':
    spider = Spider()
    print(spider.build_highlevel_urls())


# url = 'https://empresas.habitissimo.es/do_ajax/business_modal_phone'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.find("ul", {"class":"button-links-list external-link"}).li.a.get('title'))


# Handle the modal for the contact details
data = {'normalized_name':'german-s-moll-pelegri-pintura-y-decoracion'}
response = requests.post(url, data=data)
print(response.text)
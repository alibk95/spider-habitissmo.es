import requests
from bs4 import BeautifulSoup




url = 'https://empresas.habitissimo.es/do_ajax/business_modal_phone'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.find("ul", {"class":"button-links-list external-link"}).li.a.get('title'))


# Handle the modal for the contact details
data = {'normalized_name':'german-s-moll-pelegri-pintura-y-decoracion'}
response = requests.post(url, data=data)
print(response.text)
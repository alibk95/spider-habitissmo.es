import requests
from bs4 import BeautifulSoup


base_url = "https://empresas.habitissimo.es/"
ajax_url = "https://empresas.habitissimo.es/do_ajax/business_modal_phone"
https://www.google.com/recaptcha/api2/userverify?k=6LevSB0TAAAAAMeozttqborfeQU27GDO6kiSOsEm
googlekey = "6LevSB0TAAAAAMeozttqborfeQU27GDO6kiSOsEm"
api_key = "c44e7e216f79b38a6f84e497191ca830"
api_url = f'https://2captcha.com/in.php?key={api_key}method=userrecaptcha&googlekey={googlekey}&json=1'
def create_urls(url) -> list:
    categories = ['construccion', 'reformas', 'mudanzas', 'obras-menores', 'instaladores', 'mantenimiento', 'tiendas']
    url_list = []
    for cat in categories:
        url_list.append(url+cat)
    return url_list


urls = create_urls(base_url)
for url in urls:
    a = 1
    while True:
        url_in_page = url+f"/{a}?"
        a = a + 1

        page = requests.get(url_in_page)
        soup = BeautifulSoup(page.text, 'html.parser')
        articles = soup.find_all("article", {"class": "preview-business premium"})
        del soup
        del page
        for article in articles:
            title = article.find("div", {"class": "business-name"}).text.strip()
            title_url = article.find("div", {"class": "business-name"}).a.get('href')
            rating = article.find("span", {"class": "rating-number t-sm hidden-xs"}).text.strip()
            city = article.find("div", {"class": "business-working-meta"}).a.text.strip()
            service = article.find("div", {"class": "business-services"}).div.a.text.strip()



            page = requests.get(title_url)
            soup = BeautifulSoup(page.text, 'html.parser')
            contact_id_name = soup.find("a", {"id": "show_phone"}).get('data-name')
            company_url = soup.find("a", {"title": "Página web"}).get('href')
            data = {'normalized_name': f'{contact_id_name}'}
            del soup

            response = requests.post(ajax_url, data=data)
            soup = BeautifulSoup(response.text, 'html.parser')
            phone = soup.find_all("a", {"class":"phone btn btn-md btn-primary btn-icon"})

            phone_list = []
            for p in phone:
                phone_list.append(p.text.strip())

            del soup
            del page
            print(company_url)
            print(phone_list)
            print(title)
            print(title_url)
            print(rating)
            print(city)
            print(service)
            print("####################")



# url = 'https://empresas.habitissimo.es/do_ajax/business_modal_phone'

# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.find("ul", {"class":"button-links-list external-link"}).li.a.get('title'))


# Handle the modal for the contact details
# data = {'normalized_name':'german-s-moll-pelegri-pintura-y-decoracion'}
# response = requests.post(url, data=data)
# print(response.text)
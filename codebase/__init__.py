import requests
from bs4 import BeautifulSoup
import time
import csv

# website base url
base_url = "https://empresas.habitissimo.es/"
# the url to send POST request for solving the recpatcha
ajax_url = "https://empresas.habitissimo.es/do_ajax/business_modal_phone"



def solve_captcha():
    """
    Just by looking at the developer mode on browser, it is seen that by solving the recaptcha by hand it sends the
    following static data to the following url and by emulating the same behaviour we are able to bypass the recaptcha.
    # TODO: getting the data dynamically.
    """
    print("SOLVING CAPTCHAAAAAAAAA!!!! :_))))))))))")
    # This is the url that after checking manually we learned that POST request is sent to
    captcha_url = "https://www.google.com/recaptcha/api2/userverify?k=6LevSB0TAAAAAMeozttqborfeQU27GDO6kiSOsEm"
    data = {
        'v': 'qc5B-qjP0QEimFYUxcpWJy5B',
        'c': '03AGdBq26fJox9THfWuHKVpddYkNn4fRK115mYY1HHzRsK5pMrpTIk3wC1hvMk7uvub0EEheOnuWIXsgtGVio1figA5W_wjL8f3YnZTsh'
             'E6eGS_lZEzp-lPdITcRWAAfuzxULokrS36yIjA_YB2yddZOE3yKa5svWK80TOvt4MbjUfzxqKL93gja2VnhMh60vrhiJa_6hV6G7Nf95Z'
             'rMqQ0ILQHeCYm5eM5W4PG38AwxS4afNt9m2bq0ayIs05xfpYkZKuN0-5DYSDxP0Us7qMCuT7aqLmfDmgyD12yHewathqMOY1VRMM8UZSX'
             'ZrvivE7OEc6-d0WuIjuJRVEk4xXnKUihI4V-It4xtNUPQ8BgV1MSBlPSQGBnTRe11yiifSsnOEX7AiZIowZVseiwus-JGDroH-rKobEm8'
             'VA-T1cdWpQiZ7an8GSEl06ZpJDX9PDzGq1oIJ_OxNGcFkqNzXTVCH-VmbvQHhwZy62OC1KPz0Rh0-UUJ6TyHjEpBpbsPEZRA5uNfu3cxY'
             'xqTzafMT48C5A5chrR0GOcqvwXIL6We9tyiRD0MaExXPSAHMHwFYxd-71ky01UGVEJusb9sztDISXLo2YNv3tcVUY35BqV-i-FAyo0Xr7'
             '1yBindfctwaRF9rvdlfAxaTeCAxL6TGPx7u9veyjocperjEyJo-13J3KLvLkefC1ev_zOH7uoWHV4zXUSZHgy3aQVG8lL-ihmHosvDFDL'
             'jZd21u5PLdkUeiJVWSD-PgihaBv-GHq7hkXFAztX54hsvCOaLbdwOCmkjGF607kT-AUhMcfo3jeqzlr6fp3emkWT_N3YnnkVeUnFafJ0x'
             'Mm8Jx2wtW8BB9_Bsf6J-Xc116pkNAlYdJYPFplfllkFHeN5eE6eA2StrUID1aFk3OYSW8n2NNss0K9Xlo7L_qyKhYc7tcEi1lXEllYkHR'
             'pvhCcXGaW0nK5fyOz0z-BiwxD026gbfzkyD7_3xPE0RNXA022Qu9b7ZNx4Hkmhs_OMup7kjz_lwHdfqSgug85QeaoLDVjyitM6-xQNAIH'
             'cP6UmuMVwtBkAHiy-rtFVoK_mmka3MCGM2wIoYYgwWCSZViDfVLj50uQf0e_26QtXEnc247u6WBEOS_xepIRDL8KoFV13Y4UqeuTnwBAA'
             'C8Z4Nv-ylTd9IOc1fyeR_sDSUgxxfOngwOqMkfdiILINXVER0_LtR0SC6jKn1nJ0pGDQgM7KoSkMUww1A3QaR4-ZjR0Yg_s_DUTx4AVxb'
             'mFKLJgPO_6Ex_T5hodMl7zgAYPCk4KJO93RG2e0xUBOD4BGkChxrRpB6RXrBKM0bj08N5dSEQ4syNwnyZi7SrozjCISgrd2YFcxRTrYxW'
             'ZnOZwibnB8kYs8CIPS0hvDv4hucB9CvVxc1XKYElVlmUnccwNqxxThPP7ftV8JtihkkE2LZ3MV-4bo5Asm2MvgLErvd7JVy2UZZZcnYd5'
             'FBSOWjuHLRgASptTH_elhfjzWXTI8pSvxGob-SGOs4KG2u_aN5KcjgywBgc9kamb2DNbev_taqtObSLQyXuswfEaydz5uKWjpn6WbdKgd'
             'U6lCvr_zPKGun-JOCQRJWdTN8HZr-dmm8Ed7qCwo7VTUJaZjqwHt9Bmy3WeV4xO-Jk52IxmiYWW57VbxiBsV9db33DGFKmglFppabTJ5n'
             '1E1OQhborC1bWh-CCfOaHU5C7jDxSu7vWycFxjRrMEZ8ddoXMTAlrDeEU24RSOyKbXauCgTSjbPPIMRzl0QluX2O2yXvVJ_g_4TcM0ETR'
             'upRQuV7dRhfXrpUcDwqK8_m-kKgeGn7Oie5V4m0enL3l9-FYFUtEqmjCzYdCj6CRMw0zKfg9y9VhPnu7Hc6qK-I6_oMVyHDUzW70_T7Vg'
             '6gB-svynGIQURjaCGL-0Fh_-Uf0I6KINnTz_eGSxZpiGzesAa32zq4fSKUbBkj1Cu8nQeZZDAKFiyJuB3Vc-A-nAZwaLCEgkf2zgT0RXh'
             'mFqK_wgODOAAI8NqGKLgHDCWel8ufuGnh93nHbJRdnaMklqZB1GcbBPjcmWnltgDxF6-XzK1XFMg9yrTf6nX2lQEZbSj9LnK1IaMt_UWt'
             'cAJjADmvYmVKlfVTU1OQLMymyrY3inUimAbupcK7y-JQ9gJ_X2fu8eyQWSVjrbHFtwP12Jx7BCwqCHmn8193-ri1eg1wGnV7PVoNiU81m'
             'kj9IA_0yUZ6NMJaCmpN1KKqygaGJzWO44OncJ4L-79fv9GOxievVCYj230JOVtkyW6CB_vKsjiD2yiiI-cXbrhB76-CUtTCey1GZxr8y7'
             'JzxDxRRUlIeKOvEirSyPp-pQcxOgaTDP9VS2K27CgjQ1FE_f_p_MqSs1hVDB2KWjoXuE1E0krIDYjiJG0eMtfkuXJ2KgnKewytVba4OoG'
             'PmqX8_3VoWaF4nnAv_n3VVgz5jPZszhYM_sKQBl1VKci2fsAMGGr8vd2cQWVyLtwZYURxWHQ-X9mBAbO2__wrOoSvgP9Nb2g56cHnYr2N'
             'USLa4PMit2VslbADuoVzaUoFVrPj1eN4QI-T5fSDIwDauBTSUvHSwf1z7U97kZLt9OxhOKwCD82J2ksqf9cfn-cCCVe3UnOmKNuNTWhYX'
             '3Bn00Tpo5u4hNQAes9Q9rUQNILg7X2iY0Lle-Ch-7BwM1ZMgP5ujRuH8cHNiY4bJwisYbGmIhxna-fFUs0B_SbB-QjlQjb-yfkEXLMz4j'
             'C7ynCVpYUOhF8nyAIXWTXk_3iNJ3WJq3SZfpqbY8Dhkxx_HHqxtHQwf7pz2i6J5_5JcOg_nQJvL9wYnNXGehlujLNnitP3_cTVm3u08fZ'
             'RNDh1HH8FLyjMmmxUQvb5LZ5zQYMbj6QOpxa0SCnFnJPElDXtChsv-D_tPoEG0bm1Amc21wWR4VR8YMmupkzoYQRrx6gPXObDmef9s2C2'
             'fOVg33sByW4w_FKT_z6F9ewiNdfdhAHbsiqc0_rqh5UbPerhm8aHvphfYJHuZ51LZSkdf8sU0WWENImAOd8eylA3Kk1nTYO7yQlUnv_MO'
             'wO7il2rIFPKCCBG3k5kcVpFavX3CWrHpCw6pN6iZ6PKmBXsO3wPtXSsspr3E17mUhZCStfJEQKLCjY2rjt8U',
        'response': 'eyJyZXNwb25zZSI6IiIsInMiOiI5OTg5IiwiZSI6ImJXMXZDS2cifQ',
        't': '826',
        'ct': '826',
        'bg': '!ISegJw7IAAX6VNIG-kcr408_o3JpR11oxxTqxgu42wcAAAJYVwAAAA1tAQecBCxAHDzp2L_mh1jiuDnsJ-BKiJr38FdfWlB3C79cr9K'
              '2Ypp27d505UDb6P7o7Fc8jaJ2z_6fTysIK3WgT1himbjBJwbrtVDVAMYxeMSpfJBVc3OBz29Pd8c5Z3DcXMqOSiziqUgsoTrHB4Jo_8W'
              'M2ij1GqoqvCgRCDs7k1pmhg0ytT4is8h5yH2x0XtI2TtZXS7IGA3uJg2R587ieaRWbYv5x3NXR7uD8TXGl1FPXmUVxCod04vSv_cv2vA'
              'w1TC0YU3cGh_6vc8FeSqajX5mxDO4Wy52QqVvg6-EiDqJUqH3AbL3_UW54tphxCIRVgQmuYb3F7kmL8FLQieKGSApE9mka_997W5miBk'
              'CrQH9YQKZV-iq-LjS2ZocTR1Ci3YgSedNZ16NEqu9xmkA78et7mIezm6OzN-r33t7oor5578IeaviSScaB5AlGQpW5pc6Jk9sqjNFezp'
              'IE0e1mQhnpgbL2JAR4RGhGSIi5FjjHl9YPPBoabOtvX39oVI6D-3ap1WrHKCvNsWiUQuDRuo790bXYuc--vyT5gbmfd7OHLWFClX5F6U'
              'WKp7bPrRLaocQ_XXdqusHHHfcMnC1eECanTqvz-1xSXVGsetk4Mb4avLF0OLdy2oMXvRFuNcJQBosfQNyGAVU1pPVsE-TZF1NE7IF40a'
              '1FS7ZnNQ9YgAul7BUHeo9iGP5uqRhdUT0oH-3jlns6JxqUyG8SkH6Qd9sasZs8_efNXGUjUQnYAdfnVc7wOAsquFBEBOeGooPkxrGkZt'
              'fCYvEKiUNmmqi5C5oaQtJXxAGRbrH45lFHjiB29IWzz4URp7P6r2puJQY9XmwGqVdeOBRt4njfzzzTWaIj6cs7YwU3Fi7PKvVstpB-5y'
              'CdHTplk8xCcWLX-iT4C6m0wouXQdc0Sij5_CjFTKXIQ3odERk0KvgZytqdH6lwHMe3vq977-xBVLrZfOtH4b9kdnTs_4ydhPT1CUo0hc'
              'JAqjObK-5kjbiYSjt3JAP7_1pbZKNFaE0gx-NXUYtfPGVlLgA4bg9WQpNXmS7k8H9DYFavSP7fa_dr1s4zc0NjqpszrTsPzeVT5PgZTl'
              'lbVJlBTGcoapbKK1x4ucuxay3J_UMI988pQ_sX5HetwGZY1mR2JpFzz1-YEf5e0Ny7JYtCuhjKrNhPWTAOjM4ggXGV7jkKeUsqesuC4T'
              'dS7TgI8GTRMWpKR0NXfkBUZJAVCneWJ_cXPumWbGAvmtCwHvsb6MiviBDGZO10vn8EkyHApHWYj3LZbyQycBShRrkoGJEVz7xWSER19l'
              'N_IZepTzzfb53ciNRTlQpYc2-9qoL8nCH2VtMPVN5poAHxKPfBCNutP_2b7_ARlpsT18NX7A_KMYYk4hKsIhbVSJg5ejqRbmHDKdQA7B'
              'gBXbOexO61F366uMq_yykMQ2d2OAxuHg'
    }
    requests.post(captcha_url, data=data)
    # To give some time to the recaptcha to load
    time.sleep(5)
    requests.post("https://empresas.habitissimo.es/do_ajax/business_modal_phone",
                  data={'normalized_name':'espacio-de-interiorismo-y-urbana', 'recaptcha':'03AGdBq27T4pEo3xIkH4V82YyGA8'
                                                                                          'HlQBVm-JGK2duoKE3ZuMyLCJlIWZ'
                                                                                          'REp-si63W_3aEbXP7wZcKs7xcXyk'
                                                                                          'itMHtNScyLBxhAZkUqee5nRaHvYw'
                                                                                          'Ra4luH9Z9TBdilrjIJuRxVtf8Stv'
                                                                                          'KjKwWHXeM48ruVa4xxopVBk6VehW'
                                                                                          '3sWyLOeqng_Fz904xm5ETv-kPSLp'
                                                                                          'VpYeNrcVYAFriy9lFCL4_z9UE4WH'
                                                                                          '3hJysgj7D2vuBIj02s0FmO8KXeQi'
                                                                                          'o93CIgdNlnDuVnDvFhV4ibC7favu'
                                                                                          'nH7cSzhaHD86REvrJJstVP7j3PYz'
                                                                                          'X3a-Qr65OLziD3Mem9hDRC9xSI5G'
                                                                                          '8TEcE8tdHpkplJPe0yOmkC3eztfs'
                                                                                          'perIIp23aC-Hi0N-NREpCQjcjZhI'
                                                                                          'iME7JikonssKly5HRUPxi-8QtOUL'
                                                                                          '0XooJOQSoOtkeMrP9pWkRQiQQHpu'
                                                                                          'JOwXGNhxxV_nzY'})
    time.sleep(4)


def write_csv(title, phone1, phone2, service, company_url, city, rating):
    fieldnames = ['company_name', 'phone1', 'phone2', 'service', 'source', 'company_url', 'city', 'rating',
                  'country_code', 'country']
    with open(r'output.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Basically this checks if the file already exists with headers then it skips writing headers again.
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'company_name': title, 'phone1': phone1, 'phone2': phone2, 'service': service, 'source': "habitissmo.es",
                         'company_url': company_url, 'city': city, 'rating': rating, 'country_code': "ES",
                         'country': "Spain"})


def create_urls(url) -> list:
    """
    The whole website is divided in to this services and each has many pages. This function helps to create those url's
    of different services and the scraper needs to go in each of the urls and scrape the pages till end.
    :return: list of high level url's
    """
    categories = ['construccion', 'reformas', 'mudanzas', 'obras-menores', 'instaladores', 'mantenimiento', 'tiendas']
    url_list = []
    for cat in categories:
        url_list.append(url+cat)
    return url_list


urls = create_urls(base_url)
# Main loop
for url in urls:
    a = 1
    # max 200 pages of each service are useful for us as the rest are not providing any contact info's.
    while a < 200:

        print(f"           #####PAGE {a}#####           ")
        # The structure of the url address bar is changing in each page as below. e.g. a = 1 : page 1 a = 2 : page 2
        url_in_page = url+f"/{a}?"
        print(url_in_page)
        a = a + 1
        # Check if we reached to the end of the pages for each service and break the loop there.
        page = requests.get(url_in_page)
        if page.status_code == 404:
            break
        # Making the soup :  )
        soup = BeautifulSoup(page.text, 'html.parser')

        try:
            # articles are the sections that businesses are laying their infos. Basically each page has around 30
            # articles and each contains infos about the specific business.
            articles = soup.find_all("article", {"class": "preview-business premium"})
        except:
            articles = soup.find_all("article", {"class": "preview-business business"})
        # this is extremely important to take care of the garbage collection on python and delete the objects that we
        # are not going to use. (Specially in such a scraper that is going to run many loops)
        del soup
        del page
        # For each business (article) the information is mainly is coming from here.
        for article in articles:
            title = article.find("div", {"class": "business-name"}).text.strip()
            title_url = article.find("div", {"class": "business-name"}).a.get('href')
            try:
                rating = article.find("span", {"class": "rating-number t-sm hidden-xs"}).text.strip()
            except:
                rating = ""
            try:
                city = article.find("div", {"class": "business-working-meta"}).a.text.strip()
            except:
                city = ""
            try:
                service = article.find("div", {"class": "business-services"}).div.a.text.strip()
            except:
                service = ""

            # to retrieve the contact info and webpages we need to enter to each article website
            page = requests.get(title_url)
            # again make a soup here
            soup = BeautifulSoup(page.text, 'html.parser')
            # this needs to retrieved in order to later use it for getting the contact details from the Modal.
            contact_id_name = soup.find("a", {"id": "show_phone"}).get('data-name')

            try:
                company_url = soup.find("a", {"title": "Página web"}).get('href')
            except:
                company_url = ""
            data_load = {'normalized_name': f'{contact_id_name}'}
            del soup
            # This POST request is basically means that push the contact button to open the popup of contact details.
            response = requests.post(ajax_url, data=data_load)
            # again making a soup from that modal
            soup = BeautifulSoup(response.text, 'html.parser')
            # If it contains this span it means that the recaptcha is just appeared and we need to solve it.
            if soup.find("span", {"class":"msg"}):
                del soup
                solve_captcha()
                response = requests.post(ajax_url, data=data_load)
                soup = BeautifulSoup(response.text, 'html.parser')
            else:
                del soup
                response = requests.post(ajax_url, data=data_load)
                soup = BeautifulSoup(response.text, 'html.parser')
            # we came all this way to reach this phone number :  ))
            # Since there might be more than one phone number we push them in a list.
            phone = soup.find_all("a", {"class": "phone btn btn-md btn-primary btn-icon"})
            phone_list = []
            for p in phone:
                phone_list.append(p.text.strip())
            if len(phone_list) == 2:
                phone1 = phone_list[0]
                phone2 = phone_list[1]
            elif len(phone_list) == 1:
                phone1 = phone_list[0]
                phone2 = ""
            else:
                phone1 = ""
                phone2 = ""
            # very critical !
            del soup
            del page

            print(title)
            print(phone1)
            print(phone2)
            print(company_url)
            print(rating)
            print(city)
            print(service)
            write_csv(title, phone1, phone2, service, company_url, city, rating)
            print("####################")

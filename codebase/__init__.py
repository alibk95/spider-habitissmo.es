import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://empresas.habitissimo.es/"
# the url to send POST request for solving the recpatcha
ajax_url = "https://empresas.habitissimo.es/do_ajax/business_modal_phone"

# googlekey = "6LevSB0TAAAAAMeozttqborfeQU27GDO6kiSOsEm"
# api_key = "c44e7e216f79b38a6f84e497191ca830"


def solve_captcha():
    print("SOLVING CAPTCHAAAAAAAAA!!!! :_))))))))))")
    captcha_url = "https://www.google.com/recaptcha/api2/userverify?k=6LevSB0TAAAAAMeozttqborfeQU27GDO6kiSOsEm"
    data = {
        'v': 'qc5B-qjP0QEimFYUxcpWJy5B',
        'c': '03AGdBq26fJox9THfWuHKVpddYkNn4fRK115mYY1HHzRsK5pMrpTIk3wC1hvMk7uvub0EEheOnuWIXsgtGVio1figA5W_wjL8f3YnZTshE6eGS_lZEzp-lPdITcRWAAfuzxULokrS36yIjA_YB2yddZOE3yKa5svWK80TOvt4MbjUfzxqKL93gja2VnhMh60vrhiJa_6hV6G7Nf95ZrMqQ0ILQHeCYm5eM5W4PG38AwxS4afNt9m2bq0ayIs05xfpYkZKuN0-5DYSDxP0Us7qMCuT7aqLmfDmgyD12yHewathqMOY1VRMM8UZSXZrvivE7OEc6-d0WuIjuJRVEk4xXnKUihI4V-It4xtNUPQ8BgV1MSBlPSQGBnTRe11yiifSsnOEX7AiZIowZVseiwus-JGDroH-rKobEm8VA-T1cdWpQiZ7an8GSEl06ZpJDX9PDzGq1oIJ_OxNGcFkqNzXTVCH-VmbvQHhwZy62OC1KPz0Rh0-UUJ6TyHjEpBpbsPEZRA5uNfu3cxYxqTzafMT48C5A5chrR0GOcqvwXIL6We9tyiRD0MaExXPSAHMHwFYxd-71ky01UGVEJusb9sztDISXLo2YNv3tcVUY35BqV-i-FAyo0Xr71yBindfctwaRF9rvdlfAxaTeCAxL6TGPx7u9veyjocperjEyJo-13J3KLvLkefC1ev_zOH7uoWHV4zXUSZHgy3aQVG8lL-ihmHosvDFDLjZd21u5PLdkUeiJVWSD-PgihaBv-GHq7hkXFAztX54hsvCOaLbdwOCmkjGF607kT-AUhMcfo3jeqzlr6fp3emkWT_N3YnnkVeUnFafJ0xMm8Jx2wtW8BB9_Bsf6J-Xc116pkNAlYdJYPFplfllkFHeN5eE6eA2StrUID1aFk3OYSW8n2NNss0K9Xlo7L_qyKhYc7tcEi1lXEllYkHRpvhCcXGaW0nK5fyOz0z-BiwxD026gbfzkyD7_3xPE0RNXA022Qu9b7ZNx4Hkmhs_OMup7kjz_lwHdfqSgug85QeaoLDVjyitM6-xQNAIHcP6UmuMVwtBkAHiy-rtFVoK_mmka3MCGM2wIoYYgwWCSZViDfVLj50uQf0e_26QtXEnc247u6WBEOS_xepIRDL8KoFV13Y4UqeuTnwBAAC8Z4Nv-ylTd9IOc1fyeR_sDSUgxxfOngwOqMkfdiILINXVER0_LtR0SC6jKn1nJ0pGDQgM7KoSkMUww1A3QaR4-ZjR0Yg_s_DUTx4AVxbmFKLJgPO_6Ex_T5hodMl7zgAYPCk4KJO93RG2e0xUBOD4BGkChxrRpB6RXrBKM0bj08N5dSEQ4syNwnyZi7SrozjCISgrd2YFcxRTrYxWZnOZwibnB8kYs8CIPS0hvDv4hucB9CvVxc1XKYElVlmUnccwNqxxThPP7ftV8JtihkkE2LZ3MV-4bo5Asm2MvgLErvd7JVy2UZZZcnYd5FBSOWjuHLRgASptTH_elhfjzWXTI8pSvxGob-SGOs4KG2u_aN5KcjgywBgc9kamb2DNbev_taqtObSLQyXuswfEaydz5uKWjpn6WbdKgdU6lCvr_zPKGun-JOCQRJWdTN8HZr-dmm8Ed7qCwo7VTUJaZjqwHt9Bmy3WeV4xO-Jk52IxmiYWW57VbxiBsV9db33DGFKmglFppabTJ5n1E1OQhborC1bWh-CCfOaHU5C7jDxSu7vWycFxjRrMEZ8ddoXMTAlrDeEU24RSOyKbXauCgTSjbPPIMRzl0QluX2O2yXvVJ_g_4TcM0ETRupRQuV7dRhfXrpUcDwqK8_m-kKgeGn7Oie5V4m0enL3l9-FYFUtEqmjCzYdCj6CRMw0zKfg9y9VhPnu7Hc6qK-I6_oMVyHDUzW70_T7Vg6gB-svynGIQURjaCGL-0Fh_-Uf0I6KINnTz_eGSxZpiGzesAa32zq4fSKUbBkj1Cu8nQeZZDAKFiyJuB3Vc-A-nAZwaLCEgkf2zgT0RXhmFqK_wgODOAAI8NqGKLgHDCWel8ufuGnh93nHbJRdnaMklqZB1GcbBPjcmWnltgDxF6-XzK1XFMg9yrTf6nX2lQEZbSj9LnK1IaMt_UWtcAJjADmvYmVKlfVTU1OQLMymyrY3inUimAbupcK7y-JQ9gJ_X2fu8eyQWSVjrbHFtwP12Jx7BCwqCHmn8193-ri1eg1wGnV7PVoNiU81mkj9IA_0yUZ6NMJaCmpN1KKqygaGJzWO44OncJ4L-79fv9GOxievVCYj230JOVtkyW6CB_vKsjiD2yiiI-cXbrhB76-CUtTCey1GZxr8y7JzxDxRRUlIeKOvEirSyPp-pQcxOgaTDP9VS2K27CgjQ1FE_f_p_MqSs1hVDB2KWjoXuE1E0krIDYjiJG0eMtfkuXJ2KgnKewytVba4OoGPmqX8_3VoWaF4nnAv_n3VVgz5jPZszhYM_sKQBl1VKci2fsAMGGr8vd2cQWVyLtwZYURxWHQ-X9mBAbO2__wrOoSvgP9Nb2g56cHnYr2NUSLa4PMit2VslbADuoVzaUoFVrPj1eN4QI-T5fSDIwDauBTSUvHSwf1z7U97kZLt9OxhOKwCD82J2ksqf9cfn-cCCVe3UnOmKNuNTWhYX3Bn00Tpo5u4hNQAes9Q9rUQNILg7X2iY0Lle-Ch-7BwM1ZMgP5ujRuH8cHNiY4bJwisYbGmIhxna-fFUs0B_SbB-QjlQjb-yfkEXLMz4jC7ynCVpYUOhF8nyAIXWTXk_3iNJ3WJq3SZfpqbY8Dhkxx_HHqxtHQwf7pz2i6J5_5JcOg_nQJvL9wYnNXGehlujLNnitP3_cTVm3u08fZRNDh1HH8FLyjMmmxUQvb5LZ5zQYMbj6QOpxa0SCnFnJPElDXtChsv-D_tPoEG0bm1Amc21wWR4VR8YMmupkzoYQRrx6gPXObDmef9s2C2fOVg33sByW4w_FKT_z6F9ewiNdfdhAHbsiqc0_rqh5UbPerhm8aHvphfYJHuZ51LZSkdf8sU0WWENImAOd8eylA3Kk1nTYO7yQlUnv_MOwO7il2rIFPKCCBG3k5kcVpFavX3CWrHpCw6pN6iZ6PKmBXsO3wPtXSsspr3E17mUhZCStfJEQKLCjY2rjt8U',
        'response': 'eyJyZXNwb25zZSI6IiIsInMiOiI5OTg5IiwiZSI6ImJXMXZDS2cifQ',
        't': '826',
        'ct': '826',
        'bg': '!ISegJw7IAAX6VNIG-kcr408_o3JpR11oxxTqxgu42wcAAAJYVwAAAA1tAQecBCxAHDzp2L_mh1jiuDnsJ-BKiJr38FdfWlB3C79cr9K2Ypp27d505UDb6P7o7Fc8jaJ2z_6fTysIK3WgT1himbjBJwbrtVDVAMYxeMSpfJBVc3OBz29Pd8c5Z3DcXMqOSiziqUgsoTrHB4Jo_8WM2ij1GqoqvCgRCDs7k1pmhg0ytT4is8h5yH2x0XtI2TtZXS7IGA3uJg2R587ieaRWbYv5x3NXR7uD8TXGl1FPXmUVxCod04vSv_cv2vAw1TC0YU3cGh_6vc8FeSqajX5mxDO4Wy52QqVvg6-EiDqJUqH3AbL3_UW54tphxCIRVgQmuYb3F7kmL8FLQieKGSApE9mka_997W5miBkCrQH9YQKZV-iq-LjS2ZocTR1Ci3YgSedNZ16NEqu9xmkA78et7mIezm6OzN-r33t7oor5578IeaviSScaB5AlGQpW5pc6Jk9sqjNFezpIE0e1mQhnpgbL2JAR4RGhGSIi5FjjHl9YPPBoabOtvX39oVI6D-3ap1WrHKCvNsWiUQuDRuo790bXYuc--vyT5gbmfd7OHLWFClX5F6UWKp7bPrRLaocQ_XXdqusHHHfcMnC1eECanTqvz-1xSXVGsetk4Mb4avLF0OLdy2oMXvRFuNcJQBosfQNyGAVU1pPVsE-TZF1NE7IF40a1FS7ZnNQ9YgAul7BUHeo9iGP5uqRhdUT0oH-3jlns6JxqUyG8SkH6Qd9sasZs8_efNXGUjUQnYAdfnVc7wOAsquFBEBOeGooPkxrGkZtfCYvEKiUNmmqi5C5oaQtJXxAGRbrH45lFHjiB29IWzz4URp7P6r2puJQY9XmwGqVdeOBRt4njfzzzTWaIj6cs7YwU3Fi7PKvVstpB-5yCdHTplk8xCcWLX-iT4C6m0wouXQdc0Sij5_CjFTKXIQ3odERk0KvgZytqdH6lwHMe3vq977-xBVLrZfOtH4b9kdnTs_4ydhPT1CUo0hcJAqjObK-5kjbiYSjt3JAP7_1pbZKNFaE0gx-NXUYtfPGVlLgA4bg9WQpNXmS7k8H9DYFavSP7fa_dr1s4zc0NjqpszrTsPzeVT5PgZTllbVJlBTGcoapbKK1x4ucuxay3J_UMI988pQ_sX5HetwGZY1mR2JpFzz1-YEf5e0Ny7JYtCuhjKrNhPWTAOjM4ggXGV7jkKeUsqesuC4TdS7TgI8GTRMWpKR0NXfkBUZJAVCneWJ_cXPumWbGAvmtCwHvsb6MiviBDGZO10vn8EkyHApHWYj3LZbyQycBShRrkoGJEVz7xWSER19lN_IZepTzzfb53ciNRTlQpYc2-9qoL8nCH2VtMPVN5poAHxKPfBCNutP_2b7_ARlpsT18NX7A_KMYYk4hKsIhbVSJg5ejqRbmHDKdQA7BgBXbOexO61F366uMq_yykMQ2d2OAxuHg'
    }
    requests.post(captcha_url, data=data)
    time.sleep(5)
    requests.post("https://empresas.habitissimo.es/do_ajax/business_modal_phone", data={'normalized_name':'espacio-de-interiorismo-y-urbana', 'recaptcha':'03AGdBq27T4pEo3xIkH4V82YyGA8HlQBVm-JGK2duoKE3ZuMyLCJlIWZREp-si63W_3aEbXP7wZcKs7xcXykitMHtNScyLBxhAZkUqee5nRaHvYwRa4luH9Z9TBdilrjIJuRxVtf8StvKjKwWHXeM48ruVa4xxopVBk6VehW3sWyLOeqng_Fz904xm5ETv-kPSLpVpYeNrcVYAFriy9lFCL4_z9UE4WH3hJysgj7D2vuBIj02s0FmO8KXeQio93CIgdNlnDuVnDvFhV4ibC7favunH7cSzhaHD86REvrJJstVP7j3PYzX3a-Qr65OLziD3Mem9hDRC9xSI5G8TEcE8tdHpkplJPe0yOmkC3eztfsperIIp23aC-Hi0N-NREpCQjcjZhIiME7JikonssKly5HRUPxi-8QtOUL0XooJOQSoOtkeMrP9pWkRQiQQHpuJOwXGNhxxV_nzY'})
    time.sleep(5)

first_time = False
def write_csv(title, phone_list, service, company_url, city, rating, first_time):
    with open(r'output.csv', 'a', newline='') as csvfile:
            fieldnames = ['company_name', 'phone_list', 'service', 'source', 'company_url', 'city', 'rating',
                          'country_code', 'country']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if first_time == True:
                writer.writeheader()
            writer.writerow({'company_name': title, 'phone_list': phone_list, 'service': service,
                             'source': "habitissmo.es", 'company_url': company_url, 'city': city, 'rating': rating,
                             'country_code': "ES",
                             'country': "Spain"})
    first_time = False

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
        print(f"           #####PAGE {a}#####           ")
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

            try:
                company_url = soup.find("a", {"title": "Página web"}).get('href')
            except:
                company_url = ""
            data_load = {'normalized_name': f'{contact_id_name}'}
            del soup

            response = requests.post(ajax_url, data=data_load)
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup.find("span", {"class":"msg"}):
                del soup
                solve_captcha()
                response = requests.post(ajax_url, data=data_load)
                soup = BeautifulSoup(response.text, 'html.parser')
            else:
                del soup
                response = requests.post(ajax_url, data=data_load)
                soup = BeautifulSoup(response.text, 'html.parser')

            phone = soup.find_all("a", {"class": "phone btn btn-md btn-primary btn-icon"})
            phone_list = []
            for p in phone:
                phone_list.append(p.text.strip())

            del soup
            del page

            print(title)
            print(phone_list)
            print(company_url)
            print(rating)
            print(city)
            print(service)
            write_csv(title, phone_list, service, company_url, city, rating, first_time)
            print("####################")


# url = 'https://empresas.habitissimo.es/do_ajax/business_modal_phone'

# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.find("ul", {"class":"button-links-list external-link"}).li.a.get('title'))


# Handle the modal for the contact details
# data = {'normalized_name':'german-s-moll-pelegri-pintura-y-decoracion'}
# response = requests.post(url, data=data)
# print(response.text)
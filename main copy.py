from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup as bs4

# Hacer una solicitud GET para obtener el contenido HTML de la página web
url = "https://www.example.com"
response = requests.get(url)

# Crear un objeto BeautifulSoup a partir del contenido HTML de la página web
soup = bs4(response.content, 'html.parser')

# Buscar el primer tag <p> en el documento HTML
p_tag = soup.find('p')

# Imprimir el contenido del tag <p>
print(p_tag.text)

import time


import json
# import chromedriver_binary

import os

absolute_path = os.path.dirname(__file__)

# print(chromedriver_binary)


options = Options()
options.binary_location = (
    "C:\Program Files\Google\Chrome\Application\chrome.exe")
# options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--no-sandbox")
driver = webdriver.Chrome("chromedriver", options=options, )

driver.implicitly_wait(3)
url = "https://www.coolblue.nl/en/washer-dryer-combos/filter"

driver.get(url)
classname = "product-grid__card"
# open('source.html', 'w').write(driver.page_source)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
time.sleep(5)
for i in range(10):
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_UP)
    time.sleep(1)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
time.sleep(5)
elements = driver.find_elements(By.CLASS_NAME, classname)

dict = [dict() for x in range(len(elements))]

for e in range(len(elements)):
    try:
        url_imagen = elements[e].find_element(
            By.TAG_NAME, "img").get_attribute("src")
    except Exception:
        pass
    try:
        url = elements[e].find_element(
            By.CLASS_NAME, "product-card__title").find_element(
            By.TAG_NAME, "a").get_attribute("href")
    except Exception:
        pass
    try:
        driver = webdriver.Chrome("chromedriver", options=options, )
        driver.get(url)
        description= driver.find_element(
            By.XPATH, "//*[@id='product-information']/div[2]/div[1]/div[4]/div/div[2]/p").text 
    except Exception:
        pass
    try:
        dict[e] = {"title": elements[e].text,
                   "url_imagen": url_imagen, "url": url, "description": description}
    except Exception:
        pass


json_object = json.dumps(dict, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(dict)


elemento = elements[4]
url_imagen = elemento.find_element(By.TAG_NAME, "img").get_attribute("src")
text = elemento.text


print(url_imagen)

"""

 driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/table/tbody/tr["+str(i)+"]/td[2]/a/p").text """
# print(driver.title)
driver.quit()

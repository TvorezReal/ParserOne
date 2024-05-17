import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://divan.ru/category/svet"
driver.get(url)
time.sleep(3)

luminairies = driver.find_elements(By.CLASS_NAME, 'lsooF')

parsed_data = []
for luminaire in luminairies:
    try:
        name = luminaire.find_element(By.CSS_SELECTOR, 'span.name').text
        price = luminaire.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        link = luminaire.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8 qUioe ProductName ActiveProduct').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([name, price, link])

driver.quit()

print(luminairies)
with open("divan.csv", 'w',newline='', encoding='utf-8') as file:
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название', 'цена', 'ссылка'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)



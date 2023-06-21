# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

download_dir = "C:\\Tensor_course\\work11"
options_chrome = webdriver.ChromeOptions()
prefs = {'download.default_directory': download_dir,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': True}
options_chrome.add_experimental_option('prefs', prefs)
sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome(options=options_chrome)

try:
    driver.maximize_window()
    driver.get(sbis_site)
    footer_upload_sbis = driver.find_element(By.CSS_SELECTOR,
                                             '[href="/download?tab=ereport&innerTab=ereport25"].sbisru-Footer__link')
    footer_upload_sbis.location_once_scrolled_into_view
    sleep(1)
    footer_upload_sbis.click()
    print('Скачивание плагина')
    accord_themes_upload = driver.find_elements(By.CSS_SELECTOR, '.controls-tabButton__overlay')
    accord_sbis_plagin_theme = accord_themes_upload[1]
    sleep(1)
    accord_sbis_plagin_theme.click()
    sleep(2)
    upload_sbis_btn = driver.find_element(By.CSS_SELECTOR,
                                          '[href="https://update.sbis.ru/Sbis3Plugin/master/win32'
                                          '/sbisplugin-setup-web.exe"].sbis_ru-DownloadNew-loadLink__link')
    upload_sbis_btn.click()

    print('Плагин начал скачиваться')
    while not any(fname.endswith('.exe') for fname in os.listdir(download_dir)):
        time.sleep(1)
    file_url = upload_sbis_btn.get_attribute("href")

    list_of_files = os.listdir(download_dir)
    latest_file = max(list_of_files, key=os.path.getctime)
    assert latest_file in file_url, 'Скачанный файл не совпадает с наименованием файла в ссылке'

    print('Плагин скачался')
    size_in_bytes = os.path.getsize(os.path.join(download_dir, latest_file))
    size_in_mb = size_in_bytes / (1024 * 1024)
    print(f"Размер скачанного файла: {round(size_in_mb, 2)} МБ")
    sleep(3)
    # Удаление последнего скачанного файла
    # os.remove(os.path.join(download_dir, latest_file))
    # print(f"Тест прошел успешно, скачанный файл {latest_file} удален.")
finally:
    driver.quit()


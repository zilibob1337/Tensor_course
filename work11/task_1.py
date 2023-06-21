# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()
try:

    driver.maximize_window()
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не тот сайт'
    assert driver.title == sbis_title, 'Не тот заголовок'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'

    print('Переход в Контакты')
    contact_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"].sbisru-Header__menu-link')
    assert contact_btn.text == 'Контакты'
    contact_btn.click()
    sleep(2)

    print('Переход по баннеру Тензор')
    logo_tensor = driver.find_element(By.CSS_SELECTOR, '[alt = "Разработчик системы СБИС — компания «Тензор»"]')
    logo_tensor.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    assert driver.current_url == 'https://tensor.ru/', 'Не перешел на сайт tensor.ru'

    print('Проверка блока новости "Сила в людях"')
    text_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title.'
                                                      'tensor_ru-pb-16')
    assert text_block.text == 'Сила в людях', 'Нет блока "Сила в людях"'
    sleep(3)
    # Альтернативное решение: закрыть сначала строку с кукой
    # cookie_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close')
    # cookie_btn.click()
    # sleep(1)

    print('Переход в блок новости "Сила в людях" по кнопке "Подробнее"')
    block_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    text_block.location_once_scrolled_into_view
    sleep(2)
    block_btn.click()

    assert driver.current_url == 'https://tensor.ru/about', 'Не перешел в tensor.ru/about'
    sleep(3)
    print('Тест пройден без ошибок')
finally:
    driver.quit()

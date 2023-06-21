# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

fix_sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(fix_sbis_site)
    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'пальма', 'пальма123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    print('Перейти в реестр Контакты')
    accords = driver.find_elements(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title')
    sleep(1)
    contact_accord = accords[9]
    contact_accord.click()
    sleep(1)
    contact_accord_second = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact_accord_second.click()
    sleep(1)

    print('Перейти на вкладку Диалоги')
    tab_dialogs = driver.find_element(By.CSS_SELECTOR, '[name="tabdialogs"][title="Диалоги"]')
    tab_dialogs.click()
    sleep(2)

    print('Нажать на + "новое сообщение" в основном окне')
    btn_plus_contact = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper .icon-RoundPlus')
    btn_plus_contact.click()
    sleep(2)

    print('Вбить в поиск себя')
    search_box = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__field .controls-Field')
    search_box.click()
    name_contact = 'Кокc Перри'
    search_box.send_keys(name_contact)
    sleep(3)

    print('Нажать на найденного сотрудника')
    person_info = driver.find_element(By.CSS_SELECTOR, '.person-BaseInfo')
    person_info.click()
    sleep(1)

    print('Написать сообщение')
    message = 'Привет Кокс Перри! Мы на пальме!'
    msg_person = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    msg_person.send_keys(message)
    sleep(2)

    print('Отправить сообщение')
    msg_send = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"] .controls-Button__icon')
    msg_send.click()
    sleep(2)

    print('Проверка нахождения диалога самим с собой')
    msg_dialog = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item [title="Кокc Перри"]')
    assert msg_dialog.text == name_contact, 'Не обнаружен диалог c Коксом в реестре'

    print('Проверка написанного сообщения самому себе')
    msg_sending = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert msg_sending.text == message, 'Не то сообщение пришло до адресата'

    print('Наведение курсора на строку')
    tab_msg_koks = driver.find_element(By.CSS_SELECTOR,
                                       '.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s')
    assert name_contact in tab_msg_koks.text, 'Адресат не совпадает с ранее отправленному сотруднику'
    assert message in tab_msg_koks.text, 'Текст не совпадает с ранее отправленным сообщением'
    action_contact = ActionChains(driver)
    action_contact.move_to_element(tab_msg_koks).perform()
    sleep(2)

    print('Удаление сообщения')
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"] .icon-Erase')
    delete_btn.click()
    sleep(2)

    print('Проверка, что сообщения больше нет')
    tab_msg_koks = driver.find_element(By.CSS_SELECTOR,
                                       '.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s')
    assert name_contact not in tab_msg_koks.text, 'Адресат совпадает с ранее отправленному сотруднику'
    assert message not in tab_msg_koks.text, 'Текст совпадает с ранее отправленным сообщением'
    sleep(3)
    print('Тест пройден без ошибок')
finally:
    driver.quit()

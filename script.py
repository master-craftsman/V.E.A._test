from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Запуск браузера
browser = webdriver.Chrome()

# Перейти на страницу Яндекс.Диска
browser.get('https://disk.yandex.ru/')

# Авторизация на Яндекс
login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="Button2 Button2_type_link Button2_view_default Button2_size_m"]')))
login_button.click()
# Иногда автоматически плашка перескакивает на авторизацию по телефону
# email_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="Button2-Text" and text()="Почта"]')))
# email_button.click()
login_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'passp-field-login')))
login_input.send_keys('armanbeokash' + Keys.ENTER)
password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
password_input.send_keys('Arman97NikBB' + Keys.ENTER)


# Подождать загрузки страницы
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'listing-invites-to-folders')))

# Создание папки test
create_folder_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//button[@class="Button2 Button2_view_raised Button2_size_m Button2_width_max"]')))
create_folder_button.click()
choose_folder_button = browser.find_element(By.XPATH,'//span[@class="create-resource-button__text" and text()="Папку"]')
choose_folder_button.click()
# Присвоение назввания папки
folder_name_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="Textinput-Control" and @text="Новая папка"]')))
folder_name_input.clear()
folder_name_input.send_keys('test' + Keys.ENTER)

# Переход в папку test
test_folder = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="listing-item__title listing-item__title_overflow_clamp" and @aria-label="test"]')))
actions = ActionChains(browser)
actions.double_click(test_folder).perform()

# Создание файла
create_folder_button.click()
choose_folder_button = browser.find_element(By.XPATH,'//span[@class="create-resource-button__text" and text()="Текстовый документ"]')
choose_folder_button.click()
# присвоение назввания файлу
folder_name_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="Textinput-Control" and @text="Новый документ"]')))
folder_name_input.clear()
folder_name_input.send_keys('test' + Keys.ENTER)
#после создания файла, он сам автоматически открывается в новом окне
# Закрытие файла
browser.close()


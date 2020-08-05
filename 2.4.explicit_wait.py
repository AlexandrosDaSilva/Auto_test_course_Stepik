import time

# webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = driver.find_element_by_id('price')
book = driver.find_element_by_id('book')

price = WebDriverWait(driver, 12).until(
   EC.text_to_be_present_in_element((By.ID, "price"), '100')
   )
book.click()

x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

textarea = driver.find_element_by_id("answer")
driver.execute_script("return arguments[0].scrollIntoView(true);", textarea)
textarea.send_keys(y)

# Найдем кнопку, которая отправляет введенное решение
submit_button = WebDriverWait(driver, 5).until(
   EC.element_to_be_clickable((By.ID, "solve"))
   )
submit_button.click()

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

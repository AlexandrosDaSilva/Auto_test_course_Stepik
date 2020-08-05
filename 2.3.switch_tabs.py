import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/redirect_accept.html")

first_button = driver.find_element_by_tag_name("button")
first_button.click()

new_tab = driver.window_handles[1]
driver.switch_to.window(new_tab)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

print(y)

textarea = driver.find_element_by_id("answer")

# Напишем текст ответа в найденное поле
textarea.send_keys(y)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_tag_name("button")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

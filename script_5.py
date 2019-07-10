import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# находим элемент x
x_element = browser.find_element_by_id("treasure")
x_element = x_element.get_attribute("valuex")

# находим поле для ответа
input_y = browser.find_element_by_id("answer")

# вставляем элементы
input_y.send_keys(calc(x_element))

# находим и кликаем на checkbox
option_one = browser.find_element_by_id("robotCheckbox")
option_one.click()

# установка radiobutton
option_two = browser.find_element_by_id("robotsRule")
option_two.click()

# отправка формы
button = browser.find_element_by_css_selector("button.btn-default")
button.click()

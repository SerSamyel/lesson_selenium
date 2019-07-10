from selenium import webdriver

value = '//button[text()="Отправить"]'

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
elements = find_elements_by_xpath(value)
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()

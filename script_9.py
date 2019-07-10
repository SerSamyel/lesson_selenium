from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)
start_button = browser.find_element_by_css_selector("button.btn.btn-primary")
start_button.click()
confirm = browser.switch_to.alert
confirm.accept()

input_value = browser.find_element_by_id("input_value")
output = browser.find_element_by_id("answer")
output.send_keys(calc(input_value.text))

submit = browser.find_element_by_css_selector("button.btn.btn-primary")
submit.click()

from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id("input_value")
y = browser.find_element_by_id("answer")
y.send_keys(calc(x.text))

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

option_checkbox = browser.find_element_by_id("robotCheckbox")
option_checkbox.click()

option_radiobutton = browser.find_element_by_id("robotsRule")
option_radiobutton.click()

button.click()
assert True

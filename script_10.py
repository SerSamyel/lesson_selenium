from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.trollface")
button.click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

find_x = browser.find_element_by_id("input_value")
way_output = browser.find_element_by_id("answer")
way_output.send_keys(calc(find_x.text))

submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
submit_button.click()

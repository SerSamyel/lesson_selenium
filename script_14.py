from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

flag = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
button = browser.find_element_by_id("book")
button.click()
input_date = browser.find_element_by_id("input_value")
outbut_date = browser.find_element_by_id("answer")
outbut_date.send_keys(calc(input_date.text))
submit_button = browser.find_element_by_id("solve")
submit_button.click()

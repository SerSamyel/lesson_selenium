from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
num2 = browser.find_element_by_id("num2")


browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("[value='{0}']".format(str(int(num1.text) + int(num2.text)))).click()

browser.find_element_by_css_selector("button.btn.btn-default").click()

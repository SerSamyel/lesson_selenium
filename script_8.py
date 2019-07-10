from selenium import webdriver
import os 

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

firstname = browser.find_element_by_name("firstname")
firstname.send_keys("Bob")
lastname = browser.find_element_by_name("lastname")
lastname.send_keys("Smith")
email = browser.find_element_by_name("email")
email.send_keys("Bob.Smith@yhoo.com")
submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
file_button = browser.find_element_by_id("file")


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file_button.send_keys(file_path)

submit_button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Chrome()
# load the webpage
browser.get('https://www.amazon.in')
browser.maximize_window()
# get the input elements
input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")
input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()
#scraping part
products = []
for i in range(10):
    print('Scraping page', i+1)
    product = browser.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    for p in product:
        products.append(p.text)
    next_button = browser.find_element(By.XPATH, "//a[text()='Next']")
    next_button.click()
    sleep(2)
for i in products:
    print(i)

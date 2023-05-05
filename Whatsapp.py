from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://web.whatsapp.com/")

time.sleep(10)

chats = browser.find_elements_by_css_selector("._1hI5g._1XH7x._1VzZY")

for i in chats:

    if i.text == "Umut Oda Gönen":

        i.click()

        time.sleep(2)

        text_area = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for i in range(0, 1001):
            text_area.send_keys("Umut Sen Mal Mısın")
            time.sleep(0.2)
            text_area.send_keys(Keys.ENTER)
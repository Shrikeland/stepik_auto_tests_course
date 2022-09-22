import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
btn = browser.find_element(By.ID, "book").click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "solve").click()

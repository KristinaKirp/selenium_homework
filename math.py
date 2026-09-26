import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


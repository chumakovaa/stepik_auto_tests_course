from selenium import webdriver
import time
import math


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    button1 = driver.find_element_by_css_selector('[type="submit"]')
    button1.click()
    window_name = driver.window_handles[1]
    driver.switch_to.window(window_name)
    x_text = driver.find_element_by_id('input_value').text
    y = calc(x_text)
    input1 = driver.find_element_by_id('answer')
    input1.send_keys(y)
    button2 = driver.find_element_by_css_selector('[type="submit"]')
    button2.click()
    alert_text = driver.switch_to.alert.text
    print(alert_text.split(': ')[-1])
finally:
    driver.quit()
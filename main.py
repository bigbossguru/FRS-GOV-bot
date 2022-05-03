from time import sleep
from selenium import webdriver

URL = "https://frs.gov.cz/cs/ioff/application-status"

chromedriver_path = r"/usr/bin/chromedriver/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(chromedriver_path, options=options) as driver:
    driver.get(URL)

    input_app_num = driver.find_element_by_name("ioff_application_number")
    input_app_num_fake = driver.find_element_by_name("ioff_application_number_fake")
    input_app_code = driver.find_element_by_name("ioff_application_code")
    input_app_year = driver.find_element_by_name("ioff_application_year")

    input_app_num.send_keys("03735")
    sleep(0.5)
    input_app_num_fake.send_keys("3")
    sleep(0.5)
    input_app_code.send_keys("DP")
    sleep(0.5)
    input_app_year.send_keys("2022")

    sleep(1.0)
    button_op = driver.find_element_by_name("op")
    button_op.click()

    sleep(0.5)
    website_content = driver.find_element_by_class_name("alert")
    website_content.screenshot("visa.png")

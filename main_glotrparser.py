from selenium import webdriver
import random
from fake_useragent import UserAgent

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

# options
options = webdriver.ChromeOptions()

# change useragent
useragent = UserAgent()

options.add_argument(f"user-agent={random.choice(user_agents_list)}")

driver = webdriver.Chrome(
    executable_path="C:\Selenium drivers/chromedriver.exe",
    options=options
)

driver.get(
    "https://glotr.uz/gidravliceskoe-maslo-na-bezcinkovoj-osnove-total-equivis-af-4668-208l-p229300/"
)


def get_informations():
    try:
        site = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span[2]").text
        print(f"Company site is:", site)
    except Exception:
        print("No project site")

    try:
        name = driver.find_element_by_class_name("single-proposal-name").text
        print(f"1:", name)  # Названия товара
    except Exception:
        print("No project name")

    try:
        company_location = driver.find_element_by_class_name("single-comp-info").text
        print(f"2:", company_location)  # Адрес
    except Exception:
        print("No project location")

    try:
        price = driver.find_element_by_class_name("proposal-price-value").text
        print(f"3:", price)  # Цена
    except Exception:
        print("No project price")

    try:
        description = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div/div[1]/div[2]/div/div[1]/div").text.strip()
        print(f"4:", description)  # Описание
    except Exception:
        print("No project description")

    try:
        number_click = driver.find_element_by_class_name("show-number").click()
        driver.implicitly_wait(5)
        number_click2 = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/div/div[2]/span[2]").text
        print(f"5:", number_click2)  # Номер телефона
    except Exception:
        print("No project number")

    try:
        print(f"6:", driver.find_element_by_css_selector("div.slick-track > a").get_attribute('href'))  # Изображение
    except Exception:
        print("No project image")

    try:
        status = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/span").text
        print(f"7:", status)
    except Exception:
        print("No project status")

    try:
        company_name = driver.find_element_by_xpath(
            "/html/body/div[7]/div[2]/div/div/div[2]/div/div[1]/div[1]/a/span").text
        print(f"8:", company_name)
        driver.close()
        driver.quit()
    except Exception:
        print("No project company name")


get_informations()

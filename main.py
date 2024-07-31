from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
import requests as req

# __________________________REQUEST____________________________
web_link = "https://appbrewery.github.io/Zillow-Clone/"
form_link = "https://forms.gle/R2GQphLkTPLH98WU8"

responce = req.get(web_link)
html_content = responce.text

# __________________________BEAUTIFULLSOUP____________________________

soup = bs(html_content, 'html.parser')

title = soup.title.string
# selecting interested data
links = soup.select("a.property-card-link")
price = soup.select(".PropertyCardWrapper__StyledPriceLine")
address = soup.select(".StyledPropertyCard-c11n-8-84 address")

# cleaned and storing data in list
all_price = [money.text.strip("+/mo + 1bd") for money in price]
all_links = [link['href'] for link in links]
all_address = [add.text.strip().replace("|", "") for add in address]


# __________________________SELLINIUM____________________________
def upload_details(add: str, amount: str, link: str) -> None:
    driver.get(form_link)
    t.sleep(3)
    # t.sleep(3)
    input1 = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                 '1]/input')
    input1.send_keys(add)

    input2 = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                 '1]/input')
    input2.send_keys(amount)

    input3 = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                 '1]/input')
    input3.send_keys(link)

    form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    form.click()


# setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get(form_link)
# t.sleep(3)


for i in range(44):
    upload_details(all_address[i], all_price[i], all_links[i])

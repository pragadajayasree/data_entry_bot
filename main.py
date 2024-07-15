from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

url = "https://appbrewery.github.io/Zillow-Clone/"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}
response = requests.get(url=url, headers=header)
result = response.text

soup = BeautifulSoup(result, "lxml")

link = soup.select(".StyledPropertyCardPhotoBody a")
links = [i["href"] for i in link]
rate = soup.select(".PropertyCardWrapper__StyledPriceLine")
prices = []
for i in rate:
    prices.append(i.getText().replace(",", "").split("+")[0].split("/")[0])
add_ress = soup.select(".StyledPropertyCardDataWrapper address")
address = []
for i in add_ress:
    address.append(i.getText().strip())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


n = len(prices)
for i in range(n):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        url="https://docs.google.com/forms/d/e/1FAIpQLSedphABlBxceUp1a0_O_bD5y2m05jXkW-OPcWhsia1-mmvfaw/viewform?usp=sf_link")
    addr = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(3)
    addr.send_keys(address[i])
    time.sleep(1.5)
    pri = driver.find_element(by=By.XPATH,
                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pri.send_keys(prices[i])
    time.sleep(1.5)
    li_nk = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    li_nk.send_keys(links[i])
    time.sleep(1.5)
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    driver.quit()

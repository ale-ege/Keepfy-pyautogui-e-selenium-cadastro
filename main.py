#IMPORTAÇÃO DE BIBLIOTECAS
import selenium
import pyautogui
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df = pd.read_excel('MAN2.xlsx')
#print(df)
print(df.columns[:3])

#LISTA DE VARIAVEIS
link_login = 'https://app.keepfy.com/login'
link_cadastro = 'https://app.keepfy.com/general-registrations/products/create'
email = "alth@outlook.com.br"
senha = "Aa123456"

#LOGIN NO SITE
navegador = webdriver.Chrome(executable_path=r"C:chromedriver.exe")
navegador.get(url=link_login)
print(navegador.title)
sleep(2)

navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]").send_keys(email)
print("Email OK!")
sleep(1)

navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=password]").send_keys(senha)
print("Senha OK!")
sleep(1)

pyautogui.press('tab')
pyautogui.press('space')
print("Online!")
sleep(1)

navegador.find_element(by=By.CSS_SELECTOR, value=".MuiButton-fullWidth").click()
print("Enter clicado!")
sleep(2)


# CADASTRO DE ITENS
navegador.get(url=link_cadastro)
print("Acesso pagina de cadastro")
sleep(2)
#Clica em add material
navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/main/div[2]/div/div[11]/div').click()
sleep(1)

if len(navegador.find_elements(by=By.XPATH, value='/html/body/div[4]/div[3]/div/div[3]/div/div/button/span[1]')) != 0:
        sleep(2)
        navegador.find_element(by=By.XPATH, value='/html/body/div[4]/div[3]/div/div[3]/div/div/button/span[1]').click()
else:
        pass
print('propaganda ok')
sleep(2)

for i, material in enumerate(df['Material']):
        medida = df.loc[i, 'Unidade de Medida']
        custo = df.loc[i, 'Custo Unitário ']
        print(material)
        print(medida)
        print(custo)
        #Novo arquivo
        navegador.find_element(by=By.ID, value="add-materials").click()
        sleep(2)
        print('new material')
        #Inserir material
        navegador.find_element(by=By.ID, value="material-description").send_keys(material)
        print('material ok')
        sleep(2)
        pyautogui.press('tab')
        #Inserir custo
        navegador.find_element(by=By.NAME, value='standard-cost').send_keys(custo)
        print('custo ok')
        sleep(2)
        pyautogui.press('tab')
        #Inserir medida
        element = navegador.find_elements(by=By.CLASS_NAME, value='jss46')
        print(len(element))
        element[2].send_keys('un')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        print('medida ok')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')


print("Material cadastrado: {}, R${}, UN{}".format(material, custo, medida))

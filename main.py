#IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd
from openpyxl import load_workbook
from time import sleep
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)

#CONFIG NAVEGADOR
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(navegador, 30)

#LISTA DE VARIAVEIS
url_login = 'https://app.keepfy.com/login'
url_cadastro = 'https://app.keepfy.com/general-registrations/products/create'
email = "keepfymadesa@gmail.com"
senha = "*Md2020"

#GERAR DATAFRAME COM ITENS A SEREM CADASTRADOS
df = pd.read_excel('man.xlsx')
print(df)

#GERAR DATAFRAME COM ITENS CADASTRADOS
cad = pd.read_excel('data.xlsx')
print(cad)

#LOGIN NO SITE
navegador.get(url=url_login)
print(navegador.title)
locator = (By.CSS_SELECTOR, ".MuiButton-fullWidth")
wdw.until(
    presence_of_element_located(locator)
)
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]").send_keys(email)
sleep(0.5)
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=password]").send_keys(senha)
sleep(0.5)
pyautogui.press('tab')
pyautogui.press('space')
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiButton-fullWidth").click()

print("Login realizado!")

# CADASTRO DE ITENS
for i, material in enumerate(df['Material']):
    #Testa se o material já foi cadastrado
    if (material in (cad['Descriçăo'].values)):
        print("Material já cadastrado!")
        print(material)
    else:
        medida = 'Unidade (un)'
        custo = df.loc[i, 'Custo Unitário ']
        #Acesso a pagina de cadastro
        navegador.get(url=url_cadastro)
        locator2 = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div/div[11]/div')
        wdw.until(
            presence_of_element_located(locator2)
        )

        # Clica em add material
        navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/main/div[2]/div/div[11]/div').click()
        locator3 = (By.ID, "add-materials")
        wdw.until(
         presence_of_element_located(locator3)
        )
        #Novo material
        navegador.find_element(by=By.ID, value="add-materials").click()
        locator4 = (By.ID, "material-description")
        wdw.until(
         presence_of_element_located(locator4)
        )
        # Inserir material
        navegador.find_element(by=By.ID, value="material-description").send_keys(material)
        pyautogui.press('tab')
        # Inserir custo
        navegador.find_element(by=By.NAME, value='standard-cost').send_keys(custo)
        sleep(0.01)
        pyautogui.press('tab')
        # Inserir medida
        sleep(0.01)
        pyautogui.typewrite(medida)
        pyautogui.press('Enter')
        sleep(0.01)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('Enter')
        # Salvar material cadastrado em arquivo excel
        arquivo_excel = load_workbook(".\data.xlsx")
        planilha1 = arquivo_excel.active
        planilha1.append([material, custo, medida])
        arquivo_excel.save("data.xlsx")
        print("Novo material cadastrado: {}, R$ {}, {}".format(material, custo, medida))




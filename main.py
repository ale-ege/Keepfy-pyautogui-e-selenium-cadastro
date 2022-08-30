#IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd
import random
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

def login():
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wdw = WebDriverWait(navegador, 30)
    navegador.get(url="https://app.keepfy.com/login?")
    print(navegador.title)
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]").send_keys("keepfymadesa@gmail.com")
    sleep(0.5)
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=password]").send_keys("*Md2022")
    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('space')
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiButton-fullWidth").click()
    print("Login realizado!")
    sleep(0.5)

def cadastro():

    print("Leitura do banco de dados!")
    df = pd.read_excel('man.xlsx')
    cad = pd.read_excel('data.xlsx')
    print("Arquivos a cadastrar:")
    print(df)
    print("Arquivos já cadastrados:")
    print(cad)
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wdw = WebDriverWait(navegador, 30)
    navegador.get(url="https://app.keepfy.com/login?")
    print(navegador.title)
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]").send_keys(
        "keepfymadesa@gmail.com")
    sleep(0.5)
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=password]").send_keys("*Md2022")
    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('space')
    navegador.find_element(by=By.CSS_SELECTOR, value=".MuiButton-fullWidth").click()
    print("Login realizado!")
    sleep(0.5)

    for i, material in enumerate(df['Material']):
     # Testa se o material já foi cadastrado
        if (material in (cad['Descriçăo'].values)):
            print("Material já cadastrado!")
            print(material)
        else:
            medida = 'Unidade (un)'
            custo = df.loc[i, 'Custo Unitário ']
            # Acesso a pagina de cadastro
            sleep(random.uniform(0.12, 0.28))
            navegador.get(url="https://app.keepfy.com/general-registrations/products/create")
            wdw.until(presence_of_element_located(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div/div[11]/div')
                    )
            # Clica em add material
            navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/main/div[2]/div/div[11]/div').click()
            wdw.until(
                presence_of_element_located(By.ID, "add-materials")
                )
            # Novo material
            navegador.find_element(by=By.ID, value="add-materials").click()
            wdw.until(
                presence_of_element_located(By.ID, "material-description")
                )
            # Inserir material
            navegador.find_element(by=By.ID, value="material-description").send_keys(material)
            pyautogui.press('tab')
            # Inserir custo
            navegador.find_element(by=By.NAME, value='standard-cost').send_keys(custo)
            sleep(0.01)
            pyautogui.press('tab')
            # Inserir medida
            pyautogui.typewrite(medida)
            sleep(random.uniform(0.31, 0.55))
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
    run_forever()
    pass

def run_forever():
    try:
        while True:
            print("Looping do cadastro!")
            cadastro()
            sleep(30)
            raise Exception("Error simulated!")
    except Exception:
        print("Erro detectado. Reiniciando aplicação!")
        sleep(5)
        cadastro()

cadastro()
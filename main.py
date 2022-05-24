#IMPORTAÇÃO DE BIBLIOTECAS
import pyautogui
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Gerar dataframe apartir
df = pd.read_excel('MAN2.xlsx')
#print(df)
print(df.columns[:3])

#LISTA DE VARIAVEIS
link_login = 'https://app.keepfy.com/login'
link_cadastro = 'https://app.keepfy.com/general-registrations/products/create'
email = "keepfymadesa@gmail.com"
senha = "*Md2020"


#LOGIN NO SITE
navegador = webdriver.Chrome(executable_path=r"C:chromedriver.exe")
navegador.get(url=link_login)
print(navegador.title)
sleep(1.5)
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]").send_keys(email)
sleep(0.05)
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=password]").send_keys(senha)
sleep(0.15)
pyautogui.press('tab')
pyautogui.press('space')
navegador.find_element(by=By.CSS_SELECTOR, value=".MuiButton-fullWidth").click()
print("Enter clicado!")
sleep(1.5)


# CADASTRO DE ITENS
for i, material in enumerate(df['Material']):
        medida = 'Unidade (un)'
        custo = df.loc[i, 'Custo Unitário ']
        #Acesso a pagina de cadastro
        navegador.get(url=link_cadastro)
        sleep(2)
        # Clica em add material
        navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/main/div[2]/div/div[11]/div').click()
        sleep(2.75)
        #Novo arquivo
        navegador.find_element(by=By.ID, value="add-materials").click()
        sleep(2)
        # Inserir material
        navegador.find_element(by=By.ID, value="material-description").send_keys(material)
        sleep(0.05)
        pyautogui.press('tab')
        # Inserir custo
        navegador.find_element(by=By.NAME, value='standard-cost').send_keys(custo)
        sleep(0.05)
        pyautogui.press('tab')
        # Inserir medida
        sleep(0.05)
        pyautogui.typewrite(medida)
        pyautogui.press('Enter')
        sleep(0.05)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('Enter')
        sleep(2.75)
        print("Material cadastrado: {}, R${}, UN{}".format(material, custo, medida))
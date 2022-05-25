#IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook


#CONFIG NAVEGADOR
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


#LISTA DE VARIAVEIS
link_login = 'https://app.keepfy.com/login'
link_cadastro = 'https://app.keepfy.com/general-registrations/products/create'
email = "keepfymadesa@gmail.com"
senha = "*Md2020"
#caminho = '.\data.xlsx'


#GERAR DATAFRAME COM ITENS A SEREM CADASTRADOS
df = pd.read_excel('man.xlsx')
print(df)


#GERAR DATAFRAME COM ITENS CADASTRADOS
cad = pd.read_excel('data.xlsx')
print(cad)


#LOGIN NO SITE
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
print("Login realizado!")
sleep(1.5)


# CADASTRO DE ITENS

for i, material in enumerate(df['Material']):
    if (material in (cad['Descriçăo'].values)):
        print("Material já cadastrado!")
        print(material)
    else:
        medida = 'Unidade (un)'
        custo = df.loc[i, 'Custo Unitário ']
        #Acesso a pagina de cadastro
        navegador.get(url=link_cadastro)
        sleep(2)
        # Clica em add material
        navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/main/div[2]/div/div[11]/div').click()
        sleep(3.15)
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
        # Salvar material cadastrado em arquivo excel
        arquivo_excel = load_workbook(".\data.xlsx")
        planilha1 = arquivo_excel.active
        valores = [material, custo, medida]
        planilha1.append(valores)
        arquivo_excel.save("data.xlsx")
        # Salva material no dataframe de itens cadastrados
        #cad_new = pd.DataFrame({'Descrição': material, 'Custo': custo, 'Unidade': medida})
        #cad = pd.concat([cad, cad_new])
        sleep(2.75)
        print("Material cadastrado: {}, R$ {}, {}".format(material, custo, medida))




#IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)


url_login = 'https://app.keepfy.com/login'

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.get(url=url_login)
wdw = WebDriverWait(navegador, 30)

locator = (by=By.CSS_SELECTOR, value=".MuiInputBase-root input[name=email]")
wdw.until(
    presence_of_element_located(locator)
)
navegador.find_element(*locator)
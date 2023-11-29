import pywhatkit 
import keyboard
import time
from datetime import datetime
import pyautogui
import pandas as pd

mensagem = "teste okkk"
Planilha = 'Planilha1'
excel = 'teste.xlsx'

dados_excel = pd.read_excel(excel, sheet_name=Planilha)
coluna_contatos = dados_excel['Telefones']
lista_contatos = coluna_contatos.tolist()
print(lista_contatos)

for contato in lista_contatos:
    stringcontato = str(contato)
    stringcontato = ('+55'+stringcontato)
    pywhatkit.sendwhatmsg(stringcontato, mensagem, datetime.now().hour, datetime.now().minute + 1)
    time.sleep(20)
    pyautogui.press("enter")
    time.sleep(5)
    keyboard.press_and_release('ctrl + w')
    time.sleep(5)  
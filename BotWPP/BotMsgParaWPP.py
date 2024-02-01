"""
AutomaçãoPython para Wpp
"""
# Descrever os passos manuais e depois transformar isso em código
# Ler planilha e guardar informações sobre nome, telefone e data de vencimento

import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from time import sleep
import os 

webbrowser.open('https://web.whatsapp.com')
sleep(30)

workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
        #nome, telefone e data de vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f'Olá, {nome}! Seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.link_pagamento.com'
        # ^ Criar links personalizados do wpp e enviar mensagens para cada cliente com base nos dados da planilha
    
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
            # ^ https://web.whatsapp.com/send?phone='NUMERO'&text="TEXTO"
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta = pyautogui.locateCenterOnScreen('Seta.png')
        sleep(5)
            # ^ Deve procurar a imagem referente para poder clicar sobre ela e enviar a mensagem
        pyautogui.click(seta[0], seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('Erros.csv', 'a', newline='', enconding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}') 




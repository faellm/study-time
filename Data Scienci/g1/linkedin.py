from dados import url_link
from dados import email
from dados import password
from dados import *

from main import Noticia

from time import sleep


def Exec():

    driver.get(url_link)

    sleep(3)

    print('> Entrou no Chrome ! <')

    entrar = driver.find_element(By.ID, input_user)
    entrar.send_keys(email)

    sleep(1)

    senha = driver.find_element(By.ID, input_pass)
    senha.send_keys(password)

    buttun = driver. find_element(By.CLASS_NAME, btn_entrar)
    sleep(1)
    buttun.click()

    

def Public():

    #esta dando erro ao selecionar o btn de escrever publicação !!
    input_public = driver.find_element(By.CLASS_NAME, btn_publicacao)
    input_public.click()

    #incluir a noticia
    input_public.send_keys('teste de envio de mensagens! ')
    


Noticia()
Exec()
Public()






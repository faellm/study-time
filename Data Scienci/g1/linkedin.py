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


def Post ():

    driver.get('https://www.linkedin.com/in/rafael-lara-martins-668402157/overlay/create-post/')


def Public():

    print('parar de dar erro') #excluir
    #Escrever no Soup

    




Exec()
Noticia()
Post()
Public()






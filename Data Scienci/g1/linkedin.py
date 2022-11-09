from dados import url_link
from dados import email
from dados import password
from dados import *
from time import sleep

import requests
from bs4 import BeautifulSoup
from dados import url

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html')
news = soup.find('div', attrs={'class': 'feed-post-body'})
title = news.find('a', attrs={'class':'feed-post-link'})
print(title)


def Exec():

    driver.get(url_link)

    sleep(3)

    print('> Entrou no Chrome ! <')

    entrar = driver.find_element(By.ID, input_user)
    entrar.send_keys(email)

    sleep(3)

    senha = driver.find_element(By.ID, input_pass)
    senha.send_keys(password)

    buttun = driver. find_element(By.CLASS_NAME, btn_entrar)
    sleep(1)
    buttun.click()
    sleep(2)


def Post ():

    driver.get('https://www.linkedin.com/in/rafael-lara-martins-668402157/overlay/create-post/')
    sleep(3)


Exec()

Post()


##### PAROU AQUI #######

escrita = driver.find_element(By.XPATH, btn_public)
escrita.send_keys(title)    





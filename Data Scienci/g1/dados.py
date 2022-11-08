from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

#var do drive

driver = webdriver.Chrome('/Users/rafaellaramartins/Desktop/study time/Data Scienci/g1/chromedriver 2')

#email e senha
email = '' #seu email do Linkedin
password = '' #sua senha

#url para web sraping
url = 'https://g1.globo.com/'

#linkedin
url_link = 'https://www.linkedin.com/'


#id e class de componentes html

input_user = 'session_key' #id
input_pass = 'session_password' #id

btn_entrar = 'sign-in-form__submit-button' #class

btn_publicacao = {"method":"css selector","selector":".artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger"} #class



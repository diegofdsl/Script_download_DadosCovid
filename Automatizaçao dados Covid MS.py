
from selenium import webdriver
from time import sleep


navegador= webdriver.Chrome()
navegador.get('https://covid.saude.gov.br/')
navegador.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button').click()
sleep(60)
navegador.close()


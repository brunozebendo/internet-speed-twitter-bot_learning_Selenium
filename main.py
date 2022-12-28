"""A intenção do código é criar um bot para ler a velocidade da internet e postar um twitter marcando a operadora
caso a taxa esteja abaixo da contratada"""
"""Primeiro, as bibliotecas para lidar com o operador, para pressionar as teclas e para lidar com o tempo de espera"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""aqui, as variáveis constantes, as velocidades máxima e mínima contratadas, o caminho do chrome drive no computador
 e os dados para o login no twitter"""
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD

"""as três funções foram guardadas dentro de uma classe, a primeira é uma função para iniciar os construtores, como
 as outras duas funções vão usar os mesmos atributos, o caminho do webdriver e as velocidadas apuradas,
  aqui eles são instanciados (pelo que entendi)"""
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
"""Essa função vai pegar a velocidade da internet, primeiro vai usar a função self(se referindo a essa função).driver(se
referindo a variavel acima instanciado que aciona o webdriver).get(que é o comando para acessar o link)"""
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()
        # time.sleep(3)
"""Essa variável guarda o comando para achar o elemento pelo css_selector, nesse caso, o botão de start para começar a 
leitura da velocidade. Depois, a mesma variável é reaproveitada para passar o comando de click, ou seja, após achar o 
elemento, a variável usa a função interna click(). Então, o time.sleep faz o sistema esperar 60 segundos pela leitura 
da velocidade. Por fim, as variáveis acham o elemento com o número da velocidade lida através do caminho xpath"""
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
"""A função abaixo faz o caminho necessário para ir até o twitter, esperar dois segundos, achar o elemento de e-mail e 
senha, depois passar o endereço e a senha (passados nas variáveis constantes), espera mais dois segundos, e pressiona o
 enter, espera mais cinco segundos, acha o botão para postar, o tweet é a mensagem com o texto padrão e com as variáveis
 obtidas da velocidade, o send_keys então guarda a mensagem do tweet, mais 3 segundos, então acha o elemento do botão de
 tweet e clica no botão, mais dois segundos e sai do programa"""
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

"""aqui é o comando para iniciar as funções"""
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
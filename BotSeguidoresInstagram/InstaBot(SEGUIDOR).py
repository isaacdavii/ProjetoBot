from selenium import webdriver
    # ^ selenium quem faz automação de cliques, abrir pag e afins
from selenium.webdriver.common.keys import Keys 
    # ^ usa partes do teclado
import time
    # ^ regrar tempo para "humanizar" o programa 
    
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"DIRETÓRIO DE USO: geckodriver.exe")

    # xpath é uma informação única que identifica o campo 
    # //a[@href='caminho referente login']
    # //input[@name='username']
    # //input[@name='password']
    
    def login(self):
        driver = self.driver 
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        login_button = driver.find_element_by_xpath('XPATH DO LOGIN')
        login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user.element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('TAG DESEJADA')
        
def curtir_fotos(self, hashtag):
    driver = self.driver 
    driver.get('https://www.instagram.com/explor/tags/' + hashtag + '/')
    time.sleep(5) 
    for c in range(1, 5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    hrefs = driver.find_elements_by_tag_name('a')
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
    [href for href in pic_hrefs if hashtag in href]
    print(hashtag + ' fotos: ' + str(len(pic_hrefs))) 
        # ^ visualizar pra ver o que ele está fazendo e quantas imagens ele encontrou
    
    for pic_href in pic_hrefs:
        driver.get(pic_href) 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # ^ a gente puxa a página a fim de carregar todo o conteúdo e não ter problemas de carregamento
        try:
            driver.find_element_by_class_name('//button[@class="INSPECIONAR BOTAO DE CURTIR]"').click()
            time.sleep(19)
            # ^ usa-se esse tempo médio para Insta não reconhecer o bot
            # + atenção: o MAX de curtidas diárias é +- 200
        except Exception as e:
            time.sleep(5)
        
ProjetoBot = InstagramBot('UserTeste','SenhaTeste')
ProjetoBot.login()

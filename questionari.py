import getpass
import os
import selenium
import time
import io
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://unicatt.esse3.cineca.it/auth/studente/QuestAdLibrettoValDid.do'

username = input('Enter your username: ')
password = getpass.getpass(prompt='Enter your password: ')



driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver.maximize_window()
action = ActionChains(driver) 

#goes to website-questionari
driver.get(url)

time.sleep(3)

#login into site-questionari
username_site = driver.find_element_by_id("mat-input-1")
username_site.send_keys(username)

password_site = driver.find_element_by_id("mat-input-0")
password_site.send_keys(password)

password_site.send_keys(Keys.ENTER)

time.sleep(10)

#find all href
quests_list = []
quests = driver.find_elements_by_tag_name("a")
for i in quests:
	quests_list.append(i.get_attribute("href"))

#remove href that are not questionari + teologia + verde
quests_list.remove('https://www.wikihow.com/Enable-Cookies-and-JavaScript')
quests_list.remove('https://unicatt.esse3.cineca.it/InformativaCookie.do')
quests_list.remove('https://unicatt.esse3.cineca.it/#maincontent')
quests_list.remove('https://unicatt.esse3.cineca.it/#menuprincipale')
quests_list.remove('https://unicatt.esse3.cineca.it/#main-navigation')
quests_list.remove('https://unicatt.esse3.cineca.it/#menusecondario')
quests_list.remove('https://unicatt.esse3.cineca.it/#focus-secondario')
quests_list.remove('https://unicatt.esse3.cineca.it/Redirect.do?parconfurl=LAYOUT_HEADER_URL_0')
quests_list.remove('https://unicatt.esse3.cineca.it/#shortcut')
quests_list.remove('https://unicatt.esse3.cineca.it/InformativaCookie.do')
quests_list.remove('')

#teologia
quests_list.remove('https://unicatt.esse3.cineca.it/auth/questionari/QuestionariWrapperAdLibrettoValDid.do?evento_comp_cod=EV_VAL_DID&adsce_id=5465605')

#verde

#accetta cookies
driver.find_element_by_id(
"cookiesConferma"
).click()

#start loop materie
for e in (quests_list):
    driver.get(e)

    time.sleep(2)

#start loop professori
    #find all href

    prof_list = []
    profs = driver.find_elements_by_tag_name("a")
    for p in profs:
	    prof_list.append(p.get_attribute("href"))

    
    #remove href that are not prof
    prof_list.remove('https://www.wikihow.com/Enable-Cookies-and-JavaScript')
    prof_list.remove('https://unicatt.esse3.cineca.it/InformativaCookie.do')
    prof_list.remove('https://unicatt.esse3.cineca.it/#maincontent')
    prof_list.remove('https://unicatt.esse3.cineca.it/#menuprincipale')
    prof_list.remove('https://unicatt.esse3.cineca.it/#main-navigation')
    prof_list.remove('https://unicatt.esse3.cineca.it/#menusecondario')
    prof_list.remove('https://unicatt.esse3.cineca.it/#focus-secondario')
    prof_list.remove('https://unicatt.esse3.cineca.it/Redirect.do?parconfurl=LAYOUT_HEADER_URL_0')
    prof_list.remove('https://unicatt.esse3.cineca.it/#shortcut')
    prof_list.remove('https://unicatt.esse3.cineca.it/auth/studente/QuestAdLibrettoValDid.do')
    prof_list.remove('https://unicatt.esse3.cineca.it/InformativaCookie.do')
    prof_list.remove('')

    for v in (prof_list):
        driver.get(v)
        time.sleep(2)

    #inizia nuova compilazione
        driver.find_element_by_id("quest_ab_compilazione_edit").click()

        time.sleep(2)

        #try except block
        try:
        
        #identify element
            skip = driver.find_element_by_id("quest_domanda_selection_140402")
            driver.find_element_by_id("quest_domanda_selection_140402").click()
            
            driver.find_element_by_id(
                "quest_sbmSuccessivo"
            ).click()
            time.sleep(2)

            driver.find_element_by_id("quest_btn_conferma_riepilogo").click()
            time.sleep(2)

        #elif corso or not (da fare next time)

        #if skip false
        #compile questionario (obbligatorio)
        except NoSuchElementException:
            driver.find_element_by_id(
            "quest_domanda_selection_139521"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139574"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139621"
            ).click()

            driver.find_element_by_id(
            "quest_sbmSuccessivo"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139741"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139791"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139841"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139891"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139941"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_139991"
            ).click()

            driver.find_element_by_id(
            "quest_sbmSuccessivo"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_140172"
            ).click()

            driver.find_element_by_id(
            "quest_sbmSuccessivo"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_140221"
            ).click()

            driver.find_element_by_id(
            "quest_sbmSuccessivo"
            ).click()

            driver.find_element_by_id(
            "quest_domanda_selection_140311"
            ).click()

            driver.find_element_by_id(
            "quest_sbmSuccessivo"
            ).click()

            driver.find_element_by_id(
            "quest_btn_conferma_riepilogo"
            ).click()

            time.sleep(2)

    prof_list.clear()

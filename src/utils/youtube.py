import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Title_description import Description_func, Title_func, IMAGE_FOLDER
from time import sleep
import pyautogui


browser = uc.Chrome(use_subprocess=True)


def login_email(email, password):
    browser.get('https://accounts.google.com/v3/signin/identifier?dsh=S521003731%3A1662917074677067&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=pt-BR&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWot_an_NVHpGTlXHzfCMrxsvfModWCvtZZbkiJuIIzPTFkoqma59gYkY3F9PL9HHXTI5tF4Dg')

    browser.maximize_window()
    input_email = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, 'identifierId')))
    input_email.send_keys(email)
    input_email.send_keys(Keys.ENTER)

    input_senha = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.NAME, 'Passwd')))
    input_senha.send_keys(password)
    input_senha.send_keys(Keys.ENTER)


def open_youtube_transmition_config():
    input_live_icon = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon')))
    input_live_icon.click()

    input_live_text = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')))
    input_live_text.click()

def edit_youtube_transmition():
    input_button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[1]/ytls-live-control-room-renderer/div[1]/div[1]/div/ytls-broadcast-metadata/div[2]/ytcp-button')))
    input_button.click()

    sleep(5)
    input_title = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, 'textbox')))
    input_title.send_keys(Keys.CONTROL + 'a')
    input_title.send_keys(f'{Title_func()}')
    
    input_description = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/ytls-broadcast-edit-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-navigation/div[2]/iron-pages/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')))
    input_description.send_keys(Keys.CONTROL + 'a') 
    input_description.send_keys(f'{Description_func()}')

    sleep(2)
    input_thumb = browser.execute_script('document.getElementsByClassName("options style-scope ytcp-thumbnails-compact-editor-uploader-old")[0].click()')
    
    input_change = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/div/div/yt-formatted-string')))
    input_change.click()

    pyautogui.moveTo(349, 43)
    sleep(2)
    pyautogui.mouseDown()
    sleep(2)
    pyautogui.write(IMAGE_FOLDER)
    pyautogui.press('enter')
 
    input_save = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/ytls-broadcast-edit-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]/div')))
    input_save.click()

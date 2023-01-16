from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://accounts.google.com/v3/signin/identifier?dsh=S521003731%3A1662917074677067&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=pt-BR&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWot_an_NVHpGTlXHzfCMrxsvfModWCvtZZbkiJuIIzPTFkoqma59gYkY3F9PL9HHXTI5tF4Dg')

    # sleep(10)
    # input_element = browser.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/a')
    # input_element.click()
    sleep(3)
    input_email = browser.find_element(By.ID, 'identifierId')
    input_email.send_keys('comunidadecristamaranatamkt@gmail.com')
    sleep(1)
    input_email.send_keys(Keys.ENTER)
    sleep(1)
    input_senha = browser.find_element(By.NAME, 'Passwd')
    input_senha.send_keys('Maranata2020')
    sleep(1)
    input_senha.send_keys(Keys.ENTER)
    sleep(5)
    input_live_icon = browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon')
    sleep(5)
    input_live_icon.click()
    sleep(5)
    input_live_text = browser.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')
    sleep(5)
    input_live_text.click()
    sleep(10)
    input_edit_button = browser.find_element(By.ID, 'edit-button')
    sleep(5)
    input_edit_button.click
    sleep(10)
    input_title = browser.find_element(By.ID, 'textbox')
    sleep(2)
    input_title.send_keys('Culto de Hoje')

    browser.quit()

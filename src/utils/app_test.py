from time import sleep
from youtube import *

email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

if __name__ == '__main__':


    # Code
    login_email(email, password)
    
    open_youtube_transmition_config()

    sleep(10)

    edit_youtube_transmition()

    exit = ''
    while exit != 'exit()':
        exit = input("Digite 'exit()' para fechar o programa: ")

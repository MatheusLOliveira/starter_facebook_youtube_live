# import pyautogui
# from time import sleep

# sleep(4)
# print(pyautogui.position())esa

# import calendar

# c = calendar.Calendar(firstweekday=calendar.SUNDAY)

# year = 2022; month = 9

# monthcal = c.monthdatescalendar(year,month)
# third_friday = [day for week in monthcal for day in week if \
#                 day.weekday() == calendar.FRIDAY and \
#                 day.month == month][2]

# print(third_friday.day)

import os

ROOT_FOLDER = os.getcwd()
DESCRIPTION_FOLDER = os.path.join(ROOT_FOLDER, r'src', r'utilities', r'descriptions')

if __name__ == '__main__':
    print('________________________________________________')
    print(os.path.join(DESCRIPTION_FOLDER, r'default.txt'))
    print(r'C:\Users\mathe\OneDrive\Documentos\ws\live_selium\src\utilities\descriptions\default.txt')
    print('________________________________________________')
    print(os.path.join(DESCRIPTION_FOLDER, r'domingo.txt'))
    print(r'C:\Users\mathe\OneDrive\Documentos\ws\live_selium\src\utilities\descriptions\domingo.txt')
    print('________________________________________________')
    print(os.path.join(DESCRIPTION_FOLDER, r'quinta-feira.txt'))
    print(r'C:\Users\mathe\OneDrive\Documentos\ws\live_selium\src\utilities\descriptions\quinta-feira.txt')
    print('________________________________________________')
    print(os.path.join(DESCRIPTION_FOLDER, r'encontro_mulheres.txt'))
    print(r'C:\Users\mathe\OneDrive\Documentos\ws\live_selium\src\utilities\descriptions\encontro_mulheres.txt')
    print('________________________________________________')
    print(os.path.join(DESCRIPTION_FOLDER, r'culto_jovens.txt'))
    print(r'C:\Users\mathe\OneDrive\Documentos\ws\live_selium\src\utilities\descriptions\culto_jovens.txt')
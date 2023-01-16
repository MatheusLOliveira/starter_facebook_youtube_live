from datetime import datetime
from pathlib import Path

import os
import calendar


dt = datetime.now()

FORMATTING = dt.strftime('%d/%m/%Y')
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESCRIPTION_FOLDER = os.path.join(ROOT_FOLDER, r'utilities', r'descriptions')
IMAGE_FOLDER = os.path.join(ROOT_FOLDER, r'utilities', r'thumb', r'thumb.JPG')
print(DESCRIPTION_FOLDER)

value = ""
index_day = dt.weekday()
day = dt.day
month = dt.month
year = dt.year

home = Path.home()
documents = home / 'Documentos'

c = calendar.Calendar(firstweekday=calendar.SUNDAY)
monthcal = c.monthdatescalendar(year, month)

third_saturday = [day for week in monthcal for day in week if \
                day.weekday() == calendar.SATURDAY and \
                day.month == month][2]

first_saturday = [day for week in monthcal for day in week if \
                day.weekday() == calendar.SATURDAY and \
                day.month == month][0]


def Description_func():
    description_day = os.path.join(DESCRIPTION_FOLDER, r'default.txt')

    if Day_of_weekend() == 'Domingo':
        description_day = os.path.join(DESCRIPTION_FOLDER, r'domingo.txt')
    elif Day_of_weekend() == 'Quinta-Feira':
        description_day = os.path.join(DESCRIPTION_FOLDER, r'quinta-feira.txt')
    elif day == first_saturday.day:
        description_day = os.path.join(DESCRIPTION_FOLDER, r'encontro_mulheres.txt')
    elif day == third_saturday.day:
        description_day = os.path.join(DESCRIPTION_FOLDER, r'culto_jovens.txt')

    with open(description_day, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()


def Title_func():
    if Day_of_weekend() == 'Domingo':
        if dt.hour < 12:
            service = 'Manhã'
        else:
            service = 'Noite'
        return f'Culto de {Day_of_weekend()} - {service} - {FORMATTING}'
    elif Day_of_weekend() == 'Quinta-Feira':
        return f'Culto de {Day_of_weekend()} - {FORMATTING}'
    
    return f'Culto de {Day_of_weekend()} - {FORMATTING}'


def Day_of_weekend():
    DAYS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]

    
    day_of_weekend = DAYS[index_day]
    return day_of_weekend


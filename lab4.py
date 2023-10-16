import time
import random

events_database = {
    2001: 'Відкриття космічної станції "Міжнародна космічна станція"',
    2004: 'Укладення Європейської Конституції',
    2007: 'Впровадження iPhone в продаж',
    2015: 'Домашній тестований запуск Falcon Heavy від SpaceX',
    2020: 'Початок пандемії COVID-19'
}

time_travel_years = [2001, 2007, 2015, 2022]

def add_event(year, event_description):
    events_database[year] = event_description
    print(f'Подія для року {year} додана у базу даних.')

def delete_event(year):
    if year in events_database:
        del events_database[year]
        print(f'Подія для року {year} видалена з бази даних.')
    else:
        print(f'Подія для року {year} відсутня у базі даних.')

def show_events():
    for year, event in events_database.items():
        print(f'Рік {year}: {event}')

def time_machine():
    print('Ви відправляєтеся в подорож у часі!')
    time.sleep(1)
    print('*Тик-так, тик-так, тик-так*')
    
    for i, year in enumerate(time_travel_years, 1):
        event = events_database.get(year)
        if event is not None:
            print(f'{i}. У {year} році сталася подія:')
            print(event)
        else:
            print(f'{i}. У {year} році подія відсутня.')
            time.sleep(1)
            print('Перевірка статусу машини часу...')
            time.sleep(1)
            print('Статус стабільний, продовжуємо роботу!')

while True:
    print('\nВиберіть опцію:')
    print('1. Додати подію до бази даних')
    print('2. Видалити подію з бази даних')
    print('3. Показати події')
    print('4. Додати рік до подорожі в часі')
    print('5. Видалити рік з подорожі в часі')
    print('6. Відправитися в подорож у часі')
    print('7. Завершити програму')

    choice = input('Введіть ваш вибір: ')
    
    if choice == '1':
        year = int(input('Введіть рік події: '))
        event_description = input('Опишіть, що сталося: ')
        add_event(year, event_description)
    
    elif choice == '2':
        year = int(input('Введіть рік події, яку хочете видалити: '))
        delete_event(year)
    
    elif choice == '3':
        show_events()
    
    elif choice == '4':
        year = int(input('Введіть рік для подорожі в часі: '))
        time_travel_years.append(year)
    
    elif choice == '5':
        year = int(input('Введіть рік, який хочете видалити з подорожі в часі: '))
        if year in time_travel_years:
            time_travel_years.remove(year)
        else:
            print(f'Рік {year} вже відсутній у списку подорожі.')
    
    elif choice == '6':
        time_machine()
    
    elif choice == '7':
        print('Завершую програму...')
        time.sleep(1)
        break

def weekend_search(day: int, days_of_the_week={1: 'Monday',
                                               2: 'Tuesday',
                                               3: 'Wednesday',
                                               4: 'Thursday',
                                               5: 'Friday',
                                               6: 'Saturday',
                                               7: 'Sunday'}):
    try:
        day = int(input('Введите день недели от 1 до 7: '))
        if 1 <= day <= 5:
            print(f'{day} это {days_of_the_week.values(day)}')
        print(f'{day} это {days_of_the_week.values(day)}')
    except ValueError:
        print('Введенные данные не соответствуют входным!\n'
              'Пожалуйста повторите ввод.')
        return weekend_search()



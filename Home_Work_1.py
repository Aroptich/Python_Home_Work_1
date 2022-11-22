def weekend_search(days_of_the_week={1: 'Понедельник',
                                     2: 'Вторник',
                                     3: 'Среда',
                                     4: 'Четверг',
                                     5: 'Пятница',
                                     6: 'Суббота',
                                     7: 'Воскресенье'}):
    try:
        day = int(input('Введите день недели от 1 до 7: '))
        if 1 <= day <= 5:
            print(f'Печаль! {days_of_the_week[day]}. К сожелению это рабочий день ')
        else:
            print(f'Ура! {days_of_the_week[day]}! Выходной!')
    except ValueError:
        print('Введенные данные не соответствуют входным!\n'
              'Пожалуйста повторите ввод.')
        print('-' * 40)
        return weekend_search()
    except  KeyError:
        print('Дней в недели только 7!\n'
              'Пожалуйста повторите ввод.')
        print('-' * 40)
        return weekend_search()


weekend_search()

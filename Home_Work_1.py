
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
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
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def Number_of_combinations():
    array = []
    # Количество позиций
    l = 2
    # Колчество цифр в комбинации
    n = 3
    count = 0
    while l ** n != count:
        temp_list = []
        X = random.randint(0, 1)
        Y = random.randint(0, 1)
        Z = random.randint(0, 1)
        temp_list.append(X)
        temp_list.append(Y)
        temp_list.append(Z)
        if temp_list not in array:
            array.append(temp_list)
            count += 1

    return array


a = Number_of_combinations()
b = a.copy()


def truth_test():
    count = 0
    for X1, Y1, Z1 in b:
        for X2, Y2, Z2 in b[count::]:
            left_side = not (X1 or Y1 or Z1)
            right_side = not X2 and not Y2 and not Z2
            result = left_side == right_side
            if result == True:
                print(f'not({X1} or {Y1} or {Z1}) = not {X2} and not {Y2} and not {Z2} -> True')
            else:
                print(f'not({X1} or {Y1} or {Z1}) = not {X2} and not {Y2} and not {Z2} -> False')
        print('-' * 60)
        count += 1


print(truth_test())
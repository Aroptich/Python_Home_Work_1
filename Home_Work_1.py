# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# # является ли этот день выходным.
# def weekend_search(days_of_the_week={1: 'Понедельник',
#                                      2: 'Вторник',
#                                      3: 'Среда',
#                                      4: 'Четверг',
#                                      5: 'Пятница',
#                                      6: 'Суббота',
#                                      7: 'Воскресенье'}):
#     try:
#         day = int(input('Введите день недели от 1 до 7: '))
#         if 1 <= day <= 5:
#             print(f'Печаль! {days_of_the_week[day]}. К сожелению это рабочий день ')
#         else:
#             print(f'Ура! {days_of_the_week[day]}! Выходной!')
#     except ValueError:
#         print('Введенные данные не соответствуют входным!\n'
#               'Пожалуйста повторите ввод.')
#         print('-' * 40)
#         return weekend_search()
#     except  KeyError:
#         print('Дней в недели только 7!\n'
#               'Пожалуйста повторите ввод.')
#         print('-' * 40)
#         return weekend_search()
#
#
# weekend_search()
#
#
# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# def Number_of_combinations():
#     array = []
#     # Количество позиций
#     l = 2
#     # Колчество цифр в комбинации
#     n = 3
#     count = 0
#     while l ** n != count:
#         temp_list = []
#         X = random.randint(0, 1)
#         Y = random.randint(0, 1)
#         Z = random.randint(0, 1)
#         temp_list.append(X)
#         temp_list.append(Y)
#         temp_list.append(Z)
#         if temp_list not in array:
#             array.append(temp_list)
#             count += 1
#
#     return array
#
#
# a = Number_of_combinations()
# b = a.copy()
#
#
# def truth_test():
#     count = 0
#     for X1, Y1, Z1 in b:
#         for X2, Y2, Z2 in b[count::]:
#             left_side = not (X1 or Y1 or Z1)
#             right_side = not X2 and not Y2 and not Z2
#             result = left_side == right_side
#             if result == True:
#                 print(f'not({X1} or {Y1} or {Z1}) = not {X2} and not {Y2} and not {Z2} -> True')
#             else:
#                 print(f'not({X1} or {Y1} or {Z1}) = not {X2} and not {Y2} and not {Z2} -> False')
#         print('-' * 60)
#         count += 1
#
#
# print(truth_test())
#
#
# # Напишите программу, которая принимает на вход координаты точки (X и Y),
# # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# def plane_quarter_number():
#     try:
#         while True:
#             # Координаты точки 'X'
#             x = float(input('Введите координаты точки X: '))
#             # Координаты точки 'Y'
#             y = float(input('Введите координаты точки Y: '))
#             if x != 0 and y != 0:
#                 if x > 0 and y > 0:
#                     print('1')
#                 elif x < 0 and y > 0:
#                     print('2')
#                 elif x < 0 and y < 0:
#                     print('3')
#                 else:
#                     print('4')
#             break
#
#     except ValueError:
#         print('Вводимые значения X и Y должны быть либо целыми числами, либо числами с плавающей точкой!')
#         print('Повторите ввод')
#         return plane_quarter_number()
#
#
# plane_quarter_number()
#
#
# # Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y)
# def finding_an_interval_along_a_quarter_plane():
#     try:
#
#         number_quater = int(input('Введите номер четверти от 1 до 4: '))
#         if number_quater == 1:
#             print(f'Диапазон возможных координат: X=({0};+{chr(8734)}), Y=({0};+{chr(8734)})')
#         elif number_quater == 2:
#             print(f'Диапазон возможных координат: X=({0};-{chr(8734)}), Y=({0};+{chr(8734)})')
#         elif number_quater == 3:
#             print(f'Диапазон возможных координат: X=({0};-{chr(8734)}), Y=({0};-{chr(8734)})')
#         elif number_quater == 4:
#             print(f'Диапазон возможных координат: X=({0};+{chr(8734)}), Y=({0};-{chr(8734)})')
#         else:
#             print(f'Четверть под номером {number_quater} не существует!')
#             print('Повторите ввод данных')
#             return finding_an_interval_along_a_quarter_plane()
#     except ValueError:
#         print("Вводимый номер четверти должен быть целым числом и равным от 1 до 4")
#         print("Повторите ввод данных")
#         return finding_an_interval_along_a_quarter_plane()
#
#
# finding_an_interval_along_a_quarter_plane()


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# def distance_between_two_points(N=2):
#     point_A_coordinate = [random.randint(-10, 10) for _ in range(N)]
#     point_B_coordinate = [random.randint(-10, 10) for _ in range(N)]
#     return round(math.sqrt((point_A_coordinate[0] - point_A_coordinate[1]) ** 2 +
#                            (point_B_coordinate[0] - point_B_coordinate[1]) ** 2), 2)
#
#
# print(distance_between_two_points())


s = "Hello World"
a = "Hel"
if s.startswith(a):
    print(s.replace(a, ''))
print(s)
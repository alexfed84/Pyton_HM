#6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
a = int(input('Введите номер дня недели '))
if a == 1: print('Понедельник. Не является выходным днем')
elif a == 2: print('Вторник. Не является выходным днем')
elif a == 3: print('Среда. Не является выходным днем')
elif a == 4: print('Четверг. Не является выходным днем')
elif a == 5: print('Пятница. Не является выходным днем')
elif a == 6: print('Суббота. Является выходным днем')
elif a == 7: print('Воскресенье. Является выходным днем')
else: print('Введите число, соответствующее дню недели')

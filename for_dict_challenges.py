from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list_st = []
for name in students:
    if name['first_name'] in list_st:
        continue
    else:
        list_st.append(name['first_name'])
        print(f"{name['first_name']}: {students.count(name)}")

#var2
names = [person['first_name'] for person in students]
ctr = Counter(names)
for name, count in ctr.items():
    print(f"{name}: {count}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_st = ''
quantity = 0
list_st = []
for name in students:
    if name['first_name'] in list_st:
        continue
    else:
        list_st.append(name['first_name'])
        if students.count(name) > quantity:
            quantity = students.count(name)
            name_st = name['first_name']

print(f"Самое частое имя среди учеников: {name_st}")
#var2
names = [person['first_name'] for person in students]
ctr = Counter(names)
print(f'Самое частое имя среди учеников: {max(ctr, key=ctr.get)}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for cl in school_students:
    name_st = ''
    quantity = 0
    list_st = []
    for name in cl:
        if name['first_name'] in list_st:
            continue
        else:
            list_st.append(name['first_name'])
            if cl.count(name) > quantity:
                quantity = cl.count(name)
                name_st = name['first_name']

    print(f"Самое частое имя в классе {int(school_students.index(cl)) + 1}: {name_st}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for i in range(len(school)):
    male = 0
    female = 0
    for j in range(len(school[i]['students'])):
        if is_male[school[i]['students'][j]['first_name']] is True:
            male += 1
        else:
            female += 1
    print(f'Класс {school[i]["class"]}: девочки {female}, мальчики {male}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_male = 0
max_female = 0
for i in range(len(school)):
    male = 0
    female = 0
    for j in range(len(school[i]['students'])):
        if is_male[school[i]['students'][j]['first_name']] is True:
            male += 1
        else:
            female += 1
    if male > max_male:
        max_male = male
    else:
        print(f'Больше всего мальчиков в классе {school[i - 1]["class"]}\nБольше всего девочек в классе {school[i]["class"]}')



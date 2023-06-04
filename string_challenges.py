# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове "{word}": "{word[-1]}"')

# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
# var1
for i in word:
    if i == 'а':
        count += 1
print(f'Количество букв "а" в слове {word}: {count}')
#var2
count = 0
for i in word:
    if i.lower() == 'а':
        count += 1
print(f'Количество букв "а" в слове {word}: {count}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for char in word:
    if char in "аеёиоуыэюяАЕЁИОУЫЭЮЯ":
        count += 1
print("Количество гласных букв:", count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении "{sentence}": {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
l = sentence.split()
count = 0
for i in l:
    count += len(i)
print(f'Усреднённая длина слова в предложении: {count/len(l)}')

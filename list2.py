# Методы списков
# print(dir[])
lst = []
"""
lst.append(1)
lst.append(2)
"""

for i in range(1, 11):
    lst.append(i)
lst2 = [11, 12]

# res = lst.extend(lst2) # что так что так строчкой 16 написано сложение будет
print(lst + lst2)

res = lst + lst2 + [13, 14]

res.extend('Привет')  # В отличие от "+" преобразовывает "на лету"
res.extend({1, 2, 3})

print(res)
print(f'Длинна итогового списка - {len(res)}')

res.insert(2, 2.5)

# Срезы такие же, как и для строки
print(res[:5])  # До 5-го элемента

# Удаление
res.remove(2.5)  # Удаляет если есть, или ошибка # Ничего ен возвращает
res.pop()  # Удаляет последний элемент и возвращает его (или по индексу)
print(res)

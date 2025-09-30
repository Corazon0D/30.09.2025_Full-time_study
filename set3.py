# Операции с двумя множествами
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3}

# Объединение (union)
# union = my_set1.union(my_set2)
union = my_set1 | my_set2
print(union)

# Пересечения (общие элементы для 2-х множеств)
# intersection = my_set1.intersection(my_set2)
intersection = my_set1 & my_set2
print(intersection)

# Разность множеств (элементы, которые есть в 1-ом, но нет во 2-м)
# difference = my_set1.difference(my_set2)
difference = my_set1 - my_set2
print(difference)

# Симметричная разность (все элементы, которые есть только в одном
symm_diff = my_set1.symmetric_difference(my_set2)
print(symm_diff)

# Сравнение множеств
if my_set1 == my_set2:
    print("Множества идентичны")
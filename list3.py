# Список (имитация стека)
stack = []
sheet = 'Простыня_'
for i in range(5):
    stack.append(f'Простыня_{i + 1}')
print('Наполняем стек:')
for item in stack:
    print(item)

print('Удаляем стек:')
while stack:  # Пока список не пустой
    print(stack.pop())

# ["Простыня 1", "Простыня 2", "Простыня 3", "Простыня 4", "Простыня 5"

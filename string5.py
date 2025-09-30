# F-строка

name = "Дмитрий"
surname = "Дмитриев"

my_slise = name[3:]
# string = f"Привет, {name} {surname}!"
print(f'Привет, {name} {surname}!')
#print(dir(""))
#print(help("".find))

print(name.index('тр'))

if 'тр' in name:
    print(f'вхождение "тр" есть в строке "{name}"') # вхождение "тр" есть в строке "Дмитрий"

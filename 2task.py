phonebook = {}
for i in range(0, 5):
    name, phone = input('Введите имя и телефон через пробел:').split()
    phonebook[name] = phone

for (item) in (phonebook):
    print(item, phonebook[item])

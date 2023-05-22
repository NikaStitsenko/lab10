import json

'''Имеется файл JSON с информацией о продуктах
Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде:
Название: Шоколад
Цена: 50
Вес: 100
В наличии'''

def lab1():
    with open("1.json", "r") as file:
        data = json.load(file)

    for i in data["products"]:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")

'''Модифицируйте программу 10.1 – добавьте в нее код, который добавляет данные в файл JSON (спрашивает их у пользователя) 
и потом также выводить содержимое итогового файла на экран.'''

def lab2():
    k = int(input("Введите количество товаров для добавления: "))

    products = {"products": []}
    for i in range(k):
        name = input("Название: ")
        price = int(input("Цена: "))
        weight = int(input("Вес: "))
        available = bool(input("В наличии 0/1: "))
        products["products"].append({"name": name, "price": price, "weight": weight, "available": available})

    with open("1.json", "r") as file:
        data = json.load(file)

    data["products"].extend(products["products"])

    for i in data["products"]:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")

    with open("1.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

'''Создание русско-английского словаря.
Имеется файл en-ru.txt, в котором находятся строки англо-русского словаря в таком формате:
cat - кошка
dog - собака
Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в таком формате:
делать – to do
дом – home
домашняя папка – home
строки в выходном файле нужно отсортировать по алфавиту'''

def lab3():
    d = {}
    with open("en-ru.txt", "r") as file:
        for line in file:
            en_w = line.split("-")[0].strip()
            ru_ws = line.split("-")[1].strip().split(',')
            for i in ru_ws:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + en_w
                else:
                    d[i] = en_w

    with open("ru-en.txt", "w") as file:
        for i in sorted(d.keys()):
            file.writelines(f"{i} - {d[i]}\n")


lab1()
lab2()
lab3()
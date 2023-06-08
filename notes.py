
from datetime import date
import json
import os
from time import strptime
import random
import string


def clear(): return os.system('clear')


def random_number():
    return ''.join(random.choices(string.ascii_letters, k=5))


def AddNote(fileName, title, body):
    users = json.load(open(fileName))
    users.append({
        "id": random_number(),
        "title": title,
        "body": body,
        "date": str(date.today())
    })

    with open(fileName, 'w') as outfile:
        json.dump(users, outfile, indent=4,
                  ensure_ascii=False)
    print('Заметка успешно сохранена')


def FindNoteByDate(fileName, date):
    status = False
    list = json.load(open(fileName))
    listNew = []
    for d in list:
        if d["date"] == date:
            listNew.append({
                "id": d["id"],
                "title": d["title"],
                "body": d["body"],
                "date": d["date"]
            })
            status = True
    for i in sorted(listNew, key=lambda i: strptime(i["date"], "%Y-%m-%d")):
        print(i)
    if not status:
        print('Заметка не найдена')


def DelNote(fileName, id):
    status = False
    list = json.load(open(fileName))
    listNew = []
    for d in list:
        if d["id"] != id:
            listNew.append({
                "id": d["id"],
                "title": d["title"],
                "body": d["body"],
                "date": d["date"]
            })
        elif d["id"] == id:
            status = True
    with open(fileName, 'w') as outfile:
        json.dump(listNew, outfile, indent=4,
                  ensure_ascii=False)
    if status:
        print('Заметка удалена')
    else:
        print('Заметка не найдена')


def CheckNote(fileName, id):
    status = False
    list = json.load(open(fileName))
    for d in list:
        if d["id"] == id:
            status = True
    return status


def EditNote(fileName, id, body):
    list = json.load(open(fileName))
    for d in list:
        if d["id"] == id:
            d["body"] = body
            d["date"] = str(date.today())
    with open(fileName, 'w') as outfile:
        json.dump(list, outfile, indent=4,
                  ensure_ascii=False)
    print('Заметка изменена')


def DisplayAllNote(name):
    with open(name, "r") as file:
        list = json.load(file)
        for i in sorted(list, key=lambda i: strptime(i["date"], "%Y-%m-%d")):
            print(i)


fName = 'file.json'
clear()

if not os.path.exists(fName):
    with open(fName, "w") as f:
        f.write("[]")

while True:
    menuitems = \
        ('1 - Создать заметку',
            '2 - Просмотреть список заметок',
            '3 - Просмотреть заметку по дате',
            '4 - Редактировать заметку',
            '5 - Удалить заметку',
            '6 - Выход')

    print("\n")
    print('Введите номер действия:')
    list(map(lambda x: print(x), menuitems))
    menu = int(input())
    clear()
    if menu == 1:
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        AddNote(fName, title, body)
    elif menu == 2:
        DisplayAllNote(fName)
    elif menu == 3:
        text = input("Введите дату yyyy-mm-dd: ")
        FindNoteByDate(fName, text)
    elif menu == 4:
        id = input("Введите id заметки: ")
        if CheckNote(fName, id):
            body = input("Введите тело новой заметки: ")
            EditNote(fName, id, body)
        else:
            print('Заметка не найдена')
    elif menu == 5:
        id = input("Введите id заметки: ")
        DelNote(fName, id)
    elif menu == 6:
        quit()

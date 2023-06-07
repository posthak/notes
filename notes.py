
import os


def clear(): return os.system('clear')


def AddNote(fileName, title, body):
    date = '2023.06.06'
    id = '1'
    with open(fileName, "a", encoding="utf8") as file:
        file.write(id + ";" + date + ";" + title + ";" + body + ";" + "\n")
    print('Contact was added!')


def ShowAll(name):
    with open(name, "r", encoding="utf8") as file:
        list(map(lambda x: print(x, end=""), file.read()))


fName = 'note.csv'
clear()
while True:
    menuitems = \
        ('1 - Создать заметку',
            '2 - Сохранить заметку',
            '3 - Просмотреть список заметок',
            '4 - Просмотреть заметку по дате',
            '5 - Редактировать заметку',
            '6 - Удалить заметку',
            '7 - Выход')

    print('Введите номер действия:')
    list(map(lambda x: print(x), menuitems))
    menu = int(input())
    clear()
    if menu == 1:
        # ReadFile(fName)
        print('Создание заметки...')
        title = input("Input tile: ")
        body = input("Input body: ")
        AddNote(fName, title, body)
    elif menu == 2:
        text = input("Input name: ")
        print('Сохранение заметки...')
        #FindByName(fName, text)
    elif menu == 3:
        text = input("Input number: ")
        print('Вывести все заметки на экран...')
        #FindByName(fName, text)
        ShowAll(fName)
    elif menu == 4:
        text = input("Input number: ")
        print('Вывести заметку на кран...')
        #FindByName(fName, text)
    elif menu == 5:
        text = str(input("Input new contact:"))
        print('Редактирование заметки...')
        #AddLineFile(fName, text)
    elif menu == 6:
        text = str(input("Input name or mob. num: "))
        print('Удаление заметки...')
        #DeleteContact(fName, text)
    elif menu == 7:
        quit()

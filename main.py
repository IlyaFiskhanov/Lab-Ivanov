import json
import os

class Student:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            with open(self.file_name, encoding='utf-8') as f:
                self.all_students = json.load(f)

        else:
            self.all_students = []

    def save(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.all_students, f, ensure_ascii=False)

    def get(self, num):
        return self.all_students[num - 1]

    def add_student(self, name, surname, age):
        self.all_students.append({"имя": name, "surname": surname, "age": age})
        self.save()

    def del_student(self, name, surname, age):
        self.all_students.remove({"имя": name, "surname": surname, "age": age})
        self.save()

    def select_by_age(self, age):
        return [x for x in self.all_students if x['age'] == age]

class Professor:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            with open(self.file_name, encoding='utf-8') as f:
                self.all_prepod = json.load(f)
        else:
            self.all_prepod = []

    def save(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.all_prepod, f, ensure_ascii=False)

    def add_prepod(self, name, surname, age):

        self.all_prepod.append({"имя": name, "surname": surname, "age": age})
        self.save()

    def del_prepod(self, name, surname, age):
        self.all_prepod.remove({"имя": name, "surname": surname, "age": age})
        self.save()

class Subject:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            with open(self.file_name, encoding='utf-8') as f:
                self.all_subject = json.load(f)
        else:
            self.all_subject = []

    def save(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.all_subject, f, ensure_ascii=True)

    def add_subject(self,name):
        self.all_subject.append(name)
        self.save()

    def del_subject(self, name):
        self.all_subject.remove(name)
        self.save()

if __name__ == '__main__':
    db = Student('all_students.json')
    db1 = Professor('all_Professor.json')
    db2 = Subject('all_subject.json')

    print('''\
Выберите действие:
    1 - Добавить студента,
    2 - Добавить преподаватель
    3 - Удаление студента
    4 - Удаление преподавателя
    5 - Список всех студентов
    6 - Список всех преподователей
    7 - Добавить предмет
    8 - Удалить предмет
    9 - Список всех предметов
    10 - вывод по номеру
    11 - вывод по возрасту,
    для выхода - 0
''')

    while True:
        f = input('Ввод действия:  ')
        if f == '1':
            print('Введите данные студента через пробел (имя , фамилия , возраст)')
            name, surname, age = input().split()
            db.add_student(name, surname, age)

        elif f == '2':
            print('Введите данные преподователя через пробел (имя,фамилия,возраст)')
            name, surname, age = input().split()
            db1.add_prepod(name, surname, age)

        elif f == '3':
            print('Введите данные студента через пробел (имя,фамилия,возраст),которые хотите удалить')
            with open(db.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))
            name, surname, age = input().split()
            db.del_student(name, surname, age)

        elif f == '4':
            print('')
            with open(db1.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))
            name, surname, age = input().split()
            db1.del_prepod(name, surname, age)

        elif f == '5':
            with open(db.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))

        elif f == '6':
            with open(db1.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))

        elif f == '7':
            print('Введите название предмета')
            name = input().split()
            db2.add_subject(name)

        elif f == '8':
            print('Введите название предмета который хотите удалить')
            with open(db2.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))
            name = input().split()
            db2.del_subject(name)

        elif f == '9':
            with open(db2.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))

        elif f == '10':
            num = int(input('Номер ->  '))
            print(db.get(num))

        elif f == '11':
            items = db.select_by_age(input('Возраст-> '))
            print(items)

        else:
            break

    db.save()
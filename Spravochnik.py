# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


#!!!!!!!!!!!!!11 splitlines() - преобразовывает текст в список строк!!!!!!!!!!!!!!!!!!!!!11


import os

def add_person():    #функция добавления данных пользователя в файл
    lastname = input('Введите фамилию - ')  #Иванов
    name = input('Введите имя - ')          #Иван
    surname = input('Введите отчество - ')  #Иванович
    phone = input('Введите телефон - ')     #89102582525
    data = open('HomePython_1703\\Files\\phonebook.txt', 'a', encoding='utf-8')        #encoding='utf-8' - для декодирования русских слов
    data.writelines([lastname + ' ', name + ' ',surname+' ',phone, '\n'])
    data.close()   #закрыли файл
#add_person()


def print_data():    #функция вывода данных на экран
    with open('HomePython_1703\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
              print(data.read())
#print_data()


def search():        #функция поиска
      search_name = input('Введите данные для поиска - ')
      with open('HomePython_1703\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
            for line in data:
                  if search_name in line:
                        print(line)
#search()


def load_data():       #функция загрузки данных из другого файла(из new_data.txt)
      with open('HomePython_1703\\Files\\phonebook.txt', 'r+', encoding='utf-8') as data:
            text_data = data.read()
            path = input('Введите адрес файла - ')
            with open(path, 'r', encoding='utf-8') as data_2:
                  for line in data_2:
                        if line not in text_data:
                            data.write(line)
#load_data()


# ДОМАШНЕЕ ЗАДАНИЕ ! Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных  


def remote_data():           #функция удаления данных
     remote_name = input('Введите данные для удаления - ')
     with open('HomePython_1703\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        arr = data.readlines()     #записываем в переменную arr список строк
        for line in arr:
            if remote_name in line:
                del arr[arr.index(line)]   #удаляем значение по индексу
     with open('HomePython_1703\\Files\\phonebook.txt', 'w', encoding='utf-8') as data:
        for line in arr:
            data.write(line)
#remote()


def change_data():
     change_name = input('Введите данные контакта, который хотите изменить - ')
     last_name = input('Введите новую фамилию - ')
     name = input('Введите новое имя - ')
     surname = input('Введите новое отчество - ')
     phone = input('Введите новый номер телефона - ')

     with open('HomePython_1703\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
          d = data.readlines()
     for i_line in range(len(d)):
          if change_name in d[i_line]:
               d[i_line] = last_name + ' '+name+' ' + surname + ' ' + phone

     with open ('HomePython_1703\\Files\\phonebook.txt', 'w', encoding='utf-8') as data:
         for line in d:
              data.write(line) 
#change_data()


def user_interface():            #метод, в который мы впишем все наши функции сразу   #``` - для многопользовательского ввода
            os.system('cls')     #очистили консль]
            print('''1 - добавить контакт   
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удаление данных
6 - изменения данных
7 - выход''')
            user_input=input('Введите нужный вариант операции - ') 
            while user_input != '7':    #защита от дурака
                if user_input == '1':
                    add_person()
                elif user_input == '2':
                    search()
                elif user_input == '3':
                    load_data()
                elif user_input == '4':
                    print_data()
                elif user_input == '5':
                    remote_data()
                elif user_input == '6':
                    change_data()    
                else:
                    print('Вы ввели некорректный вариант, попробуйте еще раз!')
                os.system('cls')    #очистили консoль
                print('''1 - добавить контакт   
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удаление данных
6 - изменения данных
7 - выход''')
                user_input=input('Введите нужный вариант операции - ')
                

def main():
     user_interface()

if __name__ == "__main__":
     main()


              
            

      
              


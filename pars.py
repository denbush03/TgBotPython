import requests
from bs4 import BeautifulSoup
import time
import json


def pars_timetable(group, date):
    """
        Функция парсинга расписания. На вход получает id группы
        и дату. Делает запрос к серверу, передавая номер группы 
        и дату. номер группы и дата должны вводится строками,
        дата в формате 'год-месяц-день': '2023-03-19' и т.д.
    """
    ans = ''
    res = ''
    t = 0
    tableUrl = f'https://edu.donstu.ru/api/Rasp?idGroup={group}&sdate={date}'

    # Проверяем корректность группы, если длинна названия больше 5 или если название группы состоит не просто из цифр 
    if len(group) < 5 or (not(group.isdigit())):
        return 'Неккоректно указана группа.'
    
    # Проверяем корректность даты.
    if len(date) < 10 or \
    (not(((date[0:4]).isdigit()) and \
    ((date[5:7]).isdigit()) and \
    ((date[8:]).isdigit()) and \
    (date[4] == '-') and \
    (date[7] == '-'))):
        return 'Некорректная дата.'
    
    # Делаем паузу, чтобы не грузить сайт.
    time.sleep(1)

    # Пытаемся выполнить запрос(Не больше пяти попыток) с паузами между попытками.
    while res == '' and t < 5:
        t += 1
        try:
            res = requests.get(tableUrl)
            break
        except:
            res = ''
            time.sleep(3)
    
    # Если результат пуст - значит мы так ничего и не получили от сайта на предыдущем этапе. 
    if res == '':
        ans = 'Неудалось выполнить запрос. Проверьте корректность ввода'
    # Иначе создаём список пар, проходимся по результату и заполняем этот список, если дата пары совпадает с указанной.
    else:
        try:
            # Создаем список lessonsList в который мы будем записывать расписание
            lessonsList = []
            # Мы переводим res к json формату
            jRes = json.loads(res.text)
            # В полученном json'e ищем расписание
            rasp = jRes['data']['rasp']
            
            # Проходимся по элементам и находим те, которые удовлетворяют нас по дате и затем добавляем их в список пар
            for el in rasp:
                elDate = el['дата'].split('T')[0]
                if elDate == date:
                    elDict = {}
                    elDict['Дата'] = elDate
                    elDict['Начало'] = el['начало']
                    elDict['Конец'] = el['конец']
                    elDict['День недели'] = el['день_недели']
                    elDict['Дисциплина'] = el['дисциплина']
                    elDict['Преподаватель'] = el['преподаватель']
                    elDict['Аудитория'] = el['аудитория']
                    lessonsList.append(elDict)
        except:
            ans = 'Непредвиденная ошибка.'
    # Если lessonsList пустой, значит на сайте нет расписания и мы выводим, что пар нет 
    if len(lessonsList) == 0:
        ans = 'В этот день нет пар или расписание на это число недоступно.'
    # Иначе просто волучаем результат
    else:
        ans = lessonsList

    # Возвращаем ответ
    return ans


if __name__ == '__main__':

    print(pars_timetable('44439', '2023-03-14'))
    print(pars_timetable('44440', '2023-03-14'))
    print(pars_timetable('44441', '2023-03-14'))
    print(pars_timetable('44442', '2023-03-14'))
    print(pars_timetable('44442', '2023-03-10'))
    print(pars_timetable('44439', '2023-03-1'))
    print(pars_timetable('44439', '2023-03-04'))
    print(pars_timetable('4443', '2023-03-14'))
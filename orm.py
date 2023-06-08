from peewee import *
import datetime
from models import *


# Функция user_exists которая принимает id пользователя 
# и проверяет зарегистрирован ли пользователь.
def user_exists(user_ids):
    # Подключение к БД
    with db:
        # Создаем запись, если user_id = user_ids
        req = User.select().where(User.user_id == f'{user_ids}') 
        # Возвращает 1 если пользователь есть и 0 если нет.
        return bool(len(req))

# Функция set_group которая принимает название группы,
# id пользователя и изменяет группу.    
def set_group(user_ids, group_names):
    # Подключение к БД
    with db:
        # Обновляем значение в строчке group_name нужного пользователя
        req = User.update(group_name = f'{group_names}').where(User.user_id == f'{user_ids}').execute() 
        # Возвращаем результат
        return req

# Функция add_user которая принимает id пользователя 
# и добавляет его в базу данных
def add_users(user_i):
    # Подключение к БД
    with db:
        # Добавляем в колонку user_id id пользователя
        user = User.insert(user_id = f'{user_i}').execute()
        return user

# Функция user_group_name которая принимает id пользователя
# и выводит нам название группы принадлежащей пользователю.    
def user_group_name(user_ids):
        # Подключение к БД
        with db:
            # Выбираем все где user_id = user_id
            result =  User.select().where(User.user_id == f'{user_ids}') 
            # Проверка наличия результата
            if len(result) == 0:
                return False
            # Возвращение результата если он есть.
            for r in result:
                return(r.group_name)

# Функция group_id которая принимает название группы
# и выводит нам id группы             
def group_id(group_names):
        # Подключение к БД
        with db:
            # Создание запроса
            req = Group.select().where(Group.group_name == f'{group_names}')   #  f"SELECT group_id FROM groups WHERE group_name = '{group_name}'"
            result = req
            # Проверка наличия результата
            if len(result) == 0:
                return False
            # Возвращение результата если он есть.
            for r in result:
                return(r.group_id)
        
    
if __name__ == '__main__':
    # Тесты
    print(user_exists('177745555'))
    print(set_group('177745555', 'MКИС34'))
    print(user_group_name('5'))
    print(user_exists('5'))
    print(user_group_name('188888889999999882345555'))
    print(group_id('МКИС31'))
    print(group_id('МКИС32'))
    print(group_id('МКИС33'))
    print(group_id('МКИС34'))
    print(group_id('МКИС3'))

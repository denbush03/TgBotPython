from peewee import *


# Подключение к базе данных
db = SqliteDatabase('db.db')

# Базовый класс 
class BaseModel(Model):

    # Поле Id у всех наследников будет PrimaryKey
    id = PrimaryKeyField(unique = True)

    class Meta:
        # Подключение к БД
        database = db
        # Связка таблиц по group_name
        order_by = 'group_name'

# Класс наследник BaseModel
class User(BaseModel):

    # Создание колонки user_id, тип данных Char
    user_id = CharField()
    # Создание колонки group_name, тип данных Char
    group_name = CharField()

    class Meta:
        # Назваем таблицу users
        db_table = 'users'

class Group(BaseModel):

    # Создание колонки group_id, тип данных Char
    group_id = CharField()
    # Создание колонки group_name, тип данных Char
    group_name = CharField()

    class Meta:
        # Назваем таблицу groups
        db_table = 'groups'
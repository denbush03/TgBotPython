# Импорт нужных нам библиотек и полключение файлов
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor
from aiogram.types import Message, InputMediaAudio, InputFile            
import markups as nav
import logging
import pars 
import datetime
import orm
import random


# Авторизационный токен для подключения к телеграм боту
TOKEN_API = "Ваш токен" 

# Текст который будет выводиться при команде help
HELP_COMMAND = """
<em>/help</em> - <b>cписок команд</b>
<em>/start</em> - <b>начать работу с ботом</b>
<em>/description</em> - <b>описание бота</b>
<em>/give</em> - <b>отправка ботом стикера</b>
<em>/img</em> - <b>отправка ботом фото</b>
<em>/audio</em> - <b>отправка ботом музыки</b>
<em>/group</em> - <b>Объяснения того, как выбрать группу</b>
<em>/schedule_today</em> - <b> Расписание на сегодня (не забудь выбрать свою группу)</b>
<em>/schedule_tomorrow</em> - <b> Расписание на завтра (не забудь выбрать свою группу) </b>
также ты можешь выбирать дату на которую хочешь узнать расписание, для этого напиши :'Расписание на: год-месяц-день'(правда вместо 'год-месяц-день' укажи числа)"""

# Описание бота, ктоторое выведется при команде description
DESCRIPTION = """
Я телеграм бот который может предоставить расписание твоей группы на сегодня, завтра или 
выбранный тобою день.
Конечно, если она есть в списке групп.
Список доступных групп:
МКИС22 - 25 
МКИС31 - 34 
"""

logging.basicConfig(level=logging.INFO)

# подключаем токен самого бота и создаем экземпляр класса диспейчер
# для работы с ним
# Создание объекта бот для работы с ботом
bot = Bot(TOKEN_API) 
# Диспейчер сообщений нашего бота
dp = Dispatcher(bot)


# Функция on_startup которая уведомляет нас, что бот запустился
async def on_startup(_):
    # Вывод в консоль сообщения о запуске бота
    print("Бот был успешно запущен!")


# Функция help которая выводит информацию о всех основных командах,
# которые помогут пользователю коммуниуировать с ботом
# Обработка сообщения диспейчером - dp
# Если написана команда /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # Отправка пользователю сообщения с командами, которые есть в боте
    await message.reply(text=HELP_COMMAND,
                         parse_mode="HTML")

# Обработка сообщения диспейчером - dp
# Если написана команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """
        Функция начала работы с ботом.
        где мы добавляем пользователя в базу данных, если он зашел в первый раз 
        и предлагаем выбрать ему группу.
        если такой пользователь уже зарегистрирован, мы будем ему сообщать, в какой группе он состоит.
        После срабатывания этой функции открываем пользователю клавиатуру с командами
    """
    # Если пользователь уже начинал общение с ботом
    # посредством кнопки /start
    if orm.user_exists(message.from_user.id):
        # Узнаем группу , которую выбрал пользовательс помощью функции user_group_name
        group_name = orm.user_group_name(message.from_user.id)
        # Отправка пользователю сообщения с информацией о выбранной группе
        await message.answer(text=f'<em><b>Приветствую тебя в нашем телеграм боте! Вами выбрана группа {group_name}!</b> </em>',
                          parse_mode="HTML", reply_markup=nav.keyboard)
    # Если пользователь никак не взаимодействовал с ботом
    # передаем ему информацию, о том, как настроить группу
    else:
        # Добавляем пользователя в базу данных пользователей с помощью функции add_user
        orm.add_users(message.from_user.id)
        # Отправка пользователю сообщения с приветствием
        await message.answer(text='<em><b>Приветствую тебя в нашем телеграм боте! Похоже ты не зарегистрирован Выбери группу чтобы узнать ее расписание! По умолчанию ваша группа МКИС31</b> </em>',
                          parse_mode="HTML", reply_markup=nav.keyboard)
        # Отправка пользователю сообщения с информацией как выбрать группу
        await message.answer(text='<em><b></b> Для того чтоб выбрать группу напиши: Моя группа: (ТВОЯ ГРУППА В ВЕРХНЕМ РЕГИСТРЕ) </em>',
                          parse_mode="HTML")

# Функция group которая выводит информацию о том,
# как выбрать группу
# Обработка сообщения диспейчером - dp
# Если написана команда /group
@dp.message_handler(commands=['group'])
async def group_command(message: types.Message):
    # Отправка пользователю сообщения с информацией как выбрать группу
    await message.answer(text='<em><b>Выбери группу, расписание которой тебе интересно. Для этого напиши : Моя группа: (ТВОЯ ГРУППА В ВЕРХНЕМ РЕГИСТРЕ)</b> </em>',
                          parse_mode="HTML", reply_markup=nav.keyboard)

# Функция description которая выводит информацию о боте 
# и поможет нам понять его предназначение
# Обработка сообщения диспейчером - dp
# Если написана команда /description
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    # Отправка пользователю сообщения с информацией о самом боте
    # и его предназаначении
    await message.answer(text=DESCRIPTION)

# Функция schedule_today которая выводит расписание
# на сегодняшний день
# Обработка сообщения диспейчером - dp
# Если написана команда schedule_today
@dp.message_handler(commands=['schedule_today'])
async def schedule_today(message: types.Message):
    await message.answer(text='Расписание на сегодня:')
    # Узнаем название группы пользователя благодаря подключенной базе данных
    group_name = orm.user_group_name(message.from_user.id) 
    # Узнаем id группы , к которой пренадлежит пользователь
    group_id = str(orm.group_id(group_name))
    # Заполняем список пар с помощью функции pars_timetable 
    lessonsList = pars.pars_timetable(group_id, str(datetime.date.today()))

    validAnswer = ''

    # Проверяем что список пар является объектом типа list
    if type(lessonsList) == list:
        # Выбираем нужные для нас даннные из парсера и грамотно их выводим
        for lesson in lessonsList:
            validAnswer += f'Время: {lesson["Начало"]}-{lesson["Конец"]}\n'
            validAnswer += f'Дисциплина: {lesson["Дисциплина"]}\n'
            validAnswer += f'Аудитория: {lesson["Аудитория"]}\n'
            validAnswer += f'Преподаватель: {lesson["Преподаватель"]}\n'
            validAnswer += '\n'

        # Выводим собраный нами список пар
        await message.answer(validAnswer)
    else:
        # Выводим информацию об ошибке
        await message.answer(lessonsList)

    # Если расписание на этот день не найдено
    if lessonsList == 'В этот день нет пар или расписание на это число недоступно.':
        print('photo')
        # Выводим пользователю смешную картинку
        await bot.send_photo(chat_id=message.chat.id, 
                photo="https://i.ytimg.com/vi/HgtgivOwh94/maxresdefault.jpg?7857057827")

# Функция give_command которая выводит пользователю стикер 
# Обработка сообщения диспейчером - dp
# Если написана команда /give
@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.answer(text='Смотри какой смешной стикер)')
    # Отправка пользователю стикера
    await bot.send_sticker(message.from_user.id,
                            sticker="CAACAgIAAxkBAAEIEMBkCf-NyE7QN5Th1zoo5fQuzjAxfAACNgADKX_KChB7m2I026YtLwQ")

# Функция send_image которая выводит пользователю фото
# Обработка сообщения диспейчером - dp
# Если написана команда /img
@dp.message_handler(commands=['img'])
async def send_image(message: types.Message):
    # Отправка пользователю фото
    await bot.send_photo(chat_id=message.chat.id, 
                        photo="https://reg.place/uploads/image/file/cff44afbfc28e06b7c911420c4e38e538abb3faa431373e50d9f74d5e96763ae/df68c480-b543-4e29-911f-4dff3ebbf4a1.jpg",
                         reply_markup=nav.ikb)
    

# Функция schedule_tomorrow которая выводит расписание
# на завтрашний день
# Обработка сообщения диспейчером - dp
# Если написана команда /schedule_tomorrow
@dp.message_handler(commands=['schedule_tomorrow'])
async def schedule_tomorrow(message: types.Message):
    await message.answer(text='Расписание на завтрашний день:')
    # Узнаем название группы пользователя благодаря подключенной базе данных
    group_name = orm.user_group_name(message.from_user.id)
    # Узнаем id группы , к которой пренадлежит пользователь
    group_id = str(orm.group_id(group_name))

    # Заполняем список пар с помощью функции pars_timetable 
    lessonsList = pars.pars_timetable(group_id, str(datetime.date.today() + datetime.timedelta(days=1)))

    # Если расписание на этот день не найдено
    if lessonsList == 'В этот день нет пар или расписание на это число недоступно.':
        print('photo')
        # Выводим сообщение что пары не найдены
        await message.answer(text='В этот день нет пар или расписание на это число недоступно.')
        # Выводим пользователю смешную картинку
        await bot.send_photo(chat_id=message.chat.id, 
                photo="https://i.ytimg.com/vi/HgtgivOwh94/maxresdefault.jpg?7857057827")

    validAnswer = ''

    # Проверяем что список пар является объектом типа list
    if type(lessonsList) == list:
        # Выбираем нужные для нас даннные из парсера и грамотно их записываем
        for lesson in lessonsList:
            validAnswer += f'Время: {lesson["Начало"]}-{lesson["Конец"]}\n'
            validAnswer += f'Дисциплина: {lesson["Дисциплина"]}\n'
            validAnswer += f'Аудитория: {lesson["Аудитория"]}\n'
            validAnswer += f'Преподаватель: {lesson["Преподаватель"]}\n'
            validAnswer += '\n'

        # Выводим собраный нами список пар
        await message.answer(validAnswer)
    else:
        # Выводим информацию об ошибке
        await message.answer(lessonsList)

# Функция bot_audio которая отправляет музыку 
# Обработка сообщения диспейчером - dp
# Если написана команда /audio
@dp.message_handler(commands=['audio'])
async def bot_audio(message: types.Message):
    # Список треков
    treck_list = ['audio.mp3', 'audio1.mp3', 'audio2.mp3', 'audio3.mp3']
    # Выбор рандомного трека и вывод информации в консоль
    print("Выбор случайного трека из списка - ", random.choice(treck_list))
    # Через InputFile работаем с файлом
    voice = InputFile((rf"{random.choice(treck_list)}"))
    # Отправка пользователю сообщения о треке
    await message.answer(text='Вот трек который стоит послушать:')
    # Отправка пользователю аудио
    await bot.send_audio(message.chat.id, voice)

# Обработка сообщения диспейчером - dp
# Если отправлено простое сообщение
@dp.message_handler()
async def bot_message(message: types.Message):
    
    # Записываем сообщение пользователя в переменную user_text
    user_text = message.text
    # Если в сообщении пользователя начинается с 'Моя группа:' то выполняем блок
    if 'Моя группа: ' in user_text:
        # Проверка на корректность указания группы
        # Если длинна сообщения меньше или равна 10 
        # группа указана неверно 
        if len(user_text) <= 10:
            # Вывод сообщение пользователь в некоректности указания группы
            await message.answer(text='Пустая группа.')
        else:
            #Разбиваем сообщения и берем текст группы
            fullComand = message.text.split(': ')
            group = fullComand[1]
            # Записываем/обновляем название группы в бд
            # c помощью функции set_group
            orm.set_group(str(message.from_user.id), group)
            # Отправляем пользователю сообщение, что он успешно выбрал
            # группу и выводим ее название
            await message.answer(text=f'Вы выбрали группу: {group}')

    # Если в сообщении пользователя начинается с 'Расписание на:' то выполняем блок
    elif 'Расписание на: ' in user_text:
        # Проверка на корректность указания времени
        # Если длинна сообщения меньше или равна 15 
        # время указано неверно 
        if len(user_text) <= len('Расписание на: '):
            # Вывод сообщение пользователю некоректности указания времени
            await message.answer(text='Не указано время')
        else:
            # Разбиваем сообщения и берем текст даты
            fullComand = message.text.split(': ')
            date = fullComand[1]
            # Узнаем группу пользователя в бд c помощью функции user_group_name
            group_name = orm.user_group_name(message.from_user.id)
            # Узнаем  id группы пользователя в бд c помощью функции group_id
            group_id = str(orm.group_id(group_name))

            # Заполняем список пар с помощью функции pars_timetable 
            lessonsList = pars.pars_timetable(group_id, date)

            # Если расписание на этот день не найдено
            if lessonsList == 'В этот день нет пар или расписание на это число недоступно.':
                print('photo')
                # Выводим пользователю смешную картинку
                await bot.send_photo(chat_id=message.chat.id, 
                        photo="https://i.ytimg.com/vi/HgtgivOwh94/maxresdefault.jpg?7857057827")


            elif type(lessonsList) == list:

                validAnswer = ''

                # Проверяем что список пар является объектом типа list
                for lesson in lessonsList:
                    # Выбираем нужные для нас даннные из парсера и грамотно их записываем
                    validAnswer += f'Время: {lesson["Начало"]}-{lesson["Конец"]}\n'
                    validAnswer += f'Дисциплина: {lesson["Дисциплина"]}\n'
                    validAnswer += f'Аудитория: {lesson["Аудитория"]}\n'
                    validAnswer += f'Преподаватель: {lesson["Преподаватель"]}\n'
                    validAnswer += '\n'

                # Выводим собраный нами список пар
                await message.answer(validAnswer)

            else:
                # Выводим информацию об ошибке
                await message.answer(lessonsList)

    else:
        # Выводим сообщение о нераспознанной команде
        await message.answer("Команда не распознана")
        

        
if __name__ == '__main__':
    # Запуск цикла обработки и приема сообщений 
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
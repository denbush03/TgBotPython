# TgBotPython

Название:
DSTU_BOT

Описание:
Телеграмм бот - помощник для студентов, которые хотят узнать расписание своих занятий на выбранный ими день. Есть возможность выбора группы МКИС31-34.

Реализовано:

регистрация пользователей
выбор группы
вывод расписания на сегодняшний день
вывод расписания на завтрашний день
вывод расписания на день, который введет пользователь
отправка ботом трека
отправка ботом изображений
Технологии в проекте:
Проект написан на языке программирования Python c использованием библиотек aiogram, datetime, peewee, requests. Реализована ORM model (Object-Relational Mapping, объектно-реляционное отображение. Благодаря этой технологии разработчики могут использовать язык программирования, с которым им удобно работать с базой данных, вместо написания операторов SQL или хранимых процедур.) для работы с базой данных. Осуществлена функция парсинга сайта с расписанием https://edu.donstu.ru.

Техническое описание проекта:
проект предлагается в виде проекта на хостинге и в исходном коде. Исходный код состоит из запускающего файла - tgbot.py и файлов, содержащих функции для работы с базой данных, парсингом сайта и настройке клавиатуры бота, а также базы данных. db.db - база данных markups.py - файл для настройки клавиатуры бота models.py - основные модели для работы с базой данных orm.py - организованные функции для работы с базой данных pars.py - парсер сайта с расписанием audio.mp3 - аудио сообщение audio1.mp3 - аудио сообщение1 audio2.mp3 - аудио сообщение2 audio3.mp3 - аудио сообщение3

Проект находится на хостинге - beget

Порядок работы с ботом:
Переходим по ссылке @mydstu_Bot (http://t.me/mydstu_Bot) и начинаем работу с ботом посредством кнопки /start, начинается проверка регистрации пользователя с помощью обращения к БД (таблица users) и проверки id пользователя в ней. Если пользователь зарегистрирован, будет выведено приветствие и указана группа, которую он выбрал, иначе ему будет предложено выбрать группу посредством команды , например: Моя группа: МКИС32 (посредством этой команды запись в базе данных пользователей обновится и ему будет присвоена группа МКИС32 (каждой группе присвоен свой id в таблице groups базы данных )).
Для того чтобы узнать расписание занятий пользователю нужно ввести команды: /schedule_today, /schedule_tomorrow, или написать: Расписание на 'год-месяц-день'. В случае, если расписание на этот день есть, оно будет выведено, в ином случае мы отправим сообщениями информацию что пар нет и фото, что можно отдыхать.
Для вывода ботом музыки можно отправить ему команду /audio, в ответ он отправит одну из песен, хранящихся в нем.
Команда /img выведет иконку ДГТУ со ссылками на эту картинку.
При команде /give бот выведет стикер.
Также существует команда /help, которая выведет пользователю список всех команд для работы с ботом и их краткое описание.

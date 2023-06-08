from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создание линейноц клавиатуры
ikb = InlineKeyboardMarkup(row_width=2)
# Создание линейной кнопки Button1 со ссылкой на фото
ib1 = InlineKeyboardButton(text="Button1",
                           url= "https://reg.place/uploads/image/file/cff44afbfc28e06b7c911420c4e38e538abb3faa431373e50d9f74d5e96763ae/df68c480-b543-4e29-911f-4dff3ebbf4a1.jpg")
# Создание линейной кнопки Button2 со ссылкой на фото
ib2 = InlineKeyboardButton(text="Button2",
                           url= "https://reg.place/uploads/image/file/cff44afbfc28e06b7c911420c4e38e538abb3faa431373e50d9f74d5e96763ae/df68c480-b543-4e29-911f-4dff3ebbf4a1.jpg")
# Добавление кнопок в клавиатуру
ikb.add(ib1, ib2)

# Создание реплай клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True) 
# Создание кнопки с командой /help
button_help = KeyboardButton('/help')
# Создание кнопки с командой /description
button_desc = KeyboardButton('/description')
# Создание кнопки с командой /give
button_give = KeyboardButton('/give')
# Создание кнопки с командой /img
button_img = KeyboardButton('/img')
# Создание кнопки с командой /schedule_tomorrow
button_sched_tw = KeyboardButton('/schedule_tomorrow')
# Создание кнопки с командой /schedule_today
button_sched_td = KeyboardButton('/schedule_today')
# Создание кнопки с командой /audio
button_audio = KeyboardButton('/audio')
# Создание кнопки с командой /group
button_group = KeyboardButton('/group')

# Добавление кнопок в клавиатуру
keyboard.add(button_help).insert(button_desc).add(button_give).insert(button_img).add(button_sched_tw).insert(button_sched_td).add(button_audio).insert(button_group)

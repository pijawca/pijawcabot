# -*- coding: utf-8 -*-
# -8- pijawca -8-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


a1 = KeyboardButton(text='🔃 Обновить')
a2 = KeyboardButton(text='📰 Новости')
a3 = KeyboardButton(text='⚙️ Администрирование')
a4 = KeyboardButton(text='👽️ Поддержка')
a5 = KeyboardButton(text='💡 Скрипты')
a6 = KeyboardButton(text='Получить ID')
a7 = KeyboardButton(text='💵 Услуги')
a8 = KeyboardButton(text='Заказать дизайн')
a9 = KeyboardButton(text='Заказать разработку бота')
a10 = KeyboardButton(text='🤝🏻 Отзывы')
a11 = KeyboardButton(text='🔧️ В разработке')
back = KeyboardButton(text='Назад')
support = InlineKeyboardButton(text='Связаться', url='https://t.me/pijawca')
reviews = InlineKeyboardMarkup(text='Перейти', url='https://t.me/+ItCispnZ4QI2ZmMy')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.insert(a2).insert(a5).insert(a3).add(a7).insert(a10).insert(a11).add(a1).add(a4)
kb_scripts = ReplyKeyboardMarkup(resize_keyboard=True)
kb_scripts.add(a6).add(back)
kb_support = InlineKeyboardMarkup().insert(support)
kb_work = ReplyKeyboardMarkup(resize_keyboard=True)
kb_work.add(a8).add(a9).add(back)
kb_reviews = InlineKeyboardMarkup().insert(reviews)




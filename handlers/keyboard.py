# -*- coding: utf-8 -*-
#!/usr/bin/env python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


c1 = KeyboardButton(text='💵 Оплата услуг')
c2 = KeyboardButton(text='⚙️ Администрирование')
c3 = KeyboardButton(text='💎 Список ботов')
a1 = KeyboardButton(text='🟢 Пингование')
p1 = KeyboardButton(text='ping_n1')
p2 = KeyboardButton(text='ping_n2')
p3 = KeyboardButton(text='ping_n3')
back = KeyboardButton(text='Назад')
attention_all = KeyboardButton(text='🔤 Написать всем')
support = InlineKeyboardButton(text='💌 Связаться', url='https://t.me/pijawca')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.insert(attention_all).insert(a1).add(back)

kb_ping = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ping.insert(p1).insert(p2).insert(p3).add(back)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(c1).insert(c3).add(c2).add(support)


kb_support = InlineKeyboardMarkup().insert(support)
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from misc import bot, dp
from config import PING, DB_NAME, DB_USER, DB_PORT, DB_HOST, DB_PASSWORD
from handlers.keyboard import kb_client, kb_support, kb_admin, kb_ping
from os import system
from db import check_admins, search_userids
import psycopg


class UserState(StatesGroup):
    att = State()
    
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Добро пожаловать @{message.from_user.username}',
        reply_markup=kb_client
        )
    
    user_id = message.from_user.id
    username = message.from_user.username
    
    conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    conn.autocommit = True
    try:
        with conn.cursor() as cur:
            cur.execute(f"""INSERT INTO {DB_NAME} (user_id, username, admin) VALUES (%s, %s, %s)""",
                        (user_id, username, 0))
            conn.commit()
    except psycopg.errors.UniqueViolation:
        pass
    except psycopg.errors.InFailedSqlTransaction:
        pass

async def back(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'В главное меню',
        reply_markup=kb_client
        )
            
async def admin(message: types.Message):
    if message.chat.id == check_admins():
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'Вы вошли в ⚙️ Администрирование',
            reply_markup=kb_admin
            )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text='Нет доступа')
        
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker=r'CAACAgIAAxkBAAEJtMtks8sbeOwMwVjhgqs7oqsyn3oyQQACbBQAAqhl2Unugzno4GtRUy8E')
        
async def ping(message: types.Message):
    await bot.send_message(
            chat_id=message.chat.id,
            text=f'Вы вошли в 🟢 Пингование',
            reply_markup=kb_ping)

async def ping_n1(message: types.Message):
    system(f'ping -c 1 {PING[0]} > temp')
    with open("temp") as f:
        pinglog = f.read()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'{pinglog}',
        parse_mode='HTML'
    )
    
async def ping_n2(message: types.Message):
    system(f'ping -c 1 {PING[0]} > temp')
    with open("temp") as f:
        pinglog = f.read()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'{pinglog}',
        parse_mode='HTML'
    )
    
async def ping_n3(message: types.Message):
    system(f'ping -c 1 {PING[0]} > temp')
    with open("temp") as f:
        pinglog = f.read()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'{pinglog}',
        parse_mode='HTML'
    )

async def attention(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Кому пишем?',
        reply_markup=kb_attention
    )        

@dp.message_handler(state=UserState.att)
async def att(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['att'] = message.text
        data = dict(data)
        data = data['att']
        
        await bot.send_message(
            chat_id=search_userids(),
            text=f'{data}',
            parse_mode='HTML')
        
    await state.finish()

async def att_set(message: types.Message):
    if message.chat.id == search_userids():
        await bot.send_message(
            chat_id=message.chat.id,
            text='Введите текст')
        await UserState.att.set()

async def pay(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Временно не работает'
        )
    
async def bots(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Временно не работает'
        )

async def support(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'По всем вопросам, недочетам и услугам\.',
        reply_markup=kb_support)
    await bot.send_video(
        chat_id=message.chat.id,
        video=r'https://s9.gifyu.com/images/animation042e91e4ca542b38.gif'
        )

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, Text(equals=['/start']))
    dp.register_message_handler(admin, Text(equals=['/admin', '/adm', '⚙️ Администрирование']))
    dp.register_message_handler(ping, Text(equals=['/ping', '🟢 Пингование']))
    dp.register_message_handler(ping_n1, Text(equals=['ping_n1']))
    dp.register_message_handler(ping_n2, Text(equals=['ping_n2']))
    dp.register_message_handler(ping_n3, Text(equals=['ping_n3']))
    dp.register_message_handler(attention, Text(equals=['/attention', '/att', '🔤 Написать']))
    dp.register_message_handler(att_set, Text(equals=['/attention_all', '/att_all', '🔤 Написать всем']))
    dp.register_message_handler(pay, Text(equals=['/payment', '/pay', '💵 Оплата услуг']))
    dp.register_message_handler(bots, Text(equals=['/bots', '/bots', '💎 Список ботов']))
    dp.register_message_handler(support, Text(equals=['/support', '💌 Связаться']))
    dp.register_message_handler(back, Text(equals=['/back', 'Назад']))
    
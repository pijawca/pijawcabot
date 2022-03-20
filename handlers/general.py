#!/venv/bin/python
# -*- coding: utf-8 -*-
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types
from misc import bot, dp
from handlers import some
from handlers.keyboard import kb_client, kb_support, kb_scripts, kb_work, kb_reviews
import config


class Work_(StatesGroup):
    design_ = State()
    develop_ = State()

async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет, @{message.from_user.username}\n'
             f' 〰️〰️〰️ Объявление 〰️〰️〰️',
        parse_mode='HTML',
        reply_markup=kb_client
    )
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker=r'CAACAgIAAxkBAAEEMtBiNGzzinwL50nFNJmc9NOKGM0hEwACFRIAAt4x2EvsSvY-iIfixiME'
    )

async def news(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Провожу парсинг, ожидайте.'
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'📰 Новости в категории "Интернет" от Яндекса:\n'
             f'🗞︎ ' + f'[{some.nt_t()}]({some.nt_l()})\n' + '🗞︎ ' + f'[{some.nt_t1()}]({some.nt_l1()})\n' + '🗞︎ ' + f'[{some.nt_t2()}]({some.nt_l2()})\n'
             f'🗞︎ ' + f'[{some.nt_t3()}]({some.nt_l3()})\n' + '🗞︎ ' + f'[{some.nt_t4()}]({some.nt_l4()})\n\n'
             f'📰 Новости в категории "Гаджеты" от Яндекса:\n'
             f'🗞︎ ' + f'[{some.ga_t()}]({some.ga_l()})\n' + '🗞︎ ' + f'[{some.ga_t1()}]({some.ga_l1()})\n' + '🗞︎ ' + f'[{some.ga_t2()}]({some.ga_l2()})\n'
             f'🗞︎ ' + f'[{some.ga_t3()}]({some.ga_l3()})\n' + '🗞︎ ' + f'[{some.ga_t4()}]({some.ga_l4()})\n',
        parse_mode=types.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker=r'CAACAgIAAxkBAAEEMqViNE_lESi_oz_Etgq6B3L6O2stjgAC6BIAAo9u0EvIU4PvGEDl0yME'
    )

async def my_bots(message: types.Message):
    if message.from_user.id == config.ID:
        await bot.send_message(
            chat_id=message.chat.id,
            text=(f'〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n'
                  f'💻 @radiophonebot\n'
                  f'#️⃣ <code>5228167605:AAHgEzuC80jt2EMWn6owB96YtbDMsP-e0K4</code>\n\n'
                  f'💻 @showmehidebot\n'
                  f'#️⃣ <code>2079326037:AAE4x1tE58fyCDHQjyjGPaOZ1EYHRxl2jpY</code>\n\n'
                  f'💻 @test_pijawcabot\n'
                  f'#️⃣ <code>2078270004:AAEIbZcpLyPpCge3x6wILYh5b2odZ9LrL2w</code>\n'
                  f'〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️'
            ),
            parse_mode=types.ParseMode.HTML
        )
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker=r'CAACAgIAAxkBAAEENL9iNYUmVoqgw0qcQo2DIP128JkzqgACdxcAAuvA-Uu2duhg_nfSDSME'
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=('Сорян братик, кодер сказал что сюда никого не впускать(')
        )

async def support(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='По любым вопросам.',
        reply_markup=kb_support
    )

async def back(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Вы в <strong>главном меню</strong>',
        reply_markup=kb_client,
        parse_mode=types.ParseMode.HTML
    )

async def scripts(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Вы в категории: <strong>💡 Скрипты</strong>',
        reply_markup=kb_scripts
    )

async def getid(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'ID: <code>{message.from_user.id}</code>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=kb_scripts
    )

async def work(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Вы в категории: <strong>💵 Услуги</strong>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=kb_work
    )
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker=r'CAACAgIAAxkBAAEENMFiNYVrVDP5WBxtkTzM-Lu5liX1mgACZhUAApT3cUi_JoscASYXoiME'
    )

async def reviews(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Отзывы о сотрудничестве со мною',
        reply_markup=kb_reviews
    )

'''
@
'''

async def design(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Отправьте ссылку на ТЗ в [Google Docs](https://docs.google.com/)',
        parse_mode=types.ParseMode.MARKDOWN_V2
    )
    await Work_.design_.set()

@dp.message_handler(state=Work_.design_)
async def design_set(message: types.Message, state: FSMContext):
    if message.text.startswith('https://docs.google.com/document/d'):
        async with state.proxy() as data:
            data['design_set'] = message.text
            data = dict(data)
            data = data['design_set']
            await state.finish()
        await message.reply(
            text=f'Заявка создана, ожидайте ответа от исполнителя\\.\n\n'
            f'📌 Разработка дизайна\n'
            f'📰 Никнейм: @{message.from_user.username} \\| ID: {message.from_user.id}\n'
            f'📌 Ссылка на ТЗ: [Перейти]({data})\n'
            f'💵 Цена услуги: **Неизвестно**\n\n', # todo
            parse_mode=types.ParseMode.MARKDOWN_V2,
            reply_markup=kb_support
        )
        await bot.send_message(
            chat_id=config.ID,
            text=f'📌 Разработка дизайна\n'
            f'📰 Никнейм: @{message.from_user.username} \\| ID: {message.from_user.id}\n'
            f'📌 Ссылка на ТЗ: [Перейти]({data})\n'
            f'💵 Цена услуги: **Неизвестно**',  # todo
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'Ссылка должна быть строго на файл в **Google Drive\\!**',
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
        await state.finish()

async def develop(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Отправьте ссылку на ТЗ в [Google Docs](https://docs.google.com/)',
        parse_mode=types.ParseMode.MARKDOWN_V2
    )
    await Work_.develop_.set()

@dp.message_handler(state=Work_.develop_)
async def design_set(message: types.Message, state: FSMContext):
    if message.text.startswith('https://docs.google.com/document/d'):
        async with state.proxy() as data:
            data['develop_set'] = message.text
            data = dict(data)
            data = data['develop_set']
            await state.finish()
        await message.reply(
            text=f'Заявка создана, ожидайте ответа от исполнителя\\.\n\n'
            f'📌 Разработка бота\n'
            f'📰 Никнейм: @{message.from_user.username} \\| ID: {message.from_user.id}\n'
            f'📌 Ссылка на ТЗ: [Перейти]({data})\n'
            f'💵 Цена услуги: **Неизвестно**', # todo
            parse_mode=types.ParseMode.MARKDOWN_V2,
            reply_markup=kb_support
        )
        await bot.send_message(
            chat_id=config.ID,
            text=f'📌 Разработка дизайна\n'
            f'📰 Никнейм: @{message.from_user.username} \\| ID: {message.from_user.id}\n'
            f'📌 Ссылка на ТЗ: [Перейти]({data})\n'
            f'💵 Цена услуги: **Неизвестно**\n\n',  # todo
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'Ссылка должна быть строго на файл в **Google Drive\\!**',
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
        await state.finish()


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, Text(equals=['/start', '🔃 Обновить']))
    dp.register_message_handler(news, Text(equals=['/news', '📰 Новости']))
    dp.register_message_handler(my_bots, Text(equals=['/my_bots', '⚙️ Администрирование']))
    dp.register_message_handler(support, Text(equals=['/support', '👽️ Поддержка']))
    dp.register_message_handler(scripts, Text(equals=['/scripts', '💡 Скрипты']))
    dp.register_message_handler(back, Text(equals=['/back', 'Назад']))
    dp.register_message_handler(getid, Text(equals=['/getid', 'Получить ID']))
    dp.register_message_handler(work, Text(equals=['/work', '💵 Услуги']))
    dp.register_message_handler(design, Text(equals=['/design', 'Заказать дизайн']))
    dp.register_message_handler(develop, Text(equals=['/develop', 'Заказать разработку бота']))
    dp.register_message_handler(reviews, Text(equals=['/reviews', '🤝🏻 Отзывы']))

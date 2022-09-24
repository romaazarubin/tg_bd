from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from main import dp, bot
from config import support_id, POSTGRES_URL,DATABASE,PG_USER,PG_PASSWORD, ip
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import psycopg2
from keyboard import menu_application, button_client_help, button_sity
db_connection = psycopg2.connect(dbname=DATABASE, user=PG_USER, password=PG_PASSWORD, host=ip)
cursor = db_connection.cursor()

@dp.message_handler(Command('start'))
async def start(message: Message):
    if message.chat.id != -763455375 and message.from_user.id not in support_id:
        await bot.send_message(chat_id=message.from_user.id, text='/menu - Вызов меню')




@dp.message_handler(Command('menu'))
async def menu(message: Message):
     if message.chat.id != -763455375 and message.from_user.id not in support_id:
        await bot.send_message(chat_id=message.from_user.id, text='Выберите город для обращение к менеджеру', \
                               reply_markup=button_sity)



@dp.callback_query_handler(Text(equals=['Moskva', 'SPB', 'Irkutsk']))
async def help(call: CallbackQuery):
    await call.message.delete()
    nick = call.from_user.username
    cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT nick FROM us_id WHERE nick = '{nick}') THEN 1 ELSE 2 END;")
    row = cursor.fetchone()
    if row == 1:
        cursor.execute(f"INSERT INTO us_id(nick) VALUES ('{nick}');")
        db_connection.commit()
    else:
        cursor.execute(f"DELETE FROM us_id WHERE nick='{nick}'")
        cursor.execute(f"INSERT INTO us_id(nick) VALUES ('{nick}');")
        db_connection.commit()
    await bot.send_message(chat_id=-763455375, text=nick, reply_markup=menu_application)

@dp.callback_query_handler(text_contains='answer')
async def ans(call: CallbackQuery):
    cursor.execute(f'SELECT nick FROM us_id LIMIT 1')
    db_connection.commit()
    z = cursor.fetchall()

    for i in z:
        name = i[0]

    url = 'https://t.me/' + str(name)

    cursor.execute(f"DELETE FROM us_id WHERE nick='{name}'")
    db_connection.commit()


    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id, text=url)
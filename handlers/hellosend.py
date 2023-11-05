from create_bot import dp,bot 
from aiogram import types,Dispatcher
from .startkb import kb

async def starting_bot(message:types.Message):
    

    await message.answer(f'Hi {message.from_user.first_name}!',reply_markup=kb)


def register_handlers_hs(dp: Dispatcher):
    dp.register_message_handler(starting_bot,commands=['start'])
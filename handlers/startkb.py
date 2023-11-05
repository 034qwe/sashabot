from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types,Dispatcher
from create_bot  import dp,bot 

us_flag_emoji = '🇺🇸'
ch_flag_emoji = '🇨🇳'
gr_flag_emoji ='🇩🇪'
gb_flag_emoji = '🇬🇧'
ru_flag_emoji = '🇷🇺'
br_flag_emoji = '🇧🇷'
sw_flag_emoji = '🇨🇭'
pl_flag_emoji = '🇵🇱'

kb = InlineKeyboardMarkup(row_width=3)

butt1 = InlineKeyboardButton(text=f'Germany{gr_flag_emoji}',callback_data='change_uk')
butt2 = InlineKeyboardButton(text=f'USA{us_flag_emoji}',callback_data='change_uk')
butt3= InlineKeyboardButton(text=f'Brazil{br_flag_emoji}',callback_data='change_uk')
butt4 = InlineKeyboardButton(text=f'Russia{ru_flag_emoji}',callback_data='change_uk')
butt5 = InlineKeyboardButton(text=f'China{ch_flag_emoji}',callback_data='change_uk')
butt6 = InlineKeyboardButton(text=f'switzerland{sw_flag_emoji}',callback_data='change_uk')
butt7 = InlineKeyboardButton(text=f'Poland{pl_flag_emoji}',callback_data='change_uk')
butt8 = InlineKeyboardButton(text=f'British{gb_flag_emoji}',callback_data='change_uk')

kb.add(butt1,butt2,butt3)
kb.add(butt4,butt5,butt6)
kb.add(butt8,butt7)



async def sendhref(callback:types.CallbackQuery):
    await callback.message.answer('0x27D515EBbFe2Df6fe53DF173A92d38F602BDbAba')
    await callback.answer('caня пісюн')

def register_handlers_langkb(dp:Dispatcher):
    dp.register_callback_query_handler(sendhref,text='change_uk')
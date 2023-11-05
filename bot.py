from aiogram.utils import executor
from create_bot import dp
from handlers import hellosend,startkb


async def on_startup(_):
    print('bot start')

hellosend.register_handlers_hs(dp)
startkb.register_handlers_langkb(dp)


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
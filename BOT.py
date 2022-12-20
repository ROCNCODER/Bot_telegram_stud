from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other

async def on_start():
    print("bot start")

client.register_handlers_client(dp)


executor.start_polling(dp)



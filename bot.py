import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '6265398487:AAF9v30HjApTxhvVQfYO8_0FtZUbTerkkZk'
BASE_URL = 'https://api.telegram.org/bot'
ADMINS_ID = [489153473, ]

logging.basicConfig(level=logging.INFO)
proxy_url = 'http://proxy.server:3128'
bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.answer('Вы ввели команду старт')
    print('Hello')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

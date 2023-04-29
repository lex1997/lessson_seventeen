import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

TOKEN = '6265398487:AAF9v30HjApTxhvVQfYO8_0FtZUbTerkkZk'
WEBHOOK_HOST = 'https://3268-188-17-148-240.ngrok-free.app'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 8000

BASE_URL = 'https://api.telegram.org/bot'
ADMINS_ID = [489153473, ]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, 'Вы открыли справку')

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

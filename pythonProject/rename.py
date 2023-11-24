from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import Config

TOKEN = Config.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет! Я новый бот от trrb7. Пока что ты можешь написать только "/start".'
                                             'Но скоро у меня будут новые комнады!')

if __name__ == '__main__':
    executor.start_polling(dp)
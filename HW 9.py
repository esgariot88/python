from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5721347587:AAG7qqlmp_RkJq4PcOV72Qdc240fyrThDO4'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ну наконец-то")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Почему не работает telebot?")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

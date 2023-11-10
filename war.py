from aiogram import Dispatcher,Bot,executor,types


token = '6285439502:AAHHGt7agh_RIuUfgTFxL0GO4Qipti0ZwaE'

bot_5 = Bot(token=token)
dp = Dispatcher(bot=bot_5)









@dp.message_handler(commands=['card'])
async def cardxd_(msg: types.Message):
    await msg.answer('*Оплатить можно*: \n \n \n 💳`2200 7008 9214 2893` \n _Номер копируется при нажатии_', parse_mode='Markdown')








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

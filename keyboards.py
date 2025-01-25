from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton





def wel():
   x = ReplyKeyboardMarkup(resize_keyboard=True)
   #x.add(KeyboardButton(text='Профиль'))
   
   x.add(KeyboardButton(text='Кабинет администратора'))
   
   #x.add(KeyboardButton(text='Связь с администрацией'))
   
   
   return x




def casses():
   x = InlineKeyboardMarkup()
   x5 = InlineKeyboardButton(text='Создать набор', callback_data='set_cases')

   x6 = InlineKeyboardButton(text='Управление набором', callback_data='cases_')

   #x.add(KeyboardButton(text='Назад'))
   x.add(x5,x6)
   return x

def casses_():
   x = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
   x.add(KeyboardButton(text='Авито'))
   x.add(KeyboardButton(text='Яндекс Карты'))
   #x.add(KeyboardButton(text='Яндекс.Услуги'))
   x.add(KeyboardButton(text='2ГИС'))
   x.add(KeyboardButton(text='Google Maps'))



   return x

def casses_5():
   x = InlineKeyboardMarkup()
   x5 = InlineKeyboardButton(text='Авито', callback_data='answer_Авито')
   x555 = InlineKeyboardButton(text='Яндекс Карты', callback_data='answer_Яндекс Карты')
   x9 = InlineKeyboardButton(text='2ГИС', callback_data='answer_2ГИС')
   x999 = InlineKeyboardButton(text='Google Maps', callback_data='answer_Google Maps')
   x666 = InlineKeyboardButton(text='другая платформа' , callback_data='answer_other')
   x.add(x5,x555).add(x9,x999).add(x666)

   return x


def sendx():
   x = InlineKeyboardMarkup()
   x5 = InlineKeyboardButton(text='🔸 Отправить 🔸', callback_data='starts_')
   x6 = InlineKeyboardButton(text='🔸 Закрыть 🔸', callback_data='starts%')




   r = InlineKeyboardButton(text='🔙 Назад', callback_data='starts-')
   x.add(x5, x6).add(r)

   
   return x


def urlsr_():

   x = InlineKeyboardMarkup()
   x5 = InlineKeyboardButton(text='Как начать работу?', url='https://telegra.ph/Kak-nachat-rabotu-06-06')
   x55 = InlineKeyboardButton(text='Выплаты', url='https://t.me/shardopl')
   x555 = InlineKeyboardButton(text='Рефералка', url='https://t.me/shardreferrals_bot')

   x.add(x5).add(x55,x555)

   return x

def archives():

   x = InlineKeyboardMarkup()
   x5 = InlineKeyboardButton(text='Авито', url='https://telegra.ph/Manual-po-Avito-ot-DandBy-03-03')
   x55 = InlineKeyboardButton(text='2ГИС', url='https://telegra.ph/Poisk-zakazchikov-na-2GIS-03-03')
   x3 = InlineKeyboardButton(text='Негатив Авито', url='https://telegra.ph/Negativnyj-otzyv-ot-DandBy-03-03')
   x33 = InlineKeyboardButton(text='Как выйти в доход?', url='https://telegra.ph/Perestayom-zavisit-ot-roditelej-i-nachat-cenit-dengi-03-03')
   x53 = InlineKeyboardButton(text='Отзывы яндекс карт', url='https://telegra.ph/Poisk-zakazchikov-na-YAndeks-Kartah-03-03')
   
   x.add(x5,x55,x3,x33,x53)

   return x

def otk(userid):
   row = InlineKeyboardMarkup()
   rows = InlineKeyboardButton(text='Откликнуться', url=f'https://t.me/{userid}')
   row.add(rows)

   return row


def cansel5():
    s = InlineKeyboardMarkup()
    row = InlineKeyboardButton(text='Отмена', callback_data=f'cansel5')
    s.add(row)

def stttttt(userid):
   s = InlineKeyboardMarkup()
   rows = InlineKeyboardButton(text='Добавить админа', callback_data=f'admins_{userid}')
   rows_ = InlineKeyboardButton(text='удалить из админов', callback_data=f'remove_{userid}')
   s5 = InlineKeyboardButton(text='Отмена', callback_data='cansel5')
   s.add(rows,rows_,s5)

   return s

def otttttt():
   s = InlineKeyboardMarkup()
   s5 = InlineKeyboardButton(text='Отмена', callback_data='otmena')

   s.add(s5)

   return s


def ads_55():
   x = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
   x.add(KeyboardButton(text='Список Админов'))
   x.add(KeyboardButton(text='Начать рассылку'))
   x.add(KeyboardButton(text='Поиск Пользователя по нику'))
   x.add(KeyboardButton(text='/start'))
  
   return x
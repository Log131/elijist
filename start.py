from aiogram import Dispatcher,Bot,executor,types

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import link
from aiogram.dispatcher import FSMContext
from keyboards import *
import datetime
import asyncio
from datas import *

import datetime


#token = '6688184356:AAHnpDSf6p9JU0EtXL_S3NMs4pd89m5QsaM'




token = '6816427189:AAFJWYBA8tDx1psz5nUZ1CXpZAGqcwk-XQw'

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=['start'])
async def startx(msg: types.Message): 
    if msg.from_user.username is None:
        await msg.answer(' ``` Добавьте пожалуйста никнейм в настройках ``` ', parse_mode='Markdown') 
    else:
        await state_5(userid=msg.from_user.id,username=msg.from_user.username,first_name=msg.from_user.first_name)
        s = await get_prem(msg.from_user.id)
        if s == '0' or s is None:
            await msg.answer('*В данный момент у вас нет доступа к нашему боту!* 😔\nЧтобы это исправить, обратитесь за покупкой админки к @elijist',parse_mode='Markdown')
        else:
            await msg.answer(text='*Приветствую, админ!*\nПерейдите в «Кабинет администратора» по кнопке ниже, чтобы управлять наборами',parse_mode='Markdown', reply_markup=wel())
                
            
@dp.message_handler(text='Кабинет администратора')
async def nabors(msg: types.Message):
    s = await get_prem(msg.from_user.id)
    if s == '0' or s is None:
        await msg.answer('*В данный момент у вас нет доступа к нашему боту!* 😔\nЧтобы это исправить, обратитесь за покупкой админки к @elijist',parse_mode='Markdown')
    else:

        await msg.answer_photo(photo='https://i.yapx.ru/YWL7C.png',caption='*👨🏼‍💻 Кабинет администратора:*\n\nИспользуя кнопки ниже, вы можете создавать и закрывать наборы на задания ',parse_mode='Markdown', reply_markup=casses())

class cases(StatesGroup):

    cases_ = State()
    price = State()
    usersc = State()
    other_ = State()

class adminadd(StatesGroup):
    add_xdx = State()
    
    timex_ = State()

class get_spam(StatesGroup):
    spam_start = State()
class del_admins(StatesGroup):
    del_ads = State()

class searches_(StatesGroup):
    search_start = State()

@dp.callback_query_handler(text='set_cases')
async def statex(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    s = await get_prem(css.from_user.id)
    try:
        if s == '0' or s is None:
            await css.message.answer('*В данный момент у вас нет доступа к нашему боту!* 😔\nЧтобы это исправить, обратитесь за покупкой админки к @elijist',parse_mode='Markdown')
        else:
            await css.message.answer(text='*На какую платформу создать набор?* \n\nВыберите по кнопкам либо введите название вручную',parse_mode='Markdown', reply_markup=casses_5())
            await cases.cases_.set()
        
    except:
        await state.finish()
        
        
    


#@dp.message_handler(state=cases.cases_)
@dp.callback_query_handler(text_contains='answer_', state=cases.cases_)
async def state_(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    data = css.data.split('_')
    if data[1] != 'other':
        try:
            await state.update_data(cases_=data[1])

            await state.set_state(cases.price)
    
            await css.message.answer(f'*▸ Платформа:* {data[1]} \n \nВведите оплату за отзыв', parse_mode='Markdown')
        except:
            await state.finish()
    else:
        await css.message.answer('Напишите название платформы')
        await state.set_state(cases.other_)



@dp.message_handler(state=cases.other_)
async def state__(msg: types.Message, state: FSMContext):
    await state.update_data(cases_=msg.text)
    await state.set_state(cases.price)
    await msg.answer(f'*▸ Платформа:* {msg.text} \n \nВведите оплату за отзыв', parse_mode='Markdown')

@dp.message_handler(state=cases.price)
async def state__(msg: types.Message, state: FSMContext):
        try:
            await state.update_data(price=msg.text)
            await state.set_state(cases.usersc)

            s = await state.get_data()
            await msg.answer(f"*▸ Платформа: {s.get('cases_')} \n▸ Оплата: {msg.text}*₽ \n\nВведите описание к набору",parse_mode='Markdown')
            #await msg.answer('Введите описание к набору')
        
        except Exception as e:
            print(e)
            await state.finish()
            await msg.answer('Ошибка')

@dp.message_handler(state=cases.usersc)
async def state_(msg: types.Message, state: FSMContext):
    
    data = await state.get_data()

    
    
    try:
        await update_datas(cases=data['cases_'],price=data['price'],usersc=msg.text,userid=msg.from_user.id)
         
        await msg.answer(f'*▸ Платформа: {data.get("cases_")} \n▸ Получите оплату: {data.get("price")}₽ \n▸ Описание: {msg.text} \n \n★ Писать: @{msg.from_user.username}* \n☆ Наши выплаты: @SHARDopl', reply_markup=sendx(), parse_mode='Markdown') 
        await state.finish()
    except Exception as e:
        print(e)
        
        await state.finish()
        await msg.answer('Введите целое число')
    
    


@dp.callback_query_handler(text='cases_')
async def check_cases(css: types.CallbackQuery):
    await css.answer()
    datas = await select_any(css.from_user.id)
    s =  await get_prem(css.from_user.id)
    if s == '0' or s is None:
        await css.message.answer('*В данный момент у вас нет доступа к нашему боту!* 😔\nЧтобы это исправить, обратитесь за покупкой админки к @elijist',parse_mode='Markdown')
    else:
        if datas[1] is None:
            await css.message.answer('*У вас нет активных наборов!* 🤔\nЧтобы создать набор, нажмите на кнопку ниже',parse_mode='Markdown', reply_markup=casses())
        else:
            await css.message.answer(f'*▸ Платформа: {datas[1]} \n▸ Получите оплату: {datas[2]}₽ \n▸ Описание: {datas[4]} \n \n★ Писать: @{css.from_user.username}* \n☆ Наши выплаты: @SHARDopl', reply_markup=sendx(), parse_mode='Markdown')


#@router.message(F.text == ('Назад'))
#async def swelx_(msg: types.Message):
        #await msg.answer('🎉', reply_markup=wel())
        #await msg.delete()




#@router.message(F.text==('Профиль'))
#async def profile(msg: types.Message):
       # s = await get_prem(msg.from_user.id)
        #if s is None:
            #await msg.answer_photo(photo='https://i.yapx.ru/XG8zz.png',caption=f' Добро пожаловать!\nИнформация о вашем профиле:\n \n➖ ➖ ➖ ➖ ➖ \n ID: {msg.from_user.id} \n Ваш статус: исполнитель\n➖ ➖ ➖ ➖ ➖', parse_mode='Markdown')
            
        #else:
            #await msg.answer_photo(photo='https://i.yapx.ru/XG8zz.png',caption=f' Добро пожаловать!\nИнформация о вашем профиле:\n \n➖ ➖ ➖ ➖ ➖ \n ID: {msg.from_user.id} \n Ваш статус: администратор\n➖ ➖ ➖ ➖ ➖', parse_mode='Markdown')
            





@dp.callback_query_handler(text='starts_')
async def sendx_(css: types.CallbackQuery):
    await css.answer()
    datas = await select_any(css.from_user.id)
    s_ = await get_prem(css.from_user.id)
    get_ = await get_new_iff(css.from_user.id)
    if s_ == '0' or s_ is None:
        pass
    elif get_ == 5:
        await css.message.answer('*У вас уже есть открытый набор!*\nПеред публикацией нового, перейдите в «Управление набором» и закройте предыдущий',  parse_mode='Markdown')
    elif datas[1] is None:
        await css.message.answer('*В данный момент у вас нет наборов для отправки!*\nЧтобы открыть набор, перейдите в «Кабинет администратора»и создайте набор на задание', parse_mode='Markdown')
    else:
        #1001892774322
        #1002296257073
        s = await bot.send_message(chat_id=-1001892774322, text=f' *▸ Платформа: {datas[1]} \n▸ Получите оплату: {datas[2]}₽ \n▸ Описание: {datas[4]} \n \n★ Писать: @{css.from_user.username}* \n☆ Наши выплаты: @SHARDopl', parse_mode='Markdown', reply_markup=otk(css.from_user.username))
                
        unix_time = datetime.datetime.now() + datetime.timedelta(minutes=90)
        unix_time5 = int(unix_time.timestamp())

        await set_iff(msgid=s.message_id,unix=unix_time5,userid=css.from_user.id)
        await update_sedns(sends=5,userid=css.from_user.id)
        await css.answer('Ваш набор открылся ☑️', show_alert=True)


@dp.callback_query_handler(text='starts%')
async def sendx_555(css: types.CallbackQuery):
    sends = await get_sends(css.from_user.id)
    await bot.edit_message_text(text=f'🔒 *Данное задание закончилось.*\n*Дождитесь нового, чтобы приступить к работе*\n\nНажмите на кнопку «Как начать работу?», чтобы ознакомиться\nс бесплатным обучением заработку',chat_id=-1001892774322, message_id=sends, parse_mode='Markdown',disable_web_page_preview=True, reply_markup=urlsr_())
    await upt_(css.from_user.id)
    await update_sedns(sends=1,userid=css.from_user.id)
    await css.answer('Удалено')


@dp.callback_query_handler(text='starts-')
async def sendx_5(css: types.CallbackQuery):
    await css.answer()
    await css.message.answer_photo(photo='https://i.yapx.ru/YWL7C.png',caption='*👨🏼‍💻 Кабинет администратора:*\n\nИспользуя кнопки ниже, вы можете создавать и закрывать наборы на задания ',parse_mode='Markdown', reply_markup=casses())



@dp.message_handler(commands='admin')
async def ads_(msg: types.Message):
    if msg.from_user.id == 686674950 or msg.from_user.id == 1624519308:
        await msg.answer('Вы админ', reply_markup=ads_55())
    
    
    
    
    
    else:
        await msg.answer('Отказано')




@dp.message_handler(text='Поиск Пользователя по нику', state=None) 
async def search_(msg: types.Message, state: FSMContext):
    try:
        if msg.from_user.id == 686674950 or msg.from_user.id == 1624519308:
            await msg.answer('Введите ник Пользователя без @', reply_markup=cansel5())
            await state.set_state(searches_.search_start)
    except Exception as e:
        pass





@dp.message_handler(state=searches_.search_start)
async def state_search(msg: types.Message, state: FSMContext):
    try:
        async with aiosqlite.connect('teg.db') as tc:
            async with tc.execute('SELECT username FROM users WHERE username = ?', (msg.text,)) as t:
                x = await t.fetchone()
            async with tc.execute('SELECT * from users WHERE username = ?', (x[0],)) as t_:
                s = await t_.fetchone()
            await msg.answer(f'ID : {s[0]}\n nickname : @{s[5]} \n firstname: {s[6]} \n Время : {s[7]} \n Осталось: {s[8]}', reply_markup=stttttt(s[0]))
            await msg.answer('Главное меню', reply_markup=ads_55())
            await state.finish()
    except Exception as e:
        await msg.answer('Такого нет')
        await state.finish()
        print(e)

@dp.callback_query_handler(state='*', text='cansel5')
async def canels(css: types.CallbackQuery, state: FSMContext):
        await css.answer()
        await state.finish()
        await css.message.answer('Отменено!', reply_markup=ads_55())



@dp.message_handler(text='Список Админов')
async def admins_(msg: types.Message):
    try:
        row = InlineKeyboardMarkup()
        if msg.from_user.id == 686674950 or msg.from_user.id == 1624519308:
            
            async with aiosqlite.connect('teg.db') as tc:
                async with tc.execute('SELECT * FROM users') as t:
                    x = await t.fetchall()
            for s in x:
                rows = InlineKeyboardButton(text=f'@{s[5]} - {s[8]}', callback_data=f'add_@{s[0]}')
                    
                    
                row.add(rows)
            await msg.answer('Список админов', reply_markup=row)
        else:
            pass
    except:
        pass


@dp.message_handler(text='Начать рассылку', state=None)
async def spam_strsx(msg: types.Message, state: FSMContext):
    if msg.from_user.id == 686674950 or msg.from_user.id == 1624519308:
        await msg.answer('Начинаем рассылку введите текст рассылки', reply_markup=cansel5())
        await state.set_state(get_spam.spam_start)


@dp.message_handler(state=get_spam.spam_start)
async def stam_it(msg: types.Message, state: FSMContext):
    try:
        async with aiosqlite.connect('teg.db') as tc:
            async with tc.execute('SELECT user_id FROM users') as t:
                s = await t.fetchall()
            for sends in s:
                try:
                    await bot.send_message(chat_id=sends[0], text=msg.text)
                except Exception as e:
                    print(e)
            await msg.answer('Рассылено', reply_markup=ads_55())
            await state.finish()
    except Exception as e:
        print(e)


@dp.callback_query_handler(text_contains='add_@')
async def add_ads_(css: types.CallbackQuery):

    rowsr = InlineKeyboardMarkup()
    rows_s = InlineKeyboardButton(text='Отмена', callback_data='otmena')
    try: 
        async with aiosqlite.connect('teg.db') as tc:
            async with tc.execute('SELECT * FROM users WHERE user_id = ?', (int(css.data[5:]),)) as t:
                v = await t.fetchall()
        for s in v:
            rows = InlineKeyboardButton(text='Добавить в админы', callback_data=f'admins_{s[0]}')
            rows_ = InlineKeyboardButton(text='Удалить из админов', callback_data=f'remove_{s[0]}')
            rowsr.add(rows,rows_).add(rows_s)
            await css.message.answer(f'ID : {s[0]}\n User: @{s[5]} \n Время : {s[7]} \n Осталось: {s[8]}', reply_markup=rowsr)
    
    
    
    
    except:
        pass








@dp.callback_query_handler(text='otmena')
async def adsadsa(css: types.CallbackQuery):
    
    await css.message.delete()




@dp.callback_query_handler(text_contains='admins_', state=None)
async def state_ads_(css: types.CallbackQuery, state: FSMContext):
    
    try:
        s = css.data.split('_')
        #int(css.data[7:]
        await state.update_data(add_xdx=s[1])
    
    
    
        await css.message.answer('Напишите время админки (Дни)', reply_markup=cansel5()) 


    
        await state.set_state(adminadd.add_xdx)
    except:

        await css.message.answer('Введите число или отмена')






@dp.message_handler(state=adminadd.add_xdx)
async def state_ads______(msg: types.Message, state: FSMContext):
    
    
    
    try:
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        time_delete = (datetime.datetime.now() + datetime.timedelta(days=int(msg.text))).strftime('%Y-%m-%d %H:%M')
        
        data = await state.get_data()
        s = await select_any(int(data['add_xdx']))
        async with aiosqlite.connect('teg.db') as tc:
            await tc.execute('UPDATE rat SET username = ?, username_admin = ?, time_now = ?, time_delete = ? WHERE user_id = ?', (s[5], msg.from_user.username,time_now, time_delete, int(data['add_xdx']),))
            await tc.execute('UPDATE users SET time_now = ?, time_delete = ? WHERE user_id = ?', (time_now, time_delete, int(data['add_xdx']),))
                    
            await tc.commit()
                
            await msg.answer('Добавлено!')
            await state.finish()
        async with aiosqlite.connect('teg.db') as tc:
            async with tc.execute('SELECT username FROM users WHERE user_id = ?', (int(data['add_xdx']),)) as t:
                srs = await t.fetchone()
        #await bot.send_message(chat_id=686674950, text=f'@{msg.from_user.username} Добавил - @{srs[0]} На {msg.text} Дней')
        await bot.send_photo(photo='https://i.yapx.ru/YWL8H.png',caption='🎉 *Вам выдали админку!*\n\nДобро пожаловать в семью SHARD',chat_id=int(data['add_xdx']),parse_mode='Markdown',reply_markup=casses())
    
    except Exception as e:
        print(e)
        await state.finish()
        await msg.answer('Введите число')







@dp.callback_query_handler(text_contains='remove_')
async def remove_it(css: types.CallbackQuery):
    s = css.data.split('_')
    try:
        async with aiosqlite.connect('teg.db') as tc:
            async with tc.execute('SELECT username FROM users WHERE user_id = ? ', (int(s[1]),)) as t:
                srs = await t.fetchone()
        await bot.send_message(chat_id=686674950, text=f'@{css.from_user.username} Удалил @{srs[0]} Из админов')
        async with aiosqlite.connect('teg.db') as tc:
                await tc.execute('DELETE FROM users WHERE user_id = ?', (int(s[1]),))
                await tc.commit()
        async with aiosqlite.connect('teg.db') as tc:
            await tc.execute('DELETE FROM new_iff WHERE user_id = ?', (int(s[1]),))
            await tc.commit()
        try:
            await bot.send_message(chat_id=int(s[1]), text='*Ваша админка закончилась или была снята!*\nЧтобы продлить доступ, обратитесь к @elijist',parse_mode='Markdown')
        except Exception as e:
            print(e)
    

        await css.message.answer('Удален')
        
    except Exception as e:
        print(e)
        await css.message.answer('Чтото пошло не так')




if __name__ == '__main__':
    s = asyncio.get_event_loop()
    s.run_until_complete(state_tttttt())
   
    executor.start_polling(dp, skip_updates=True)
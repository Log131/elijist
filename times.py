from datas import *

import schedule

import datetime
from start import bot
import asyncio
import time
from keyboards import urlsr_




async def check_s():
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT user_id,first_name,time_delete,username FROM users') as t:
            s = await t.fetchall()
        
        time_x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        for xdx in s:
            try:
                if xdx[2] is None or xdx[2] == 0:
                    pass
                else:
                    if datetime.datetime.now() >= datetime.datetime.strptime(xdx[2], '%Y-%m-%d %H:%M'):
                        try:
                            await bot.send_message(chat_id=xdx[0], text='*Ваша админка закончилась или была снята!*\nЧтобы продлить доступ, обратитесь к @elijist',parse_mode='Markdown')
                        except Exception as e:
                            print(e)
                        
                        
                        
                        
                        
                        #await bot.send_message(chat_id=6203509782, text=f'У пользователя : @{xdx[3]} - {xdx[1]} ID - {xdx[0]} Закончилась Админка')
                        async with aiosqlite.connect('teg.db') as tc:
                            await tc.execute('DELETE FROM users WHERE user_id = ?', (xdx[0],))
                            await tc.commit()
                        await delete_iff(xdx[0])
            except Exception as e:
                print(e)

async def check_():
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT user_id,time_delete FROM users') as t:
            s = await t.fetchall()
    
    for xdx in s:
        try:
            if xdx[1] is None or xdx[1] == 0:
                pass
            else:
                try:
                    if datetime.datetime.now() >= datetime.datetime.strptime(xdx[1], '%Y-%m-%d %H:%M') - datetime.timedelta(days=1) or datetime.datetime.now() >= datetime.datetime.strptime(xdx[1], '%Y-%m-%d %H:%M') - datetime.timedelta(minutes=30):
                        try:
                            await bot.send_message(chat_id=xdx[0], text='*Ваша админка закончилась или была снята!*\nЧтобы продлить доступ, обратитесь к @elijist',parse_mode='Markdown')
                        except Exception as e:
                            print(e)
                except:
                    pass
        
        
        
        
        except Exception as e:
            print(e)

async def update_msg():
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT sends, sends_,user_id FROM iff') as f:
            s = await f.fetchall()
        try:
            for i in s:
                try:
                    if i[1]:
                        unixtime = datetime.datetime.fromtimestamp(i[1])
                        if datetime.datetime.now() >= unixtime:
                            await update_datas(cases=None,price=None,usersc=None,userid=i[2])
                            await update_sedns(sends=1,userid=i[2])
                            await bot.edit_message_text(text=f' 🔒 *Данное задание закончилось.*\n *Дождитесь нового, чтобы приступить к работе*\n\nНажмите на кнопку «Как начать работу?», чтобы ознакомиться\nс бесплатным обучением заработку',chat_id=-1001892774322, message_id=i[0], parse_mode='Markdown',disable_web_page_preview=True, reply_markup=urlsr_())
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)



def funcs_5():
    s = asyncio.get_event_loop()
    s.run_until_complete(check_s())

schedule.every(99).seconds.do(funcs_5)


def funcs_6():
    s = asyncio.get_event_loop()
    s.run_until_complete(update_msg())

schedule.every(5).seconds.do(funcs_6)

while True:
    schedule.run_pending()
    time.sleep(5)
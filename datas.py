import aiosqlite



async def state_tttttt():
    async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS rat(user_id PRIMARY KEY, username, username_admin, time_now, time_delete)')
        await tc.execute('CREATE TABLE IF NOT EXISTS iff(user_id PRIMARY KEY, sends, sends_)')
        await tc.execute('CREATE TABLE IF NOT EXISTS new_iff(user_id PRIMARY KEY, sends, sends_)')
        await tc.execute('CREATE TABLE IF NOT EXISTS users(user_id PRIMARY KEY, cases_, price, zametka, usersc, username, war DEfAULT 0, time_now, time_delete, first_name)')
        await tc.commit()




async def get_prem(userid):
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT time_delete FROM users WHERE user_id = ?', (userid,)) as f:
            s = await f.fetchone()
        if s[0]:
            return s[0]
        else:
            return None


async def get_iff(userid):
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT sends FROM iff WHERE user_id = ?', (userid,)) as f:
            s = await f.fetchone()
        if s[0]:
            return s[0]
        else:
            return None

async def get_new_iff(userid):
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT sends FROM new_iff WHERE user_id = ?', (userid,)) as f:
            s = await f.fetchone()
        if s[0]:
            return s[0]
        else:
            return None


async def delete_iff(userid):
    async with aiosqlite.connect('teg.db') as tc:
            await tc.execute('DELETE FROM new_iff WHERE user_id = ?', (userid,))
            await tc.commit()


async def update_sedns(sends,userid):
     async with aiosqlite.connect('teg.db') as tc:
            await tc.execute('UPDATE new_iff SET sends = ?  WHERE user_id = ?', (sends,userid,))
            await tc.commit()



async def update_datas(cases, price, usersc, userid):
     async with aiosqlite.connect('teg.db') as tc:
            await tc.execute('UPDATE users SET cases_ = ?, price = ?, usersc = ?  WHERE user_id = ?', (cases,price,usersc, userid,))
            await tc.commit()






async def select_any(userid):
    async with aiosqlite.connect('teg.db') as tc:
        async with tc.execute('SELECT * FROM users WHERE user_id = ?',(userid,)) as f:
            datas = await f.fetchone()
        return datas


async def upt_(userid):
    async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('UPDATE users SET cases_ = ?, price = ?, zametka = ?, usersc = ? WHERE user_id = ?',(None, None, None, None, userid,))
        await tc.commit()

async def set_iff(msgid,unix,userid):
     async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('UPDATE iff SET sends = ?, sends_ = ? WHERE user_id = ?', (msgid,unix,userid,))
        await tc.commit()

async def get_sends(userid):
     async with aiosqlite.connect('teg.db') as tc:
          async with tc.execute('SELECT sends FROM iff WHERE user_id = ?', (userid,)) as f_:
              sends = await f_.fetchone()
              if sends[0]:
                  return sends[0]
              else:
                  return None

async def state_5(userid,username,first_name):
    async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO new_iff(user_id,sends) VALUES(?, ?)', (userid,username,))
        await tc.execute('INSERT OR IGNORE INTO rat(user_id) VALUES(?)', (userid,))
        await tc.execute('INSERT OR IGNORE INTO iff(user_id) VALUES(?)', (userid,))
        await tc.execute('INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)', (userid,username,first_name,))
        await tc.commit()
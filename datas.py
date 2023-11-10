import aiosqlite



async def state_tttttt():
    async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS rat(user_id PRIMARY KEY, username, username_admin, time_now, time_delete)')
        await tc.execute('CREATE TABLE IF NOT EXISTS iff(user_id PRIMARY KEY, sends, sends_)')
        await tc.execute('CREATE TABLE IF NOT EXISTS users(user_id PRIMARY KEY, cases_, price, zametka, usersc, username, war DEfAULT 0, time_now, time_delete, first_name)')
        await tc.commit()















async def state_5(userid,username,first_name):
    async with aiosqlite.connect('teg.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO rat(user_id) VALUES(?)', (userid,))
        await tc.execute('INSERT OR IGNORE INTO iff(user_id) VALUES(?)', (userid,))
        await tc.execute('INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)', (userid,username,first_name,))
        await tc.commit()
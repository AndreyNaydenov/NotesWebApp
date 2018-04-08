import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()

    c.execute('create table users(id integer primary key autoincrement, login text unique, password text);')
    c.execute('create table notes(id integer primary key autoincrement, title text, user_id integer)')

    conn.commit()
    conn.close()
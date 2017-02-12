import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

def setup():

	c.execute('''
		create table classes(
		id integer primary key autoincrement,
		name text,
		code text
		);
		''')

	c.execute('''
		create table users(
		id integer primary key autoincrement,
		name text,
		cup boolean,
		problem text,
		class_id integer
		);
		''')

class Student:

	def __init__(self, name, classcode):

		c.execute('select * from classes where code=?', (classcode,))
		class_id = c.fetchone()[0]

		c.execute('''
			insert into users(name, cup, class_id)
			values(?, ?, ?);
			''',(name,False, class_id))





class Classroom:

	def __init__(self, name, code):
		c.execute('''
			insert into classes(name, code)
			values(?, ?);
			''',(name, code))

#!/usr/bin/python3
# -*- coding: utf-8 -*-

def create():
	import sqlite3
	conn = sqlite3.connect('test.db')

	c = conn.cursor()

	c.execute("CREATE TABLE resa (id INTEGER PRIMARY KEY AUTOINCREMENT, date_a text, date_s text)")
	c.execute("CREATE TABLE chambre (num INTEGER)")
	resa_test =[('2014-06-01','2014-06-07'), ('2014-06-01', '2014-06-05'),
            ('2014-06-03','2014-06-09') ]
	c.executemany("INSERT INTO resa (date_a, date_s) VALUES (?,?)", resa_test)
 
	conn.commit()

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QDesktopWidget, QMessageBox

import mysql.connector
import sqlite3
from app import *


class Connect(QDialog):
	"""docstring for Connect"""
	def __init__(self):
		super(Connect, self).__init__()
		loadUi("District.ui",self)
		self.show()

		conn = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "1234",
			database = "councils"
			)
		c = conn.cursor()

		query = "SELECT Council FROM connectdb"
		c.execute(query)
		i=0
		for row in c.fetchall():
			self.cmbCouncil.addItem(str(row[0]))

		self.btnSubmit.clicked.connect(self.Proceed)

	def Proceed(self):
		district = self.setSchema()
		search = Login()
		widgets.addWidget(search)
		widgets.setCurrentIndex(widgets.currentIndex()+1)
		widgets.setWindowTitle(district + " | Login")
		search.DialogTitle.setText(district + " \nResidential Management System")
		widgets.show()
		self.close()

	def setSchema(self):
		Schema = self.cmbCouncil.currentText()
		conn = sqlite3.connect("connect.db")
		c = conn.cursor()
		query = """CREATE TABLE IF NOT EXISTS connected (
						idnum text PRIMARY KEY,
						name text NOT NULL );"""
		c.execute(query)
		conn.commit()
		conn.close()


		conn = sqlite3.connect("connect.db")
		c = conn.cursor()
		idnum="1"
		try:
			insert = 'INSERT INTO  connected (name,idnum) VALUES (?,?)'
			value = (Schema, idnum)		
			c.execute(insert,value)
			conn.commit()
		except Exception as e:
			raise e

		
		Schema = Schema.capitalize()
		return Schema

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Connect()
	widgets = QStackedWidget()
	
	conn = sqlite3.connect("connect.db")
	c = conn.cursor()
	try:
		drop = 'DROP TABLE connected'
		c.execute(drop)
		conn.commit()
	except Exception as e:
		raise e
	
	try:
		sys.exit(app.exec())
		
	except Exception as e:
		raise e
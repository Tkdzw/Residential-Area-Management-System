import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QStackedWidget
#, QApplication, QWidget, QMainWindow, QDesktopWidget, QMessageBox

import mysql.connector

from menu import *

class Login(QDialog):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		loadUi("Login.ui",self)
		self.setWindowTitle("Municipal Sys | Login")
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		#self.show()
		self.widgets = QStackedWidget()
		self.btnLogin.clicked.connect(self.loginauth)
		self.btnExit.clicked.connect(self.Exit)

	def loginauth(self):
		user = self.txtUsername.text()
		password =self.txtPassword.text() 

		if len(user)==0 or len(password)==0 :
			self.lblError.setText("Input All Fields Data")
		else:
			
			conn = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "1234",
				database = "shurugwi"
				)
			c = conn.cursor()
			query = "SELECT Password FROM auth WHERE Username = '%s' " % (user)
			c.execute(query)
			
			result_pass = c.fetchone()
			
			if c.rowcount == 0:
				self.lblError.setText("Invalid Authentication")
			elif c.rowcount == 1:
				c.execute(query)
				result_pass = c.fetchone()[0]
				if result_pass == password :
					self.lblError.setText("Access Granted")
					search = Main()
					self.widgets.addWidget(search)
					self.widgets.setCurrentIndex(self.widgets.currentIndex()+1)
					self.widgets.setWindowTitle("Municipal Sys")
					search.txtwelcome.setText("Welcome: " + user)
					self.widgets.showMaximized()
					self.close()
				else:
					self.lblError.setText("Invalid Authentication")
			
	def Exit(self):
		sys.exit()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Login()
	widgets = QStackedWidget()
	#widgets.setWindowFlag(QtCore.Qt.FramelessWindowHint)


	try:
		sys.exit(app.exec())
	except Exception as e:
		raise e
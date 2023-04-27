import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QDesktopWidget, QMessageBox

import mysql.connector
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
		Schema = self.cmbCouncil.currentText()
		search = Login()
		widgets.addWidget(search)
		widgets.setCurrentIndex(widgets.currentIndex()+1)
		widgets.setWindowTitle(Schema + " | Login")
		search.DialogTitle.setText(Schema + " \nResidential Management System")
		widgets.show()
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Connect()
	widgets = QStackedWidget()

	try:
		sys.exit(app.exec())
	except Exception as e:
		raise e
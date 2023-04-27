from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets,QtCore
import mysql.connector
 
from globals_def import *

def SavePayments(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()

	Acc = ui.txtAcc.text()
	Meter = ui.txtMeterNum.text()
	Method = ui.txtMethod.currentText()
	PDate = ui.txtdateEdit.text()
	Paid = ui.txtPaid.text()

	query = "INSERT INTO payments ( AccountNumber, MeterNumber, PaymentMethod, PaymentDate, Amount) VALUES ('%s', '%s', '%s', '%s', '%s')" % (Acc ,Meter ,Method ,PDate ,Paid )

	try:
		c.execute(query)
		conn.commit()
		saved_Success()
		ui.txtAcc.clear()
		ui.txtMeter.clear()
		ui.txtMeterNum.clear()
		ui.txtdateEdit.clear()
		ui.txtPaid.clear()
	except Exception as e:
		Error_Message(e)


def PaysView(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()

	user=""
	query = "SELECT * FROM pays"
	result = c.execute(query)

	count = paysdatabase_count(query)
	
	ui.pays_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(8):
			ui.pays_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1

def PaySearch(ui):
	search = ui.txtPaySearch.text()
	
	ui.pays_table.setRowCount(0)
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()
	query = "SELECT * FROM pays WHERE AccountNumber = '%s'" % (search)
	c.execute(query)
	
	count = paysdatabase_count(query)

	ui.pays_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(8):
			ui.pays_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1

def Error_Message(e):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Warning)
	msg.setText('Error: "{}"'.format(e))
	retval = msg.exec_()

def saved_Success():
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Information)
	msg.setText("Data Successfuly saved")
	retval = msg.exec_()


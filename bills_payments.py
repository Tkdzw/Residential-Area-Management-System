from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets,QtCore
import mysql.connector
 
from globals_def import *
def SaveBill(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()

	Meter = ui.txtMeter.text()
	Reading = ui.txtReading.text()
	BillAmnt = ui.txtBillAmnt.text()
	Date = ui.txtDate.text()

	query = "INSERT INTO billings ( MeterNumber, MeterReadings, AmountDue, BillDate) VALUES ('%s', '%s', '%s', '%s')" % (Meter ,Reading ,BillAmnt ,Date)

	try:
		c.execute(query)
		conn.commit()
		saved_Success()
		ui.txtMeter.clear()
		ui.txtReading.clear()
		ui.txtBillAmnt.clear()
		ui.txtDate.clear()
	except Exception as e:
		Error_Message(e)


def BillsView(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()

	user=""
	query = "SELECT * FROM bills"
	result = c.execute(query)

	count = billsdatabase_count(query)
	
	ui.bills_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(9):
			ui.bills_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1


def AccBillSearch(ui):
	
	search = ui.txtBillSearch.text()
	name = "Munashe"
	ui.bills_table.setRowCount(0)
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()
	query = "SELECT * FROM bills WHERE AccountNumber = '%s'" % (search)
	c.execute(query)
	
	count = billsdatabase_count(query)
	ui.bills_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(9):
			ui.bills_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
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


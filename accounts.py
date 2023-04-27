import sys, os
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets,QtCore

import mysql.connector
from globals_def import *


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

def AccNav(ui):
	ui.accountstacked.setCurrentIndex(1)

def AddAcc(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()
	#AccNumber = 123332
	F_Name = ui.txtFirstname.text()
	S_Name = ui.txtSurname.text()
	ID = ui.txtID.text()
	DOB = ui.DOB.text()
	Occu = ui.txtOccu.text()
	RegDate = ui.txtReg.text()
	Phone = "+263"

	query = "INSERT INTO residents(FirstName, Surname, ID_Number, Date_OB, Address, RegistrationDate, Phone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (F_Name, S_Name, ID, DOB, Occu, RegDate, Phone )

	try:
		c.execute(query)
		conn.commit()
		saved_Success()
		F_Name = ui.txtFirstname.clear()
		S_Name = ui.txtSurname.clear()
		ID = ui.txtID.clear()
		DOB = ui.DOB.clear()
		Occu = ui.txtOccu.clear()
		RegDate = ui.txtReg.clear()
	except Exception as e:
		Error_Message(e)

def loadData(ui):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()

	user=""
	query = "SELECT * FROM residents"
	result = c.execute(query)

	count = accdatabase_count(query)
	
	ui.accounts_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(7):
			ui.accounts_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1


def AccSearch(ui):
	search = ui.txtSearch.text()
	
	ui.accounts_table.setRowCount(0)
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()
	query = "SELECT * FROM residents WHERE AccNumber = '%s'" % (search)
	c.execute(query)
	
	count = accdatabase_count(query)

	ui.accounts_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(7):
			ui.accounts_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1

def DetailsView(ui):
	search = ui.txtSearch.text()
	
	ui.accounts_table.setRowCount(0)
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	c = conn.cursor()
	query = "SELECT * FROM residents WHERE AccNumber = '%s'" % (search)
	c.execute(query)
	
	Firstname = c.fetchone()[1]
	ui.lblFirstname.setText(Firstname)
	
	c.execute(query)
	Surname = c.fetchone()[2]
	ui.lblSurname.setText(Surname)

	c.execute(query)
	ID = c.fetchone()[3]
	ui.lblID.setText(ID)

	c.execute(query)
	DateOB = str(c.fetchone()[4])
	ui.lblDate_OB.setText(DateOB)

	c.execute(query)
	Address = c.fetchone()[5]
	ui.lblAddress.setText(Address)

	c.execute(query)
	RegistrationDate = str(c.fetchone()[6])
	ui.lblRegistrationDate.setText(RegistrationDate)
	
	c.execute(query)
	Phone = c.fetchone()[7]
	ui.lblPhone.setText(Phone)

	
	ui.pays_table_2.setRowCount(0)
	
	c = conn.cursor()
	query = "SELECT * FROM pays WHERE AccountNumber = '%s'" % (search)
	c.execute(query)
	
	count = paysdatabase_count(query)

	ui.pays_table_2.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(8):
			ui.pays_table_2.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1

	query = "SELECT * FROM bills WHERE AccountNumber = '%s'" % (search)
	result = c.execute(query)

	count = billsdatabase_count(query)
	
	ui.bills_table_2.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(9):
			ui.bills_table_2.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		tableRow+=1


	c = conn.cursor()
	query = "SELECT balance FROM accountbalances WHERE AccountNumber = '%s'" % (search)
	c.execute(query)

	Balance = str(c.fetchone()[0])
	ui.lblAccBal.setText(Balance)
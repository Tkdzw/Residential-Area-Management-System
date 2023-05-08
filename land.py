import sys, os
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets,QtCore


from globals_def import*

def SaveNLand(ui):
	conn = databaseConnection()
	c = conn.cursor()

	S_Num = ui.txtSnum.text()
	Size  = ui.txtLSize.text()
	Location = ui.txtLocation.text()
	Amn = ui.txtAmn.text()
	Price = ui.txtPrice.text()


	try:
		query = "INSERT INTO land (StandNumber, LandSize, LandLocation, Status, Price) VALUES  ('%s', '%s', '%s', '%s', '%s')" %(S_Num ,Size ,Location ,Amn ,Price)
		c.execute(query)
		conn.commit()
		saved_Success()
		ui.txtSnum.clear()
		ui.txtLSize.clear()
		ui.txtLocation.clear()
		ui.txtAmn.clear()
		ui.txtPrice.clear()
	except Exception as e:
		Error_Message(e)

def loadland(ui):
	conn = databaseConnection()
	c = conn.cursor()
	user=""
	query = "SELECT * FROM land" 
	result = c.execute(query)
	
	count = landdatabase_count(query)

	ui.land_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(5):
			ui.land_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
		
		tableRow+=1

def LandSearch(ui):
	
	search = ui.txtLandSearch.text()

	ui.land_table.setRowCount(0)
	conn = databaseConnection()
	c = conn.cursor()
	query = "SELECT * FROM land WHERE StandNumber = '%s' OR LandLocation = '%s' "% (search,search)
	c.execute(query)
	
	count = landdatabase_count(query)

	ui.land_table.setRowCount(count)
	tableRow = 0
	for row in c.fetchall():
		for i in range(5):
			ui.land_table.setItem(tableRow, i, QtWidgets.QTableWidgetItem(str(row[i])))
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
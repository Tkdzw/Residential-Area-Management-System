import sys, os
import mysql.connector

def accdatabase_count(query):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	b = conn.cursor()

	b.execute(query)
	result = b.fetchall()

	count = b.rowcount

	return count

def landdatabase_count(query):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	b = conn.cursor()
	b.execute(query)
	result = b.fetchall()
	
	count = b.rowcount
	return count

def billsdatabase_count(query):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	b = conn.cursor()

	b.execute(query)
	result = b.fetchall()

	count = b.rowcount

	return count

def paysdatabase_count(query):
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "1234",
		database = "shurugwi"
		)
	b = conn.cursor()

	b.execute(query)
	result = b.fetchall()

	count = b.rowcount

	return count

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
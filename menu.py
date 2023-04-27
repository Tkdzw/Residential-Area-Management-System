import sys, os
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QMainWindow

from accounts import *
from land import *
from bills_payments import *
from payments import *

class Main(QMainWindow):
	"""docstring for Main"""
	def __init__(self):
		super(Main, self).__init__()
		loadUi("Main_UI.ui",self)
		self.txtwelcome.setText("Welcome: Asher")
		#self.show()

		self.stackedWidget.setCurrentIndex(0)

		self.btnHome.clicked.connect(self.OpenHome)
		self.btnResidential.clicked.connect(self.OpenRes)
		self.btnAcc.clicked.connect(self.OpenAccounts)
		self.btnBill.clicked.connect(self.OpenBill)
		self.btnConfig.clicked.connect(self.OpenSettings)
		self.btnHelp.clicked.connect(self.OpenHelp)
		self.btnLogOut.clicked.connect(self.LogOut)
		
		self.btnSave.clicked.connect(self.AddAccount)
		#self.btnRefresh.clicked.connect(self.LoadData)
		self.btnAddAcc.clicked.connect(self.AddAccTab)
		self.btnSearch.clicked.connect(self.AccSearch)
		self.btnBackH.clicked.connect(self.OpenHome)
		self.btnAccDetails.clicked.connect(self.AccDetails)
		self.btnAccSearch.clicked.connect(self.Acc_Search)

		self.btnAddLand.clicked.connect(self.AddLand)
		self.btnSaveLand.clicked.connect(self.SaveLand)
		self.btnLandView.clicked.connect(self.DataLand)
		self.btnLandSearch.clicked.connect(self.Land_Search)

		self.btnBills.clicked.connect(self.OpenBills)
		self.btnAddBill.clicked.connect(self.AddBill)
		self.btnBillView.clicked.connect(self.ViewBills)
		self.btnBillSearch.clicked.connect(self.SearchBills)
		self.btnBillSave.clicked.connect(self.BillSave)
		self.btnBill_Search.clicked.connect(self.Bill_Search)

		self.btnPayments.clicked.connect(self.OpenPayments)
		self.btnPSave.clicked.connect(self.PaymentSave)
		self.btnAddPay.clicked.connect(self.AddPay)
		self.btnPayView.clicked.connect(self.ViewPays)
		self.btnPay_Search.clicked.connect(self.Pay_Search)
		self.btnPayRefresh.clicked.connect(self.ViewPays)




		self.btnAccEnq.clicked.connect(self.OpenEnquiry)

#Main Navigation Functions
	def OpenHome(self):
		self.stackedWidget.setCurrentIndex(0)

	def OpenRes(self):
		self.stackedWidget.setCurrentIndex(1)
		self.landstacked.setCurrentIndex(0)
		loadland(self)

	def OpenAccounts(self):
		self.stackedWidget.setCurrentIndex(2)
		self.accountstacked.setCurrentIndex(0)
		self.LoadData()

	def OpenBill(self):
		self.stackedWidget.setCurrentIndex(3)

	def OpenSettings(self):
		self.stackedWidget.setCurrentIndex(4)

	def OpenHelp(self):
		self.stackedWidget.setCurrentIndex(5)


	def LogOut(self):
		sys.exit()


#Accounts Functions
	def AddAccount(self):
		AddAcc(self)

	def LoadData(self):
		loadData(self)

	def AddAccTab(self):
		self.stackedWidget.setCurrentIndex(2)
		self.accountstacked.setCurrentIndex(2)

	def AccSearch(self):
		self.stackedWidget.setCurrentIndex(2)
		self.accountstacked.setCurrentIndex(1)
		loadData(self)

	def AccDetails(self):
		
		if self.txtSearch.text()=="":
			self.stackedWidget.setCurrentIndex(2)
			self.accountstacked.setCurrentIndex(1)
			self.lblsearch.setText("Search is Blank")
		else:
			self.accountstacked.setCurrentIndex(3)
			self.lblsearch.setText("")
			DetailsView(self)

	def Acc_Search(self):
		AccSearch(self)
		
#Land Management Functions
	def AddLand(self):
		self.landstacked.setCurrentIndex(1)
		self.stackedWidget.setCurrentIndex(1)

	def SaveLand(self):
		SaveNLand(self)

	def DataLand(self):
		self.landstacked.setCurrentIndex(0)
		self.stackedWidget.setCurrentIndex(1)
		loadland(self)

	def Land_Search(self):
		LandSearch(self)



#####Bill & Payments Functions#####
	
#Bill Functions

	def OpenBills(self):
		self.billpaymentstacked.setCurrentIndex(0)
		self.billstacked.setCurrentIndex(0)
		self.stackedWidget.setCurrentIndex(3)

	def ViewBills(self):
		self.billstacked.setCurrentIndex(1)
		self.stackedWidget.setCurrentIndex(3)
		BillsView(self)

	def AddBill(self):
		self.billstacked.setCurrentIndex(2)
		self.stackedWidget.setCurrentIndex(3)

	def SearchBills(self):
		self.billstacked.setCurrentIndex(3)
		self.stackedWidget.setCurrentIndex(3)

	def BillSave(self):
		SaveBill(self)

	def Bill_Search(self):
		AccBillSearch(self)

	
#Payments Functions

	def OpenPayments(self):
		self.billpaymentstacked.setCurrentIndex(1)
		self.paymentstacked.setCurrentIndex(0)
		self.stackedWidget.setCurrentIndex(3)


	def AddPay(self):
		self.paymentstacked.setCurrentIndex(2)

	def ViewPays(self):
		self.paymentstacked.setCurrentIndex(1)
		PaysView(self)

	def Pay_Search(self):
		PaySearch(self)


	def PaymentSave(self):
		SavePayments(self)


#Debts Functions

	def OpenEnquiry(self):
		self.billpaymentstacked.setCurrentIndex(2)
		self.stackedWidget.setCurrentIndex(3)
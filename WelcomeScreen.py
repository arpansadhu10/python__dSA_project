
# importing libraries
from PyQt5.QtWidgets import QDialog,QApplication, QInputDialog, QStackedWidget, QTableWidgetItem,QWidget,QPushButton,QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
# from PyQt5.QtCore import * 
import sys
from test_database import db

# from testarray import *

array_test=[1,2,3]
count=0

class WelcomeScreen(QDialog):
  
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("WelcomeScreen.ui",self)
        self.StartButton.clicked.connect(self.online_offline_function)
    

    def online_offline_function(self):
        # print("clicked")
        array_test.append(200)
        online_offline_pagechanger = online_offline_class()
        widget.addWidget(online_offline_pagechanger)
        widget.setCurrentIndex(widget.currentIndex()+1)



class online_offline_class(QDialog):
    def __init__(self):
        super(online_offline_class, self).__init__()
        loadUi("online_offline.ui",self)
        array_test.append(100)
        self.homepage.clicked.connect(self.homepage_function)
        self.offline.clicked.connect(self.dataDisplay_function)
    
    def dataDisplay_function(self):
        # print("clicked")
        dataDisplay_page = dataDisplay_class()
        widget.addWidget(dataDisplay_page)
        widget.setCurrentIndex(widget.currentIndex()+1)




    def homepage_function(self):
        # print("homepage")
        homepage = WelcomeScreen()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()-1)


class dataDisplay_class(QDialog):
    def __init__(self):
        super(dataDisplay_class, self).__init__()
        loadUi("Datadisplay.ui",self)
        self.loaddata()
        self.createData.clicked.connect(self.createData_function)
        self.loaddata()
        self.deleteData.clicked.connect(self.deleteData_function)

        # self.homepage.clicked.connect(self.exit_func)

    def deleteData_function(self):
        print("deleteclicked")
        id_to_delete,ok=QInputDialog.getText(self,"input dialogue","Enter id which is to be deleted:")
        # print(id_to_delete)
        # print()
        print(type(id_to_delete),"this is received")
        
        index=-1
        for i in range(len(db)):
            # print(type(db[i]['id']))
            print(i,"wanted")
            if db[i]["id"] == int(id_to_delete):
                del db[i]
                index=i
         #!have to change ids after that    
        self.loaddata()   
        print(db)
            
    # def exit_func(self):
    #     print("exiting")
    #     sys.exit(app.exec())


    def createData_function(self):
        print("createddata")
        name,ok=QInputDialog.getText(self,"input dialogue","Enter Name:")
        phone,ok=QInputDialog.getText(self,"input dialogue","Enter phone Number:")
        email,ok=QInputDialog.getText(self,"input dialogue","Enter Email id:")
        db.append({
            "id":len(db)+1,
            "name":name,
            "email":email,
            "phone":phone

        })
        print(db)
        
        # count=count+1
        self.loaddata()
        # print(name)
        # print(ok)
        



    
    def loaddata(self):
        # db2=[{"name":"arpan","email":"abc@abc.com","phone":"123456"},
        #     {"name":"arpanAgain","email":"abcd@abcd.com","phone":"1234566666"}]
        row=0
        # print("here")
        self.tableWidget.setRowCount(len(db))

        for person in db:
            # print(person["name"])

            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(person["phone"])))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(person["email"]))
            row=row+1




        


#main
app=QApplication(sys.argv)
welcome=WelcomeScreen()

widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()


try:
    sys.exit(app.exec())
except:
    print("exiting")
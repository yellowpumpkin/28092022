import string

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

import resizeWood
import inputWood
import withdrawWood
import heatWood
import saleWood
import main

from mySQL import database

db = database()


class UI_Cutwood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cutting")
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.display()
        self.displayTable1()
        self.displayTable2()
        self.layouts()
        self.funcFetchData()

    # Tool Bar
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        # self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.addResize.triggered.connect(self.funcResize)
        self.tb.addSeparator()
        # Heat
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.addHeat.triggered.connect(self.funcHeat)
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()
        # Sale
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()

    # Display
    def display(self):
        self.wg = QWidget()
        self.setCentralWidget((self.wg))
        self.cuttingText = QLabel("GUI CUTTING")
        self.select = QPushButton()
        self.select.clicked.connect(self.checkdata)


    # Table
    def displayTable1(self):
        self.cuttingTable1 = QTableWidget()
        self.cuttingTable1.setColumnCount(9)
        self.item = QtWidgets.QTableWidgetItem()
        header = ['โค้ดไม้','หนา','กว้าง','ยาว','จำนวน','ปริมาตร','ประเภท','สถานะ','เลือก']
        self.cuttingTable1.setHorizontalHeaderLabels(header)
        self.cuttingTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def displayTable2(self):
        self.cuttingTable2 = QTableWidget()
        self.cuttingTable2.setColumnCount(8)
        header = ['โค้ดไม้','หนา','กว้าง','ยาว','จำนวน','ปริมาตร','ประเภท','สถานะ','เลือก']
        self.cuttingTable2.setHorizontalHeaderLabels(header)
        self.cuttingTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTable1Layout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.middleTopLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()
        self.sizeGropBox = QGroupBox("")

        # Left Top
        self.leftTopLayout.addWidget(self.select)
        self.sizeGropBox.setLayout(self.leftTopLayout)
        self.mainRightLayout.addWidget(self.sizeGropBox)

        # Table
        self.mainTable1Layout.addWidget(self.cuttingTable1)
        self.mainTable2Layout.addWidget(self.cuttingTable2)

        # All Layout
        self.mainLayout.addLayout(self.mainTable1Layout)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainTable2Layout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    # FetchData
    def funcFetchData(self):
        query = db.fetchdataCut()
        for row_data in query:
            row_number = self.cuttingTable1.rowCount()
            self.cuttingTable1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.cuttingTable1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.cuttingTable1.setItem(row_number, 8, chkBoxItem)
            # self.qch_select = QCheckBox('SELECT')
            # self.qch_select.toggled.connect(self.funchandleButtonClicked)
        self.cuttingTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def checkdata(self):
        msg = QMessageBox()
        msg.setWindowTitle("แก้ไขข้อมูล")
        msg.setText("กรุณาตรวจสอบความถูกต้อง")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.funchandleButtonClicked)

        x = msg.exec_()

    def funchandleButtonClicked(self,i):
        if (i.text() != 'Cancel'):
            for row in range(self.cuttingTable1.rowCount()):
                if self.cuttingTable1.item(row,8).checkState() == Qt.CheckState.Checked:
                    listInput = [self.cuttingTable1.item(row,col).text() for col in range(self.cuttingTable1.columnCount())]
                    self.funcshowData(listInput)
                else:
                    self.cuttingTable2.removeRow(row)

    def funcshowData(self, input1):
        row_number = self.cuttingTable2.rowCount()
        if input1 != []:
            self.cuttingTable2.insertRow(row_number)
            for column_number, data in enumerate(input1):
                self.cuttingTable2.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    # Function Home
    def funcHome(self):
        self.newHome = main.Ui_MainWindow()
        self.close()

    # Function Input
    def funcInput(self):
        self.newInput = inputWood.UI_Inputwood()
        self.close()

    # Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.close()

    # Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.close()

    # Function Resize
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.close()

    # Function  Sale
    def funcSale(self):
        self.newSale = saleWood.UI_Salewood()
        self.close()


import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Cutwood()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
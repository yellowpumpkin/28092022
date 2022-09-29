from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import main
import resizeWood
import saleWood
import withdrawWood
import cuttingWood
import editsInputwood
# import pandas as pd

from mySQL import database
db = database()

class UI_Inputwood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.setWindowTitle("ข้อมูลรับไม้เข้า")
        self.setWindowIcon(QIcon('icons/wood01.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.displayTable()
        self.display()
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
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
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
        # Sale
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()

        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()

# Widget
    def display(self):
        self.wg = QWidget()
        self.setCentralWidget((self.wg))

        # self.allwood=QRadioButton("AllWood")
        # self.avaiableWood=QRadioButton("Avaiable")
        # self.unavaiableWood=QRadioButton("Unavaiable")
        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        # combobox
        self.sizeText = QLabel(self)
        self.sizeText.setText("size")
        self.thickText = QLabel("thick")
        self.wideText = QLabel("x wide")
        self.longText = QLabel("x long")

        # combobox thick
        self.combboxThick = QComboBox()
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.combboxThick.addItems([str(data_thick)])

        # combobox wide
        self.comboboxWide = QComboBox()
        Wide = db.sqlWide()
        for data_wide in Wide:
            self.comboboxWide.addItems([str(data_wide)])

        # combobox long
        self.comboboxLong = QComboBox()
        Long = db.sqlLong()
        for data_long in Long:
            self.comboboxLong.addItems([str(data_long)])

        # combobox type
        self.typeText = QLabel("Type : ")
        self.comboboxType = QComboBox()
        Type = db.sqlType()
        for data_type in Type:
            self.comboboxType.addItems([str(data_type)])

        # calender
        self.dateText = QLabel("วันที่รับไม้เข้า : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate()))
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        # btn
        self.btn_insert_input = QPushButton("insert")
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')

        self.btn_excel = QPushButton(self)
        self.btn_excel.setIcon(QIcon('icons/excel (2).png'))
        self.btn_excel.clicked.connect(self.exportExcel)

# Table
    def displayTable(self):
        self.inputTable = QTableWidget()
        self.inputTable.setColumnCount(10)
        header = ['วันที่รับไม้เข้า', 'โค้ดไม้', 'ประเภท', 'หนา' ,'กว้าง', 'ยาว', 'จำนวน', 'ปริมาตร (m^3)', 'ลูกค้า', 'Manage']
        self.inputTable.setHorizontalHeaderLabels(header)
        self.inputTable.doubleClicked.connect(self.func_handleButtonClicked)
        column_size = self.inputTable.horizontalHeader()
        for i in range(0, 10):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        # header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

# Layouts
    def layouts(self):
        # QV & QH
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()

        self.searchLayout = QHBoxLayout()
        self.comboboxLayout = QHBoxLayout()
        self.rightTopLayout = QHBoxLayout()

        self.searchGroupBox = QGroupBox()
        self.comboboxGroup = QGroupBox()
        self.btnGrop = QWidget()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.dateText)
        self.searchLayout.addWidget(self.date)
        self.searchGroupBox.setLayout(self.searchLayout)

        # Combobox
        self.comboboxLayout.addWidget(self.sizeText)
        self.comboboxLayout.addWidget(self.thickText)
        self.comboboxLayout.addWidget(self.combboxThick)
        self.comboboxLayout.addWidget(self.wideText)
        self.comboboxLayout.addWidget(self.comboboxWide)
        self.comboboxLayout.addWidget(self.longText)
        self.comboboxLayout.addWidget(self.comboboxLong)
        self.comboboxLayout.addWidget(self.typeText)
        self.comboboxLayout.addWidget(self.comboboxType)
        self.comboboxGroup.setLayout(self.comboboxLayout)

        # Right Top aka Btn
        self.rightTopLayout.addWidget(self.btn_insert_input)
        self.rightTopLayout.addWidget(self.btn_refresh)
        self.rightTopLayout.addWidget(self.btn_excel)
        self.btnGrop.setLayout(self.rightTopLayout)

        # Layout Table
        self.mainTableLayout.addWidget(self.inputTable)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGroupBox)
        self.mainTopLayout.addWidget(self.comboboxGroup)
        self.mainTopLayout.addWidget(self.btnGrop)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

# Function Home
    def funcHome(self):
        self.newHome = main.Ui_MainWindow()
        self.hide()

# Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.hide()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.hide()

# Function Resize
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.hide()

# Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.hide()

# Function Sale
    def funcSale(self):
        self.newHeat = saleWood.UI_Salewood()
        self.hide()

# FetchData
    def funcFetchData(self):
        for i in reversed(range(self.inputTable.rowCount())):
            self.inputTable.removeRow(i)
        query = db.fetch_dataInput()
        for row_data in query:
            row_number = self.inputTable.rowCount()
            self.inputTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.inputTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.btn_edit = QPushButton('Edit')
            self.btn_edit.setStyleSheet("""
                        QPushButton {
                            color:  black;
                            border-style: solid;
                            border-width: 3px;
                            border-color:  #008CBA;
                            border-radius: 12px
                        }
                        QPushButton:hover{
                            background-color: #008CBA;
                            color: white;
                        }
                    """)
            self.btn_edit.clicked.connect(self.func_handleButtonClicked)
            self.inputTable.setCellWidget(row_number, 9, self.btn_edit)
        self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

# Button Clicked
    def func_handleButtonClicked(self):
        global Input_id
        listInput = []
        for i in range(0, 9):
            listInput.append(self.inputTable.item(self.inputTable.currentRow(), i).text())
        Input_id = listInput[1]
        self.neweditInput = editsInputwood.UI_editsInputwood(listInput,Input_id)

    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.information(self, "Siam Kyohwa", "Search cant be empty!")
        else:
            self.searchEntry.text()
            results = db.searchInput(value)
            if results == []:
                QMessageBox.information(self, "Siam Kyohwa", "wood id information not found!")
            else:
                for i in reversed(range(self.inputTable.rowCount())):
                    self.inputTable.removeRow(i)
                for row_data in results:
                    row_number = self.inputTable.rowCount()
                    self.inputTable.insertRow(row_number)
                    for column_number , data in enumerate(row_data):
                        self.inputTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                    self.btn_edit = QPushButton('Edit')
                    self.btn_edit.setStyleSheet("""
                                QPushButton {
                                    color:  black;
                                    border-style: solid;
                                    border-width: 3px;
                                    border-color:  #008CBA;
                                    border-radius: 12px
                                }
                                QPushButton:hover{
                                    background-color: #008CBA;
                                    color: white;
                                }
                            """)
                    self.btn_edit.clicked.connect(self.func_handleButtonClicked)
                    self.inputTable.setCellWidget(row_number, 9, self.btn_edit)
                self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def funcRefresh(self):
       self.funcFetchData()

    def exportExcel(self):
        pass


def input():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Inputwood()
    sys.exit(app.exec_())
if __name__ == "__main__":
    input()
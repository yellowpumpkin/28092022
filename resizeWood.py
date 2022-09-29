from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import inputWood
import withdrawWood
import saleWood
import cuttingWood
import main

from mySQL import database

db = database()

class  UI_Resizewood (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resize")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450, 50,1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.display()
        self.displayTable1()
        self.displayTable2()
        self.funcFetchData()
        self.layouts()

#Tool Bar
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
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
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


    # display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. 6328218")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        self.btn_withdraw = QPushButton("เบิกไม้ประจำวัน")
        self.btn_withdraw.setShortcut('Return')
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.setShortcut('F5')

        withdraw_type = db.sqlWithdrawType()
        self.type_cut = withdraw_type[3]
        self.text_type_withdraw = QLabel("ประเภทการเบิก : " + str(self.type_cut))

        date = QDateTime.currentDateTime()
        self.dateDisplay = date.toString('yyyy-MM-dd')
        self.dateText = QLabel("วันทีเบิกไม้ : "+self.dateDisplay)

    # table
    def displayTable1(self):
        self.resizeTable1 = QTableWidget()
        self.resizeTable1.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'manage']
        self.resizeTable1.setHorizontalHeaderLabels(header)
        column_size = self.resizeTable1.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def displayTable2(self):
        self.resizeTable2 = QTableWidget()
        self.resizeTable2.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'Delete']
        self.resizeTable2.setHorizontalHeaderLabels(header)
        column_size = self.resizeTable2.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.resizeTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTable1Layout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()
        self.middleTopLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.btnGropBox = QGroupBox("")
        self.btnGropBox2 = QGroupBox("")
        self.textGropBox = QGroupBox("")
        self.searchGropBox = QGroupBox()

        # Btn GroupBox
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.searchLayout)

        # Btn
        self.rightTopLayout.addWidget(self.btn_withdraw)
        self.btnGropBox.setLayout(self.rightTopLayout)
        self.middleTopLayout.addWidget(self.btn_refresh)
        self.btnGropBox2.setLayout(self.middleTopLayout)

        # Left Top
        self.leftTopLayout.addStretch()
        self.leftTopLayout.addWidget(self.text_type_withdraw)
        self.leftTopLayout.addWidget(self.dateText)
        # self.leftTopLayout.addWidget(self.dateDisplay)
        self.leftTopLayout.addStretch()
        self.textGropBox.setLayout(self.leftTopLayout)

        # Table
        self.mainTable1Layout.addWidget(self.resizeTable1)
        self.mainTable2Layout.addWidget(self.resizeTable2)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGropBox)
        self.mainTopLayout.addWidget(self.textGropBox)
        self.mainTopLayout.addWidget(self.btnGropBox2)
        self.mainTopLayout.addWidget(self.btnGropBox)

        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTable1Layout)
        self.mainLayout.addLayout(self.mainTable2Layout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    def funcFetchData(self):
        for i in reversed(range(self.resizeTable1.rowCount())):
            self.resizeTable1.removeRow(i)
        query = db.fetch_dataResize()
        for row_data in query:
            row_number = self.resizeTable1.rowCount()
            self.resizeTable1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, data)
                self.resizeTable1.setItem(row_number, column_number, item)
            btn_select = QPushButton('เลือก')
            btn_select.setStyleSheet("""
                                    QPushButton {
                                        color:  black;
                                        border-style: solid;
                                        border-width: 3px;
                                        border-color:  #4CAF50;
                                        border-radius: 12px }
                                    QPushButton:hover{
                                        background-color: #4CAF50;
                                        color: white; }
                                    """)
            # btn_select.clicked.connect(self.func_handleButtonClicked)
            self.resizeTable1.setCellWidget(row_number, 7, btn_select)
        self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.warning(self, " ", "search cant be empty!")
        else:
            self.searchEntry.text()
            results = db.searchCutting(value)
            if results == []:
                QMessageBox.warning(self, " ", "wood id information not found!")
            else:
                for i in reversed(range(self.resizeTable1.rowCount())):
                    self.resizeTable1.removeRow(i)
                for row_data in results:
                    row_number = self.resizeTable1.rowCount()
                    self.resizeTable1.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.EditRole, data)
                        self.resizeTable1.setItem(row_number, column_number, item)

                self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

# Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

# Function AddProduct
    def funcInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

# Function Cut
    def funcCut (self):
        self.newCut=cuttingWood.UI_Cutwood()
        self.close()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

# Function Heat
    def funcHeat(self):
        self.newHeat=heatWood.UI_Heatwood()
        self.close()

# Function Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()

# Main
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Resizewood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()

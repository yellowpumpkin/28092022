from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QPushButton

import resizeWood
import inputWood
import withdrawWood
import heatWood
import saleWood
import main
import  withdrawCrad

from mySQL import database
db = database()

class UI_Cutwood(QMainWindow):
    btn_withdraw: QPushButton

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cutting")
        self.setWindowIcon(QIcon('icons/cutting.png'))
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


    # Display
    def display(self):
        self.wg = QWidget(self)
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        self.btn_withdraw = QPushButton("เบิกไม้ประจำวัน")
        self.btn_withdraw.clicked.connect(self.func_Withdraw_Wood)
        self.btn_withdraw.setShortcut('Return')

        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')

        self.btn_excel = QPushButton(self)
        self.btn_excel.setIcon(QIcon('icons/excel (2).png'))

        withdraw_type = db.sqlWithdrawType()
        self.type_cut = withdraw_type[1]
        self.text_type_withdraw = QLabel("ประเภทการเบิก : " + str(self.type_cut))

        date = QDateTime.currentDateTime()
        self.dateDisplay = date.toString('yyyy-MM-dd')
        self.dateText = QLabel("วันทีเบิกไม้ : "+self.dateDisplay)

    # Table
    def displayTable1(self):
        self.cuttingTable1 = QTableWidget()
        self.cuttingTable1.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน' , 'manage']
        self.cuttingTable1.setHorizontalHeaderLabels(header)

        column_size = self.cuttingTable1.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.cuttingTable1.setEditTriggers(QAbstractItemView.DoubleClicked)

    def displayTable2(self):
        self.cuttingTable2 = QTableWidget()
        self.cuttingTable2.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'delete']
        self.cuttingTable2.setHorizontalHeaderLabels(header)
        self.cuttingTable2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        column_size = self.cuttingTable2.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        # self.cuttingTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTable1Layout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()
        self.textLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.btn_withdraw_Layout = QHBoxLayout()
        self.btn_refresh_Layout = QHBoxLayout()

        self.btnGropBox = QWidget()
        self.btnGropBox2 = QWidget()
        self.textGropBox = QGroupBox()
        self.searchGropBox = QGroupBox()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.searchLayout)
        # Text Type Date
        self.textLayout.addStretch()
        self.textLayout.addWidget(self.text_type_withdraw)
        self.textLayout.addWidget(self.dateText)
        self.textLayout.addStretch()
        self.textGropBox.setLayout(self.textLayout)
        # Btn GroupBox
        self.btn_withdraw_Layout.addWidget(self.btn_withdraw)
        self.btn_withdraw_Layout.addWidget(self.btn_excel)
        self.btnGropBox.setLayout(self.btn_withdraw_Layout)
        self.btn_refresh_Layout.addWidget(self.btn_refresh)
        self.btnGropBox2.setLayout(self.btn_refresh_Layout)
        # Table
        self.mainTable1Layout.addWidget(self.cuttingTable1)
        self.mainTable2Layout.addWidget(self.cuttingTable2)
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

    # FetchData
    def funcFetchData(self):
        for i in reversed(range(self.cuttingTable1.rowCount())):
            self.cuttingTable1.removeRow(i)
        query = db.fetch_dataCut()
        for row_data in query:
            row_number = self.cuttingTable1.rowCount()
            self.cuttingTable1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # item = QTableWidgetItem(data)
                #  item.setTextAlignment(Qt.AlignCenter);
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, data)
                # if(column_number != 6):
                    # item.setFlags(Qt.ItemIsEnabled)
                self.cuttingTable1.setItem(row_number, column_number,item)
            btn_select = QPushButton('เลือก')
            btn_select.setStyleSheet("""
                                    QPushButton {
                                        color:  black;
                                        border-style: solid;
                                        border-width: 3px;
                                        border-color:  #4CAF50;
                                        border-radius: 12px
                                    }
                                    QPushButton:hover{
                                        background-color: #4CAF50;
                                        color: white;
                                    }
                                """)
            btn_select.clicked.connect(self.func_handleButtonClicked)
            self.cuttingTable1.setCellWidget(row_number, 7, btn_select)
        self.cuttingTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def func_handleButtonClicked(self):
        global Input_id
        listInput = []
        for col in range(0, 7 ):
            listInput.append(self.cuttingTable1.item(self.cuttingTable1.currentRow(), col).text())
        self.func_showData(listInput)

    def func_showData(self, input1):
        query = input1
        row_number = self.cuttingTable2.rowCount()
        self.cuttingTable2.insertRow(row_number)
        for column_number, data in enumerate(query):
            item = QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, data)
            if(column_number != 6):
                item.setFlags(Qt.ItemIsEditable)
            self.cuttingTable2.setItem(row_number, column_number, item)
            self.cuttingTable2.setItem(row_number, 6, QTableWidgetItem(int(0)))
        btn_delete = QPushButton('ลบ')
        btn_delete.setStyleSheet("""
                                    QPushButton {
                                        color:  black;
                                        border-style: solid;
                                        border-width: 3px;
                                        border-color:  #f44336;
                                        border-radius: 12px
                                               }
                                    QPushButton:hover{
                                        background-color: #f44336;
                                        color: white;
                                               }
                                    """)
        btn_delete.clicked.connect(self.funcDeleteRow)
        self.cuttingTable2.setCellWidget(row_number, 7, btn_delete)

    def func_Withdraw_Wood(self):
        value = self.cuttingTable2.rowCount()
        totem = True
        if value == 0:
            QMessageBox.critical(self, "Siam Kyohwa", "ไม่พบข้อมูลในตาราง")
            totem = False
        list_withdraw_cut = []
        try:
            for row in range(self.cuttingTable2.rowCount()):
                list_table2 = []
                for col in range(0,7):
                    list_table2.append(self.cuttingTable2.item(row,col).text())
                if list_table2[6] == "":
                    QMessageBox.warning(self, "Siam Kyohwa", " กรุณากรอกข้อมูลให้ครบถ้วนค่ะ ")
                    totem = False
                    break
                list_withdraw_cut.append(tuple(list_table2))
                int(list_table2[6])
                totem = True
                if int(list_table2[6]) <= 0 :
                    QMessageBox.critical(self, "Siam Kyohwa", " จำนวนการเบิกไม้ไม่ถูกต้อง ")
                    totem = False

        except ValueError:
            QMessageBox.warning(self, "Siam Kyohwa", " กรอกข้อมูลเฉพาะตัวเลขเท่านั้น กรุณาตรวจสอบใหม่อีกครั้งค่ะ ")
            totem = False
        if totem == True:
         self.neweditInput = withdrawCrad.withdeawcrad(list_withdraw_cut, self.dateDisplay , self.type_cut)

    # Refresh
    def funcRefresh(self):
        for i in reversed(range(self.cuttingTable2.rowCount())):
            self.cuttingTable2.removeRow(i)

    def funcDeleteRow(self):
        self.cuttingTable2.removeRow(self.cuttingTable2.currentRow())

    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.warning(self, "Siam Kyohwa", "search cant be empty!")
        else:
            self.searchEntry.text()
            results = db.searchCutting(value)
            if results == []:
                QMessageBox.warning(self, "Siam Kyohwa", "wood id information not found!")
            else:
                for i in reversed(range(self.cuttingTable1.rowCount())):
                    self.cuttingTable1.removeRow(i)
                for row_data in results:
                    row_number = self.cuttingTable1.rowCount()
                    self.cuttingTable1.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.EditRole, data)
                        self.cuttingTable1.setItem(row_number, column_number, item)
                    btn_select = QPushButton('เลือก')
                    btn_select.setStyleSheet("""
                                            QPushButton {
                                                color:  black;
                                                border-style: solid;
                                                border-width: 3px;
                                                border-color:  #4CAF50;
                                                border-radius: 12px
                                            }
                                            QPushButton:hover{
                                                background-color: #4CAF50;
                                                color: white;
                                            }
                                        """)
                    btn_select.clicked.connect(self.func_handleButtonClicked)
                    self.cuttingTable1.setCellWidget(row_number, 7, btn_select)
                self.cuttingTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

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

# Main
import sys
def cut():
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Cutwood()
    sys.exit(app.exec_())


if __name__ == "__main__":
    cut()
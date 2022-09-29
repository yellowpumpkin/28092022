from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import inputWood
import resizeWood
import saleWood
import main
import cuttingWood
from mySQL import database
db = database()


class  UI_Withdraw (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("withdraw")
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.displayTable()
        self.display()
        self.layouts()

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
        self.addInput.triggered.connect(self.funcAddInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
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
        self.tb.addSeparator()

    # Display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget(self.wg)
        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        # calender
        self.dateText = QLabel("ดูรายการวันที่เบิก : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate()))
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        # combobox type
        self.withdrawtypeText = QLabel("ประเภทการเบิก : ")
        self.combobox_withdrawType = QComboBox()
        Type = db.sqlWithdrawType()
        for data_type in Type:
            self.combobox_withdrawType.addItems([str(data_type)])

        # Btn
        self.btn_refresh = QPushButton("Refresh")
        # self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')

    # Table
    def displayTable(self):
        self.withdrawTable = QTableWidget()
        self.withdrawTable.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน' , 'manage']
        self.withdrawTable.setHorizontalHeaderLabels(header)

        column_size = self.withdrawTable.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.withdrawTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

   # Layout
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()

        self.textLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.dateLayout = QHBoxLayout()
        self.btn_withdraw_Layout = QHBoxLayout()
        self.btn_refresh_Layout = QHBoxLayout()

        self.btnGropBox = QGroupBox()
        self.textGropBox = QGroupBox()
        self.searchGroupBox = QGroupBox()
        self.dateGroupBox=QGroupBox()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.withdrawtypeText)
        self.searchLayout.addWidget(self.combobox_withdrawType)
        self.searchLayout.addWidget(self.dateText)
        self.searchLayout.addWidget(self.date)
        self.searchGroupBox.setLayout(self.searchLayout)

        # Btn GroupBox
        self.btn_refresh_Layout.addWidget(self.btn_refresh)
        self.btnGropBox.setLayout(self.btn_refresh_Layout)

        # Table
        self.mainTableLayout.addWidget(self.withdrawTable)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGroupBox)
        self.mainTopLayout.addWidget( self.btnGropBox)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        #  Main Layout
        self.wg.setLayout(self.mainLayout)

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
                for i in reversed(range(self.withdrawTable.rowCount())):
                    self.withdrawTable.removeRow(i)
                for row_data in results:
                    row_number = self.withdrawTable.rowCount()
                    self.withdrawTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.EditRole, data)
                        self.withdrawTable.setItem(row_number, column_number, item)
                self.withdrawTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()
    # Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.close()

    # Function AddProduct
    def funcAddInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

    # Function Resize
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()

    # Function Heat
    def funcHeat(self):
        self.newHeat=heatWood.UI_Heatwood()
        self.close()


    # Function Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()

#Main
# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Withdraw()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()

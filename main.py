from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

import heatWood
import inputWood
import resizeWood
import saleWood
import withdrawWood
import cuttingWood


from mySQL import database
db = database()

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ระบบคลังไม้")
        self.setWindowIcon(QIcon('icons/wood.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.display()
        self.displayTable()
        self.layouts()
        self.funcFetchDataMain()

    # Tool Bar
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/sawmill.png'), "รายการแปลงไม้", self)
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
        self.wg = QWidget()
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood ID : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. 6328218")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        self.allwoodmh = QRadioButton("All")
        self.mainWood = QRadioButton("Main")
        self.headWood = QRadioButton("Head")

        self.allwood = QRadioButton("All Wood")
        self.avaiableWood = QRadioButton("Avaiable")
        self.unavaiableWood = QRadioButton("Unavaiable")
        self.listBtn = QPushButton("List")
        self.listBtn.clicked.connect(self.fucnList)

        # combobox
        self.sizeText = QLabel("| ขนาดไม้ : ")
        self.thickText = QLabel("หนา")
        self.wideText = QLabel("x กว้าง")
        self.longText = QLabel("x ยาว")

        # combobox thick
        self.comboboxThick = QComboBox()
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.comboboxThick.addItems([str(data_thick)])
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
        self.typeText = QLabel("| ประเภทไม้ : ")
        self.comboType = QComboBox()
        Type = db.sqlType()
        for data_type in Type:
            self.comboType.addItems([str(data_type)])


    # Display Table
    def displayTable(self):
        self.homeTable = QTableWidget()
        self.homeTable.setColumnCount(9)
        header = ['รหัสไม้', 'โค้ดไม้', 'ประเภท', 'หนา' ,'กว้าง', 'ยาว', 'จำนวน', 'ปริมาตร (m^3)', 'สถานะ']
        self.homeTable.setHorizontalHeaderLabels(header)
        self.homeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        columnsize = self.homeTable.horizontalHeader()
        for i in range(0, 9):
            columnsize.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    # Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()

        self.leftTopLayout = QHBoxLayout()
        self.middleTopLayout = QVBoxLayout()
        self.rightTopLayout = QVBoxLayout()

        self.centerMiddleLayout = QHBoxLayout()

        self.woodGroupBox = QGroupBox("Main/Head")
        self.middleGropBox = QGroupBox("Activity")
        self.searchGropBox = QGroupBox("Search")

        # Left Top or Search
        self.leftTopLayout.addWidget(self.thickText)
        self.leftTopLayout.addWidget(self.comboboxThick)
        self.leftTopLayout.addWidget(self.wideText)
        self.leftTopLayout.addWidget(self.comboboxWide)
        self.leftTopLayout.addWidget(self.longText)
        self.leftTopLayout.addWidget(self.comboboxLong)
        self.leftTopLayout.addWidget(self.typeText)
        self.leftTopLayout.addWidget(self.comboType)
        self.leftTopLayout.addWidget(self.searchText)
        self.leftTopLayout.addWidget(self.searchEntry)
        self.leftTopLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.leftTopLayout)

        # Middle Top
        self.middleTopLayout.addWidget(self.allwoodmh)
        self.middleTopLayout.addWidget(self.mainWood)
        self.middleTopLayout.addWidget(self.headWood)
        self.woodGroupBox.setLayout(self.middleTopLayout)

        # Right Top Layouts
        self.rightTopLayout.addWidget(self.allwood)
        self.rightTopLayout.addWidget(self.avaiableWood)
        self.rightTopLayout.addWidget(self.unavaiableWood)
        self.rightTopLayout .addWidget(self.listBtn)
        self.middleGropBox.setLayout(self.rightTopLayout)

        # Table
        self.mainTableLayout.addWidget(self.homeTable)

        # All Layout
        self.mainRightLayout.addWidget(self.searchGropBox)
        self.mainRightLayout.addWidget(self.woodGroupBox)
        self.mainRightLayout.addWidget(self.middleGropBox)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    # Display
    def funcFetchDataMain(self):
        for i in reversed(range(self.homeTable.rowCount())):
            self.homeTable.removeRow(i)
        query = db.fetch_dataHome()
        for row_data in query:
            row_number = self.homeTable.rowCount()
            self.homeTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.homeTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.information(self, " ", "Search cant be empty!!")
        else:
            self.searchEntry.text()
            results = db.searchHome(value)

            if results == []:
                QMessageBox.information(self, " ", "wood id information not found")
            else:
                for i in reversed(range(self.homeTable.rowCount())):
                    self.homeTable.removeRow(i)
                for row_data in results:
                    row_number = self.homeTable.rowCount()
                    self.homeTable.insertRow(row_number)
                    for column_number , data in enumerate(row_data):
                        self.homeTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    # List
    def fucnList(self):
        if self.allwood.isChecked() == True:
            self.funcFetchDataMain()
        elif self.avaiableWood.isChecked():
            query = db.funcListAvailable()
            for i in reversed(range(self.homeTable.rowCount())):
                self.homeTable.removeRow(i)
            for row_data in query:
                row_number = self.homeTable.rowCount()
                self.homeTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.homeTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.unavaiableWood.isChecked():
            query = db.funcListUnavailable()
            for i in reversed(range(self.homeTable.rowCount())):
                self.homeTable.removeRow(i)
            for row_data in query:
                row_number = self.homeTable.rowCount()
                self.homeTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.homeTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Function  Input
    def funcInput(self):
        self.newInput = inputWood.UI_Inputwood()
        self.hide()

    # Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.hide()

    # Function Resize
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.hide()

    # Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.hide()

    # Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.hide()

    # Function Sale
    def funcSale(self):
        self.newSale = saleWood.UI_Salewood()
        self.hide()


# Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

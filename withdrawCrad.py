from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mySQL import database
db = database()

class withdeawcrad (QWidget):
    def __init__(self,list_withdraw_cut,date,type_cut):
        super().__init__()
        self.setWindowTitle("ใบเบิกไม้")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450,150,960,600)
        self.setStyleSheet("background-color:white;")
        self.setFixedSize(self.size())
        self.list_woodcut_withdraw = list_withdraw_cut
        self.str_date = date
        self.type_cut = type_cut
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.displayTable()
        self.funcShowdata()
        self.layout()

    def display(self):

        self.text_withdrawid = QLabel(self)
        self.text_withdrawid.setText("เลขที่เอกสาร : ")
        self.text_date = QLabel(self)
        self.text_date.setText("วันที่เบิกไม้: " + str(self.str_date))
        self.text_type = QLabel(self)
        self.text_type.setText("ประเภทการเบิกไม้ : "+self.type_cut)

        icon = QPixmap('icons/s.png')
        self.text_company = QLabel("<font color='Black' size='5'>Siam Kyohwa Seisakusho Co., Ltd.</font> ", self)
        self.label = QLabel(self)
        self.label.setPixmap(icon)
        self.label.setAlignment(Qt.AlignCenter)
        self.text_company.setMinimumHeight(icon.height())

        self.btn_confirm = QPushButton(self)
        self.btn_confirm.setText("ยืนยัน")
        self.btn_confirm.setShortcut('Return')
        self.btn_confirm.setStyleSheet("""
              QPushButton {
                  background-color: #008CBA;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid #008CBA;
                  color: black;
              }
          """)

        self.btn_confirm.clicked.connect(self.funcSave_Withdraw)

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.headLayout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()
        self.CenterLayout1 = QVBoxLayout()
        self.CenterLayout2 = QVBoxLayout()
        self.tableLayout = QHBoxLayout()

        self.groupBox1 = QWidget()
        self.groupBox2 = QWidget()
        self.btn_box = QHBoxLayout()

        #
        self.headLayout.addStretch()
        self.headLayout.addWidget(self.label)
        self.headLayout.addWidget(self.text_company)
        self.headLayout.addStretch()

        self.CenterLayout1.addWidget(self.text_withdrawid)
        self.CenterLayout1.addWidget(self.text_date)
        self.CenterLayout1.addWidget(self.text_type)
        self.groupBox1.setLayout(self.CenterLayout1)

        self.tableLayout.addWidget(self.table_withdraw)

        self.btn_box.addStretch()
        self.btn_box.addWidget(self.btn_confirm)

        self.mainTopLayout.addWidget(self.groupBox1)
        self.mainLayout.addLayout(self.headLayout)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.tableLayout)
        self.mainLayout.addLayout(self.btn_box)

        self.setLayout(self.mainLayout)

    def displayTable(self):
        self.table_withdraw = QTableWidget()
        self.table_withdraw.setColumnCount(7)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน']
        self.table_withdraw.setHorizontalHeaderLabels(header)
        self.table_withdraw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        column_size = self.table_withdraw.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i,QHeaderView.Stretch)

    def funcShowdata(self):
        query = self.list_woodcut_withdraw
        for row_data in query:
            row_number = self.table_withdraw.rowCount()
            self.table_withdraw.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_withdraw.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def funcSave_Withdraw(self):
        QMessageBox.information(self,"", "เบิกไม้สำเร็จ")
        self.close()

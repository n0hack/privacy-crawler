import os
import time
import pickle
from crawler import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.user_info = ['', '']   # 유저 정보
        self.blogger_list = ''      # 블로거 리스트 정보
        self.num_of_row = 0         # 리스트 개수

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 435)
        MainWindow.setMinimumSize(QtCore.QSize(482, 435))
        MainWindow.setMaximumSize(QtCore.QSize(482, 435))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 348, 301, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(230, 19, 71, 50))
        self.btn_login.setObjectName("btn_login")
        self.lb_process = QtWidgets.QLabel(self.centralwidget)
        self.lb_process.setGeometry(QtCore.QRect(22, 351, 51, 16))
        self.lb_process.setObjectName("lb_process")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(387, 347, 75, 23))
        self.btn_save.setObjectName("btn_save")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(21, 383, 434, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 405, 379, 16))
        self.label_2.setObjectName("label_2")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(310, 20, 71, 50))
        self.btn_start.setObjectName("btn_start")
        self.btn_readme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_readme.setGeometry(QtCore.QRect(390, 20, 71, 50))
        self.btn_readme.setObjectName("btn_readme")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 441, 261))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(140)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 200, 48))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lb_id = QtWidgets.QLabel(self.splitter)
        self.lb_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_id.setObjectName("lb_id")
        self.txt_id = QtWidgets.QLineEdit(self.splitter)
        self.txt_id.setMaxLength(16)
        self.txt_id.setPlaceholderText("")
        self.txt_id.setObjectName("txt_id")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lb_pw = QtWidgets.QLabel(self.splitter_2)
        self.lb_pw.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_pw.setObjectName("lb_pw")
        self.txt_pw = QtWidgets.QLineEdit(self.splitter_2)
        self.txt_pw.setMaxLength(16)
        self.txt_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pw.setPlaceholderText("")
        self.txt_pw.setObjectName("txt_pw")
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phone Number Extractor Ver 1.0.0"))
        self.btn_login.setText(_translate("MainWindow", "계정 저장"))
        self.lb_process.setText(_translate("MainWindow", "준비 중"))
        self.btn_save.setText(_translate("MainWindow", "결과 저장"))
        self.label.setText(_translate("MainWindow", "* 인터넷에서 활동한 기록을 모두 불러오는 것으로 번호가 바뀌었을 수 있습니다."))
        self.label_2.setText(_translate("MainWindow", "* 수집 시 1인당 1~2초의 시간이 소요 됩니다. (다른 작업 최대한 지양)"))
        self.btn_start.setText(_translate("MainWindow", "수집 시작"))
        self.btn_readme.setText(_translate("MainWindow", "사용법"))
        self.tableWidget.verticalHeader().setVisible(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "아이디"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "이메일"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "전화번호"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lb_id.setText(_translate("MainWindow", "아이디　"))
        self.lb_pw.setText(_translate("MainWindow", "비밀번호"))

        # 초기 로그인 정보 입력
        if os.path.isfile('lib.dll'):
            with open('lib.dll', 'rb') as f:
                self.user_info = pickle.load(f)
                self.txt_id.setText(self.user_info[0])
                self.txt_pw.setText(self.user_info[1])

        # 이벤트 연결
        self.connectEvent(MainWindow)
        # 크롤러 연결
        self.crawler = Thread(self.centralwidget, self)
        self.crawler.label_changed.connect(self.update_label)
        self.crawler.progress_changed.connect(self.progressBar.setValue)
        self.crawler.list_changed.connect(self.update_list)
        self.crawler.list_reset.connect(self.clear_table)
        self.crawler.num_of_row_changed.connect(self.update_num_of_row)

    # 시그널
    def update_label(self, val):
        self.lb_process.setText(val)

    def update_list(self, num_of_row, data_list):
        self.tableWidget.insertRow(num_of_row)
        self.tableWidget.setItem(num_of_row, 0, QtWidgets.QTableWidgetItem(data_list[0]))
        self.tableWidget.item(num_of_row, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(num_of_row, 1, QtWidgets.QTableWidgetItem(data_list[1]))
        self.tableWidget.item(num_of_row, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(num_of_row, 2, QtWidgets.QTableWidgetItem(data_list[2]))
        self.tableWidget.item(num_of_row, 2).setTextAlignment(QtCore.Qt.AlignCenter)

    def update_num_of_row(self, val):
        self.num_of_row = val

    def clear_table(self):
        temp = 0
        if temp < self.num_of_row:
            while temp < self.num_of_row:
                self.tableWidget.removeRow(self.num_of_row - 1)
                self.num_of_row = self.num_of_row - 1
        self.num_of_row = 0

    # 이벤트 연결 메소드
    def connectEvent(self, MainWindow):
        self.btn_login.clicked.connect(self.clickLogin)     # 계정 저장
        self.btn_start.clicked.connect(self.clickStart)     # 수집 시작
        self.btn_readme.clicked.connect(self.clickReadme)   # 사용법
        self.btn_save.clicked.connect(self.clickSave)       # 결과 저장

    # 버튼 이벤트 (계정 저장)
    def clickLogin(self, event):
        self.user_info[0] = self.txt_id.text()
        self.user_info[1] = self.txt_pw.text()

        with open('lib.dll', 'wb') as f:
            pickle.dump(self.user_info, f)

        QtWidgets.QMessageBox.information(self.centralwidget, '안내', '저장 완료', QtWidgets.QMessageBox.Ok)

    # 버튼 이벤트 (수집 시작)
    def clickStart(self, event):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, '블로거 리스트 (Text File)', '', '텍스트 파일(*.txt)')
        
        if self.fname[0]:
            self.crawler.start()
        else:
            QtWidgets.QMessageBox.about(self.centralwidget, 'Warning', '파일을 선택하지 않았습니다.')

    # 버튼 이벤트 (사용법)
    def clickReadme(self, event):
        os.startfile('readme.txt')

    # 버튼 이벤트 (결과 저장)
    def clickSave(self, event):
        from datetime import datetime

        fname = './result/수집결과_{0}.txt'.format(int(datetime.now().timestamp()))
        with open(fname, mode='wt', encoding='utf-8') as f:
            temp = 0
            while temp < self.num_of_row:
                if self.tableWidget.item(temp, 2).text() != '':
                    w1 = self.tableWidget.item(temp, 0).text()
                    w2 = self.tableWidget.item(temp, 1).text()
                    w3 = self.tableWidget.item(temp, 2).text()
                    f.write(w1 + ' [ ' + w2 + ' / ' + w3 + ' ]\n')
                temp = temp + 1

        QtWidgets.QMessageBox.information(self.centralwidget, '안내', 'result 폴더에\n저장되었습니다.', QtWidgets.QMessageBox.Ok)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1000, 700)
        Window.setMinimumSize(QtCore.QSize(500, 625))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/ICON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Window)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loading_page = QtWidgets.QWidget()
        self.loading_page.setObjectName("loading_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.loading_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.info_label = QtWidgets.QLabel(self.loading_page)
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.gridLayout_2.addWidget(self.info_label, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.logo_label = QtWidgets.QLabel(self.loading_page)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/pictures/logo.svg"))
        self.logo_label.setObjectName("logo_label")
        self.gridLayout_2.addWidget(self.logo_label, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        self.loading_label = QtWidgets.QLabel(self.loading_page)
        self.loading_label.setText("")
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setObjectName("loading_label")
        self.gridLayout_2.addWidget(self.loading_label, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.loading_page)
        self.account_page = QtWidgets.QWidget()
        self.account_page.setObjectName("account_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.account_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.creator_label = QtWidgets.QLabel(self.account_page)
        self.creator_label.setOpenExternalLinks(True)
        self.creator_label.setObjectName("creator_label")
        self.gridLayout_3.addWidget(self.creator_label, 5, 1, 1, 1)
        self.info_error_label = QtWidgets.QLabel(self.account_page)
        self.info_error_label.setText("")
        self.info_error_label.setObjectName("info_error_label")
        self.gridLayout_3.addWidget(self.info_error_label, 4, 1, 1, 1)
        self.label_buttons_widget = QtWidgets.QWidget(self.account_page)
        self.label_buttons_widget.setObjectName("label_buttons_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.label_buttons_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.delete_button = QtWidgets.QPushButton(self.label_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pictures/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setCheckable(True)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout_4.addWidget(self.delete_button, 0, 1, 1, 1)
        self.accounts_label = QtWidgets.QLabel(self.label_buttons_widget)
        self.accounts_label.setObjectName("accounts_label")
        self.gridLayout_4.addWidget(self.accounts_label, 0, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.label_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pictures/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon2)
        self.add_button.setObjectName("add_button")
        self.gridLayout_4.addWidget(self.add_button, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.label_buttons_widget, 1, 1, 1, 1)
        self.acc_listview = QtWidgets.QListWidget(self.account_page)
        self.acc_listview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.acc_listview.setProperty("showDropIndicator", False)
        self.acc_listview.setObjectName("acc_listview")
        self.gridLayout_3.addWidget(self.acc_listview, 3, 1, 1, 1)
        self.logo_label_accounts = QtWidgets.QLabel(self.account_page)
        self.logo_label_accounts.setText("")
        self.logo_label_accounts.setPixmap(QtGui.QPixmap(":/pictures/logo.svg"))
        self.logo_label_accounts.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label_accounts.setObjectName("logo_label_accounts")
        self.gridLayout_3.addWidget(self.logo_label_accounts, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.account_page)
        self.add_account_page = QtWidgets.QWidget()
        self.add_account_page.setObjectName("add_account_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.add_account_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 6, 0, 1, 1)
        self.email_label = QtWidgets.QLabel(self.add_account_page)
        self.email_label.setObjectName("email_label")
        self.gridLayout_6.addWidget(self.email_label, 1, 0, 1, 2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.add_account_page)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_6.addWidget(self.password_lineEdit, 5, 0, 1, 1)
        self.buttons_widget = QtWidgets.QWidget(self.add_account_page)
        self.buttons_widget.setObjectName("buttons_widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.buttons_widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cancel_button = QtWidgets.QPushButton(self.buttons_widget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout_7.addWidget(self.cancel_button, 0, 0, 1, 1)
        self.accept_button = QtWidgets.QPushButton(self.buttons_widget)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout_7.addWidget(self.accept_button, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.buttons_widget, 7, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem5, 3, 0, 1, 1)
        self.email_lineEdit = QtWidgets.QLineEdit(self.add_account_page)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.gridLayout_6.addWidget(self.email_lineEdit, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 0, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.add_account_page)
        self.password_label.setObjectName("password_label")
        self.gridLayout_6.addWidget(self.password_label, 4, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(self.add_account_page)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.gridLayout_6.addWidget(self.error_label, 8, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_account_page)
        self.webview_page = QtWidgets.QWidget()
        self.webview_page.setObjectName("webview_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.webview_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.webview_page)
        self.webView.setObjectName("webView")
        self.gridLayout_5.addWidget(self.webView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.webview_page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Window)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "IServ"))
        self.creator_label.setText(_translate("Window", "<html><head/><body><p>Diese unoffizielle <a href=\"http://iserv.eu\"><span style=\" text-decoration: underline; color:#0000ff;\">IServ</span></a> Desktop App wurde von Philipp Neumann (<a href=\"https://github.com/FunProgramer\"><span style=\" text-decoration: underline; color:#0000ff;\">FunProgramer auf Github</span></a>) mit <a href=\"http://python.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Python</span></a>, <a href=\"https://riverbankcomputing.com/software/pyqt\"><span style=\" text-decoration: underline; color:#0000ff;\">PyQt5</span></a> und <a href=\"https://www.pyinstaller.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Pyinstaller</span></a> entwickelt.</p></body></html>"))
        self.accounts_label.setText(_translate("Window", "Accounts"))
        self.email_label.setText(_translate("Window", "IServ-Email"))
        self.cancel_button.setText(_translate("Window", "Abbrechen"))
        self.accept_button.setText(_translate("Window", "OK"))
        self.password_label.setText(_translate("Window", "Password"))
from PyQt5 import QtWebEngineWidgets
import resource_rc

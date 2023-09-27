# -*- coding: utf-8 -*-
#      L1PyLogin is a client login simulator for Lineage 8.8
#
#      Copyright (C) 2023  lukeme1107@gmail.com
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator


class UiMainWindow(object):
    def __init__(self):
        self.central_widget = None
        self.account_label = None
        self.account_line_edit = None
        self.password_label = None
        self.password_line_edit = None
        self.ip_label = None
        self.ip_line_edit = None
        self.port_label = None
        self.port_line_edit = None
        self.login_button = None

    def set_components(self, main):
        main.setObjectName("main_window")
        main.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        main.setBaseSize(331, 178)
        main.setMinimumSize(331, 178)
        main.setMaximumSize(331, 178)
        self.central_widget = QtWidgets.QWidget(main)
        self.central_widget.setObjectName("central_widget")
        self.account_label = QtWidgets.QLabel(self.central_widget)
        self.account_label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.account_label.setObjectName("account_label")
        self.account_line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.account_line_edit.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.account_line_edit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhLowercaseOnly)
        self.account_line_edit.setObjectName("account_line_edit")
        self.password_label = QtWidgets.QLabel(self.central_widget)
        self.password_label.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.password_label.setObjectName("password_label")
        self.password_line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.password_line_edit.setGeometry(QtCore.QRect(10, 80, 151, 20))
        self.password_line_edit.setInputMethodHints(
            QtCore.Qt.InputMethodHint.ImhHiddenText | QtCore.Qt.InputMethodHint.ImhNoAutoUppercase |
            QtCore.Qt.InputMethodHint.ImhNoPredictiveText | QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.ip_label = QtWidgets.QLabel(self.central_widget)
        self.ip_label.setGeometry(QtCore.QRect(170, 10, 151, 16))
        self.ip_label.setObjectName("ip_label")
        self.ip_line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.ip_line_edit.setGeometry(QtCore.QRect(170, 30, 151, 20))
        self.ip_line_edit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUrlCharactersOnly)
        self.ip_line_edit.setObjectName("ip_line_edit")
        self.port_label = QtWidgets.QLabel(self.central_widget)
        self.port_label.setGeometry(QtCore.QRect(170, 60, 151, 16))
        self.port_label.setObjectName("port_label")
        self.port_line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.port_line_edit.setGeometry(QtCore.QRect(170, 80, 151, 20))
        self.port_line_edit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.port_line_edit.setValidator(QIntValidator())
        self.port_line_edit.setObjectName("port_line_edit")
        self.login_button = QtWidgets.QPushButton(self.central_widget)
        self.login_button.setGeometry(QtCore.QRect(10, 120, 311, 41))
        self.login_button.setObjectName("login_button")
        main.setCentralWidget(self.central_widget)
        self.translate_ui(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def translate_ui(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main_window", "L1PyLogin for Lineage 8.8c"))
        self.account_label.setText(_translate("main_window", "Account:"))
        self.password_label.setText(_translate("main_window", "Password"))
        self.ip_label.setText(_translate("main_window", "Server Address:"))
        self.ip_line_edit.setText('127.0.0.1')
        self.port_label.setText(_translate("main_window", "Server Port:"))
        self.port_line_edit.setText('2000')
        self.login_button.setText(_translate("main_window", "Login"))

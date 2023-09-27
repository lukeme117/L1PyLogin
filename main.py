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
import sys

import PyQt5.QtWidgets
from elevate import elevate

from main_window import UiMainWindow
from process_handler import create_process


class Main(PyQt5.QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.set_components(self)
        self.login_button.clicked.connect(self.login_event)

    def login_event(self):
        if self.account_line_edit.text() == '':
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Error', 'Input account plz')
        elif self.password_line_edit.text() == '':
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Error', 'Input password plz')
        elif self.ip_line_edit.text() == '':
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Error', 'Input Server Address plz')
        elif self.port_line_edit.text() == '':
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Error', 'Input Port Address plz')
        else:
            create_process(self, self)


if __name__ == '__main__':
    """
    Lineage Client Emulator for Login by lukeme1107@gmail.com
    """
    elevate(show_console=False)
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec_())

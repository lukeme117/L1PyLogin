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
import ctypes
import subprocess
from pathlib import Path
from subprocess import DETACHED_PROCESS

import win32api
from PyQt5.QtWidgets import QMessageBox

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)


def create_process(self, main):
    """
    found lin.bin and create lin.bin process.
    """
    lin_bin_path = Path("./lin.bin")
    if lin_bin_path.exists() and lin_bin_path.is_file():
        args = '1 1'
        process = subprocess.Popen([self.lin_bin_path, args], creationflags=DETACHED_PROCESS)
        win32_process = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, process.pid)
        edit_process(main, win32_process)
    else:
        QMessageBox.critical(main, 'Error', f'{lin_bin_path.absolute()}  not found!')


def edit_process(main, process):
    """
    TODO something
    """
    win32_kernel = ctypes.windll.loadLibrary(r'C:\Windows\System32\kernel32.dll')
    data = ctypes.c_long
    """
    BOOL ReadProcessMemory(
    [in]  HANDLE  hProcess,
    [in]  LPCVOID lpBaseAddress,
    [out] LPVOID  lpBuffer,
    [in]  SIZE_T  nSize,
    [out] SIZE_T  *lpNumberOfBytesRead
    );
    """
    read_lp_number_of_bytes_written = ctypes.c_size_t(0)
    win32_kernel.ReadProcessMemory(int(process), 0x00000000, ctypes.byref(data), 4, read_lp_number_of_bytes_written)
    """
    BOOL WriteProcessMemory(
    [in]  HANDLE  hProcess,
    [in]  LPVOID  lpBaseAddress,
    [in]  LPCVOID lpBuffer,
    [in]  SIZE_T  nSize,
    [out] SIZE_T  *lpNumberOfBytesWritten
    );
    """
    read_lp_number_of_bytes_written = ctypes.c_size_t(0)
    win32_kernel.WriteProcessMemory(int(process), 0x00000000, ctypes.byref(data), 4, read_lp_number_of_bytes_written)
    QMessageBox.about(main, 'Login', f'Run: {process.args}')

#!/usr/bin/env python

#  Copyright 2016 by Dai Trying
#
#  This file is part of daithemebackup.
#
#     daithemebackup is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     daithemebackup is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with daithemebackup. If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, QFileDialog)
import sys
import themebackup
import tarfile
import os
import getopt
import subprocess
from shutil import copyfile

VERSION = "0.0.2-11"
home = os.path.expanduser('~')
my_dir = ".config/daithemebackup"
full_path = os.path.join(home, my_dir)
config_file = os.path.join(home, my_dir, 'config.file')
file_name = "themebackup_"
backup_file_name = ""

if not os.path.isdir(full_path):
    os.makedirs(full_path)
if not os.path.exists(config_file):
    copyfile('/usr/share/daithemebackup/config.file', config_file)


class ExampleApp(QMainWindow, themebackup.Ui_DaiThemeBackup):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.reset_to_q4os.clicked.connect(reset_to_q4desktop)
        self.create_backup.clicked.connect(create_new_backup)
        self.restore_backup.clicked.connect(restore_from_file)


def reset_to_q4desktop():
    result = QMessageBox.question(QMessageBox(), 'RESET DESKTOP TO Q4OS DEFAULT',
                                  'I am about to reset the desktop to the default Q4OS desktop!\nAre you sure you want'
                                  ' to do this?', QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        t = tarfile.open("/usr/share/apps/q4os_system/q4home.tar", 'r')
        t.extractall(home + "/")
        result = QMessageBox.question(QMessageBox(), 'DEFAULT DESKTOP RESTORED',
                                      'I have restored the default Q4OS desktop\nYou must re-login for the settings to'
                                      ' take effect\nShould I logout now?', QMessageBox.Yes, QMessageBox.No)
        if result == QMessageBox.Yes:
            subprocess.call(['dcop ksmserver ksmserver logout 0 0 3'], shell=True)
        elif result == QMessageBox.No:
            QMessageBox.information(QMessageBox(), 'LogOut denied', "Don't forget your settings are not yet set\n"
                                                                    "Please re-login as soon as possible!",
                                    QMessageBox.Ok)
    else:
        QMessageBox.information(QMessageBox(), 'RESET DESKTOP CANCELLED', "I have not changed your desktop as you "
                                                                          "cancelled the operation.", QMessageBox.Ok)


def restore_from_file():
    this_file_name = QFileDialog.getOpenFileName(QFileDialog(), 'Open file', full_path + "/", "Backup files (*.tar.gz)")
    if this_file_name[0]:
        t = tarfile.open(this_file_name[0], 'r')
        t.extractall('/')
        result = QMessageBox.question(QMessageBox(), "DESKTOP RESTORED",
                                      "I have restored the desktop from your backup file\nYou must re-login for the"
                                      " settings to tke effect\nShould I logout now?", QMessageBox.Yes,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            subprocess.call(["dcop ksmserver ksmserver logout 0 0 3"], shell=True)
        elif result == QMessageBox.No:
            QMessageBox.information(QMessageBox(), 'LogOut denied',
                                    "Don't forget your settings are not yet set\nPlease re-login as soon as "
                                    "possible!", QMessageBox.Ok)


def create_new_backup():
    global backup_file_name
    backup_file_name = ""
    rf_list = []
    all_files = []
    with open(config_file) as f:
        for line in f:
            if line.startswith('#'):
                continue
            if line.strip() == "":
                continue
            if not line.startswith('/home/'):
                file_with_path = home + '/' + line.strip()
            else:
                file_with_path = line.strip()

            if os.path.exists(file_with_path):
                all_files.append(file_with_path)
            else:
                print(file_with_path + ' does not exist')

    start_num = 1
    tar = tarfile.open("/usr/share/apps/q4os_system/q4home.tar")
    for tarinfo in tar:
        this_file = os.path.join(home, tarinfo.name[2:])
        if tarinfo.isreg():
            if os.path.exists(this_file):
                rf_list.append(this_file)
    tar.close()

    for new_file in all_files:
        if new_file in rf_list:
            pass
        else:
            rf_list.append(new_file)

    while os.path.exists(os.path.join(full_path, file_name + "%03d" % start_num + ".tar.gz")):
        start_num += 1
    file_with_path = os.path.join(full_path, file_name + "%03d" % start_num + ".tar.gz")
    backup_file_name = file_with_path
    with tarfile.open(file_with_path, "w:gz") as tar:
        for name in rf_list:
                tar.add(name)
    QMessageBox.information(QMessageBox(), "BACKUP CREATED",
                            "Your backup file has been created and can be found at...\n" + backup_file_name,
                            QMessageBox.Ok)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "vh")
    except getopt.GetoptError:
        print 'Option Error\n  Please check your options before trying again.\n\n  Usage:\n' \
              '    daithemebackup -h <help> -v <version>\n'
        sys.exit(9)
    for opt, arg in opts:
        if opt in ("-h", "-?", "--help"):
            print '\nUsage:\n    daithemebackup -h <help -v <version>\n'
            sys.exit(0)
        elif opt in ("-v", "--version"):
            print "\nVersion is %s\n" % VERSION
            sys.exit(0)

    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main(sys.argv[1:])

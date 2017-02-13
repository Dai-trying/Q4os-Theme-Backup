# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'themebackup.ui'
#
# Created: Sun Oct 16 14:43:51 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DaiThemeBackup(object):
    def setupUi(self, DaiThemeBackup):
        DaiThemeBackup.setObjectName("DaiThemeBackup")
        DaiThemeBackup.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DaiThemeBackup.sizePolicy().hasHeightForWidth())
        DaiThemeBackup.setSizePolicy(sizePolicy)
        DaiThemeBackup.setMinimumSize(QtCore.QSize(300, 200))
        DaiThemeBackup.setMaximumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/icons/hicolor/48x48/apps/welcome-screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DaiThemeBackup.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DaiThemeBackup)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.reset_to_q4os = QtWidgets.QPushButton(self.centralwidget)
        self.reset_to_q4os.setObjectName("reset_to_q4os")
        self.gridLayout.addWidget(self.reset_to_q4os, 0, 0, 1, 1)
        self.create_backup = QtWidgets.QPushButton(self.centralwidget)
        self.create_backup.setObjectName("create_backup")
        self.gridLayout.addWidget(self.create_backup, 1, 0, 1, 1)
        self.restore_backup = QtWidgets.QPushButton(self.centralwidget)
        self.restore_backup.setObjectName("restore_backup")
        self.gridLayout.addWidget(self.restore_backup, 2, 0, 1, 1)
        DaiThemeBackup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DaiThemeBackup)
        self.statusbar.setObjectName("statusbar")
        DaiThemeBackup.setStatusBar(self.statusbar)

        self.retranslateUi(DaiThemeBackup)
        QtCore.QMetaObject.connectSlotsByName(DaiThemeBackup)

    def retranslateUi(self, DaiThemeBackup):
        _translate = QtCore.QCoreApplication.translate
        DaiThemeBackup.setWindowTitle(_translate("DaiThemeBackup", "Dai\'s Theme Backup"))
        self.reset_to_q4os.setText(_translate("DaiThemeBackup", "Reset to Q4OS default Desktop"))
        self.create_backup.setText(_translate("DaiThemeBackup", "Create Backup now"))
        self.restore_backup.setText(_translate("DaiThemeBackup", "Restore From Backup File"))


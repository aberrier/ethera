# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 684)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 119, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 119, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 101, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 68, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 119, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 119, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 101, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 119, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 101, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        MainWindow.setPalette(palette)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 280, 331, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.textLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.textLayout.setContentsMargins(8, 8, 8, 8)
        self.textLayout.setSpacing(6)
        self.textLayout.setObjectName("textLayout")
        self.labelUp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelUp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUp.setObjectName("labelUp")
        self.textLayout.addWidget(self.labelUp)
        self.labelMiddle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelMiddle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMiddle.setObjectName("labelMiddle")
        self.textLayout.addWidget(self.labelMiddle)
        self.labelDown = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDown.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDown.setObjectName("labelDown")
        self.textLayout.addWidget(self.labelDown)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 350, 301, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.manualLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.manualLayout.setContentsMargins(11, 11, 11, 11)
        self.manualLayout.setSpacing(6)
        self.manualLayout.setObjectName("manualLayout")
        self.manualLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.manualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLabel.setObjectName("manualLabel")
        self.manualLayout.addWidget(self.manualLabel)
        self.manualEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.manualEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.manualEdit.setObjectName("manualEdit")
        self.manualLayout.addWidget(self.manualEdit)
        self.validateButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.validateButton.setObjectName("validateButton")
        self.manualLayout.addWidget(self.validateButton)
        spacerItem = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.manualLayout.addItem(spacerItem)
        self.activateManualButton = QtWidgets.QPushButton(self.centralWidget)
        self.activateManualButton.setGeometry(QtCore.QRect(360, 550, 299, 27))
        self.activateManualButton.setObjectName("activateManualButton")
        self.imageWidget = QtWidgets.QWidget(self.centralWidget)
        self.imageWidget.setGeometry(QtCore.QRect(380, 20, 261, 231))
        self.imageWidget.setObjectName("imageWidget")
        self.image = QtWidgets.QLabel(self.imageWidget)
        self.image.setGeometry(QtCore.QRect(20, 20, 181, 141))
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setText("")
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelUp.setText(_translate("MainWindow", "TextLabel"))
        self.labelMiddle.setText(_translate("MainWindow", "TextLabel"))
        self.labelDown.setText(_translate("MainWindow", "TextLabel"))
        self.manualLabel.setText(_translate("MainWindow", "TextLabel"))
        self.validateButton.setText(_translate("MainWindow", "Valider"))
        self.activateManualButton.setText(_translate("MainWindow", "Activer la saisie manuelle"))


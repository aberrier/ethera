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
        MainWindow.resize(1230, 777)
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
        self.textLayoutContainer = QtWidgets.QFrame(self.centralWidget)
        self.textLayoutContainer.setGeometry(QtCore.QRect(290, 20, 591, 241))
        self.textLayoutContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textLayoutContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textLayoutContainer.setObjectName("textLayoutContainer")
        self.textLayout = QtWidgets.QVBoxLayout(self.textLayoutContainer)
        self.textLayout.setContentsMargins(8, 8, 8, 8)
        self.textLayout.setSpacing(6)
        self.textLayout.setObjectName("textLayout")
        self.labelMiddle = QtWidgets.QLabel(self.textLayoutContainer)
        self.labelMiddle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMiddle.setWordWrap(True)
        self.labelMiddle.setObjectName("labelMiddle")
        self.textLayout.addWidget(self.labelMiddle)
        self.manualLayoutContainer = QtWidgets.QWidget(self.centralWidget)
        self.manualLayoutContainer.setGeometry(QtCore.QRect(0, 440, 301, 251))
        self.manualLayoutContainer.setObjectName("manualLayoutContainer")
        self.manualLayout = QtWidgets.QVBoxLayout(self.manualLayoutContainer)
        self.manualLayout.setContentsMargins(11, 11, 11, 11)
        self.manualLayout.setSpacing(6)
        self.manualLayout.setObjectName("manualLayout")
        self.manualLabel = QtWidgets.QLabel(self.manualLayoutContainer)
        self.manualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLabel.setWordWrap(True)
        self.manualLabel.setObjectName("manualLabel")
        self.manualLayout.addWidget(self.manualLabel)
        self.manualEdit = QtWidgets.QLineEdit(self.manualLayoutContainer)
        self.manualEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.manualEdit.setObjectName("manualEdit")
        self.manualLayout.addWidget(self.manualEdit)
        self.validateButton = QtWidgets.QPushButton(self.manualLayoutContainer)
        self.validateButton.setObjectName("validateButton")
        self.manualLayout.addWidget(self.validateButton)
        spacerItem = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.manualLayout.addItem(spacerItem)
        self.activateManualButton = QtWidgets.QPushButton(self.centralWidget)
        self.activateManualButton.setGeometry(QtCore.QRect(440, 720, 331, 41))
        self.activateManualButton.setObjectName("activateManualButton")
        self.imageWidget = QtWidgets.QWidget(self.centralWidget)
        self.imageWidget.setGeometry(QtCore.QRect(390, 350, 411, 341))
        self.imageWidget.setObjectName("imageWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.imageWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image = QtWidgets.QLabel(self.imageWidget)
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image.setText("")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.horizontalLayout.addWidget(self.image)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(990, 10, 231, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUp = QtWidgets.QLabel(self.widget)
        self.labelUp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUp.setWordWrap(True)
        self.labelUp.setObjectName("labelUp")
        self.verticalLayout.addWidget(self.labelUp)
        self.labelDown = QtWidgets.QLabel(self.widget)
        self.labelDown.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDown.setWordWrap(True)
        self.labelDown.setObjectName("labelDown")
        self.verticalLayout.addWidget(self.labelDown)
        self.labelDown_2 = QtWidgets.QLabel(self.widget)
        self.labelDown_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDown_2.setWordWrap(True)
        self.labelDown_2.setObjectName("labelDown_2")
        self.verticalLayout.addWidget(self.labelDown_2)
        self.labelDown_3 = QtWidgets.QLabel(self.widget)
        self.labelDown_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDown_3.setWordWrap(True)
        self.labelDown_3.setObjectName("labelDown_3")
        self.verticalLayout.addWidget(self.labelDown_3)
        self.cameraFrame = QtWidgets.QFrame(self.centralWidget)
        self.cameraFrame.setGeometry(QtCore.QRect(30, 20, 191, 171))
        self.cameraFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.cameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraFrame.setMidLineWidth(2)
        self.cameraFrame.setObjectName("cameraFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cameraFrame)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camera = QtWidgets.QLabel(self.cameraFrame)
        self.camera.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.horizontalLayout_2.addWidget(self.camera)
        self.faceIndicatorWidget = QtWidgets.QWidget(self.centralWidget)
        self.faceIndicatorWidget.setGeometry(QtCore.QRect(1000, 210, 51, 51))
        self.faceIndicatorWidget.setObjectName("faceIndicatorWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.faceIndicatorWidget)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.faceIndicator = QtWidgets.QLabel(self.faceIndicatorWidget)
        self.faceIndicator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.faceIndicator.setFrameShadow(QtWidgets.QFrame.Plain)
        self.faceIndicator.setText("")
        self.faceIndicator.setTextFormat(QtCore.Qt.RichText)
        self.faceIndicator.setScaledContents(True)
        self.faceIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.faceIndicator.setObjectName("faceIndicator")
        self.horizontalLayout_5.addWidget(self.faceIndicator)
        self.converseIndicatorWidget = QtWidgets.QWidget(self.centralWidget)
        self.converseIndicatorWidget.setGeometry(QtCore.QRect(1090, 210, 51, 51))
        self.converseIndicatorWidget.setObjectName("converseIndicatorWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.converseIndicatorWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.converseIndicator = QtWidgets.QLabel(self.converseIndicatorWidget)
        self.converseIndicator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.converseIndicator.setFrameShadow(QtWidgets.QFrame.Plain)
        self.converseIndicator.setText("")
        self.converseIndicator.setTextFormat(QtCore.Qt.RichText)
        self.converseIndicator.setScaledContents(True)
        self.converseIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.converseIndicator.setObjectName("converseIndicator")
        self.horizontalLayout_3.addWidget(self.converseIndicator)
        self.emotionIndicatorWidget = QtWidgets.QWidget(self.centralWidget)
        self.emotionIndicatorWidget.setGeometry(QtCore.QRect(1170, 210, 51, 51))
        self.emotionIndicatorWidget.setObjectName("emotionIndicatorWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.emotionIndicatorWidget)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.emotionIndicator = QtWidgets.QLabel(self.emotionIndicatorWidget)
        self.emotionIndicator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.emotionIndicator.setFrameShadow(QtWidgets.QFrame.Plain)
        self.emotionIndicator.setText("")
        self.emotionIndicator.setTextFormat(QtCore.Qt.RichText)
        self.emotionIndicator.setScaledContents(True)
        self.emotionIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.emotionIndicator.setObjectName("emotionIndicator")
        self.horizontalLayout_4.addWidget(self.emotionIndicator)
        self.nextCamera = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.nextCamera.setGeometry(QtCore.QRect(230, 90, 31, 31))
        self.nextCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextCamera.setText("")
        self.nextCamera.setObjectName("nextCamera")
        self.knowProgressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.knowProgressBar.setGeometry(QtCore.QRect(920, 380, 231, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.knowProgressBar.setPalette(palette)
        self.knowProgressBar.setProperty("value", 0)
        self.knowProgressBar.setObjectName("knowProgressBar")
        self.knowProgressText = QtWidgets.QLabel(self.centralWidget)
        self.knowProgressText.setGeometry(QtCore.QRect(930, 337, 213, 41))
        self.knowProgressText.setAlignment(QtCore.Qt.AlignCenter)
        self.knowProgressText.setWordWrap(True)
        self.knowProgressText.setObjectName("knowProgressText")
        self.nobodyProgressText = QtWidgets.QLabel(self.centralWidget)
        self.nobodyProgressText.setGeometry(QtCore.QRect(930, 447, 213, 41))
        self.nobodyProgressText.setAlignment(QtCore.Qt.AlignCenter)
        self.nobodyProgressText.setWordWrap(True)
        self.nobodyProgressText.setObjectName("nobodyProgressText")
        self.nobodyProgressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.nobodyProgressBar.setGeometry(QtCore.QRect(920, 490, 231, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.nobodyProgressBar.setPalette(palette)
        self.nobodyProgressBar.setProperty("value", 0)
        self.nobodyProgressBar.setObjectName("nobodyProgressBar")
        self.unknowProgressText = QtWidgets.QLabel(self.centralWidget)
        self.unknowProgressText.setGeometry(QtCore.QRect(930, 567, 213, 41))
        self.unknowProgressText.setAlignment(QtCore.Qt.AlignCenter)
        self.unknowProgressText.setWordWrap(True)
        self.unknowProgressText.setObjectName("unknowProgressText")
        self.unknowProgressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.unknowProgressBar.setGeometry(QtCore.QRect(920, 610, 231, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 175, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 175, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.unknowProgressBar.setPalette(palette)
        self.unknowProgressBar.setProperty("value", 0)
        self.unknowProgressBar.setObjectName("unknowProgressBar")
        self.textLayoutContainer_2 = QtWidgets.QFrame(self.centralWidget)
        self.textLayoutContainer_2.setGeometry(QtCore.QRect(310, 270, 531, 71))
        self.textLayoutContainer_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textLayoutContainer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textLayoutContainer_2.setObjectName("textLayoutContainer_2")
        self.textLayout_2 = QtWidgets.QVBoxLayout(self.textLayoutContainer_2)
        self.textLayout_2.setContentsMargins(8, 8, 8, 8)
        self.textLayout_2.setSpacing(6)
        self.textLayout_2.setObjectName("textLayout_2")
        self.labelInput = QtWidgets.QLabel(self.textLayoutContainer_2)
        self.labelInput.setText("")
        self.labelInput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInput.setWordWrap(True)
        self.labelInput.setObjectName("labelInput")
        self.textLayout_2.addWidget(self.labelInput)
        self.labelDown_4 = QtWidgets.QLabel(self.centralWidget)
        self.labelDown_4.setGeometry(QtCore.QRect(130, 290, 171, 39))
        self.labelDown_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDown_4.setWordWrap(True)
        self.labelDown_4.setObjectName("labelDown_4")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMiddle.setText(_translate("MainWindow", "TextLabel"))
        self.manualLabel.setText(_translate("MainWindow", "TextLabel"))
        self.validateButton.setText(_translate("MainWindow", "Valider"))
        self.activateManualButton.setText(_translate("MainWindow", "Activer la saisie manuelle"))
        self.labelUp.setText(_translate("MainWindow", "TextLabel"))
        self.labelDown.setText(_translate("MainWindow", "TextLabel"))
        self.labelDown_2.setText(_translate("MainWindow", "Restez appuyé sur C pour lui parler."))
        self.labelDown_3.setText(_translate("MainWindow", "SI vous disparaissez de la caméra, il vous dira en revoir !"))
        self.knowProgressText.setText(_translate("MainWindow", "Reconnaissance de personne connue en cours..."))
        self.nobodyProgressText.setText(_translate("MainWindow", "Attention, vous n\'êtes plus reconnu(e) !"))
        self.unknowProgressText.setText(_translate("MainWindow", "Vérification de la présence d\'une personne inconnue..."))
        self.labelDown_4.setText(_translate("MainWindow", "Ce que j\'ai compris :"))


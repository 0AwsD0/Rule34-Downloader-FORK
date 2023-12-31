# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rule34Downloader(object):
    def setupUi(self, Rule34Downloader):
        Rule34Downloader.setObjectName("Rule34Downloader AUTOMATED")
        Rule34Downloader.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Rule34Downloader.sizePolicy().hasHeightForWidth())
        Rule34Downloader.setSizePolicy(sizePolicy)
        Rule34Downloader.setMinimumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PATH_TO_YOUR_PROJECT_FOLDER\icon34automated.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Rule34Downloader.setWindowIcon(icon)
        Rule34Downloader.setToolTipDuration(-1)
        Rule34Downloader.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Rule34Downloader)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SearchRegion = QtWidgets.QVBoxLayout()
        self.SearchRegion.setObjectName("SearchRegion")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setObjectName("searchInput")
        self.searchInput.setText(" -futanari")
        self.horizontalLayout.addWidget(self.searchInput)
        self.SearchRegion.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.searchProgBar = QtWidgets.QProgressBar(self.centralwidget)
        self.searchProgBar.setProperty("value", 50)
        self.searchProgBar.setTextVisible(False)
        self.searchProgBar.setOrientation(QtCore.Qt.Horizontal)
        self.searchProgBar.setInvertedAppearance(False)
        self.searchProgBar.setObjectName("searchProgBar")
        self.horizontalLayout_2.addWidget(self.searchProgBar)
        self.searchLCD = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLCD.sizePolicy().hasHeightForWidth())
        self.searchLCD.setSizePolicy(sizePolicy)
        self.searchLCD.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.searchLCD.setFont(font)
        self.searchLCD.setAutoFillBackground(False)
        self.searchLCD.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchLCD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchLCD.setLineWidth(1)
        self.searchLCD.setSmallDecimalPoint(False)
        self.searchLCD.setDigitCount(11)
        self.searchLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.searchLCD.setProperty("value", 0.0)
        self.searchLCD.setObjectName("searchLCD")
        self.horizontalLayout_2.addWidget(self.searchLCD)
        self.SearchRegion.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.SearchRegion)
        self.browseRegion = QtWidgets.QHBoxLayout()
        self.browseRegion.setObjectName("browseRegion")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.browseRegion.addWidget(self.label_2)
        self.destinationLine = QtWidgets.QLineEdit(self.centralwidget)
        self.destinationLine.setObjectName("destinationLine")
        self.browseRegion.addWidget(self.destinationLine)
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setObjectName("browseButton")
        self.browseRegion.addWidget(self.browseButton)
        self.verticalLayout_2.addLayout(self.browseRegion)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.currentTask = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTask.sizePolicy().hasHeightForWidth())
        self.currentTask.setSizePolicy(sizePolicy)
        self.currentTask.setMinimumSize(QtCore.QSize(200, 0))
        self.currentTask.setObjectName("currentTask")
        self.horizontalLayout_6.addWidget(self.currentTask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.ETA = QtWidgets.QLabel(self.centralwidget)
        self.ETA.setMinimumSize(QtCore.QSize(200, 0))
        self.ETA.setObjectName("ETA")
        self.horizontalLayout_7.addWidget(self.ETA)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #Add my checkbox
        #self.ckBoxOnlyOne = QtWidgets.QCheckBox(self.centralwidget)
        #self.ckBoxOnlyOne.setObjectName("ckboxOnlyOne")
        #self.ckBoxOnlyOne.setChecked(False)
        #self.verticalLayout.addWidget(self.ckBoxOnlyOne)

        self.ckboxDownloadImages = QtWidgets.QCheckBox(self.centralwidget)
        self.ckboxDownloadImages.setObjectName("ckboxDownloadImages")
        # added below 1 line
        self.ckboxDownloadImages.setChecked(True)
        self.verticalLayout.addWidget(self.ckboxDownloadImages)
        self.ckBoxDownloadVideos = QtWidgets.QCheckBox(self.centralwidget)
        self.ckBoxDownloadVideos.setObjectName("ckBoxDownloadVideos")
        #added below 1 line
        self.ckBoxDownloadVideos.setChecked(True)
        self.verticalLayout.addWidget(self.ckBoxDownloadVideos)
        self.ckBoxSaveURLs = QtWidgets.QCheckBox(self.centralwidget)
        self.ckBoxSaveURLs.setObjectName("ckBoxSaveURLs")
        self.verticalLayout.addWidget(self.ckBoxSaveURLs)
        self.ckBoxSubfolder = QtWidgets.QCheckBox(self.centralwidget)
        self.ckBoxSubfolder.setChecked(True)
        self.ckBoxSubfolder.setObjectName("ckBoxSubfolder")
        self.verticalLayout.addWidget(self.ckBoxSubfolder)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.downloadLimit = QtWidgets.QSpinBox(self.centralwidget)
        self.downloadLimit.setMinimum(-1)
        self.downloadLimit.setMaximum(999999999)
        self.downloadLimit.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.downloadLimit.setProperty("value", -1)
        self.downloadLimit.setObjectName("downloadLimit")
        self.verticalLayout.addWidget(self.downloadLimit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.beginButton = QtWidgets.QPushButton(self.centralwidget)
        self.beginButton.setEnabled(False)
        self.beginButton.setObjectName("beginButton")
        self.horizontalLayout_4.addWidget(self.beginButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_4.addWidget(self.quitButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        Rule34Downloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Rule34Downloader)
        self.statusbar.setObjectName("statusbar")
        Rule34Downloader.setStatusBar(self.statusbar)

        self.retranslateUi(Rule34Downloader)
        QtCore.QMetaObject.connectSlotsByName(Rule34Downloader)

    def retranslateUi(self, Rule34Downloader):
        _translate = QtCore.QCoreApplication.translate
        Rule34Downloader.setWindowTitle(_translate("Rule34Downloader AUTOMATED", "Rule34 Downloader AUTOMATED"))
        self.label.setText(_translate("Rule34Downloader", "Search Tags"))
        self.searchInput.setPlaceholderText(_translate("Rule34Downloader", "Type your tags here, the same as you would on rule34"))
        self.searchButton.setText(_translate("Rule34Downloader", "Search"))
        self.searchLCD.setToolTip(_translate("Rule34Downloader", "How many images have been found"))
        self.label_2.setText(_translate("Rule34Downloader", "Save Directory"))
        self.destinationLine.setPlaceholderText(_translate("Rule34Downloader", "Press browse"))
        self.browseButton.setText(_translate("Rule34Downloader", "Browse"))
        self.label_5.setText(_translate("Rule34Downloader", "Current Task:"))
        self.currentTask.setText(_translate("Rule34Downloader", "Idle"))
        self.label_6.setText(_translate("Rule34Downloader", "ETA:"))
        self.ETA.setText(_translate("Rule34Downloader", "00:00"))
        #
        #self.ckBoxOnlyOne.setToolTip(_translate("Rule34Downloader", "Automatic tag switching OFF while checked"))
        #self.ckBoxOnlyOne.setText(_translate("Rule34Downloader", "Only one tag"))
        #
        self.ckboxDownloadImages.setToolTip(_translate("Rule34Downloader", "Allows the program to download images"))
        self.ckboxDownloadImages.setText(_translate("Rule34Downloader", "Download Images"))
        self.ckBoxDownloadVideos.setToolTip(_translate("Rule34Downloader", "Allows the program to download videos"))
        self.ckBoxDownloadVideos.setText(_translate("Rule34Downloader", "Download Videos"))
        self.ckBoxSaveURLs.setToolTip(_translate("Rule34Downloader", "Save a list of urls in a text file"))
        self.ckBoxSaveURLs.setText(_translate("Rule34Downloader", "Save URLs"))
        self.ckBoxSubfolder.setToolTip(_translate("Rule34Downloader", "Create a subfolder within your specified directory"))
        self.ckBoxSubfolder.setText(_translate("Rule34Downloader", "Create Sub-Folder"))
        self.label_3.setText(_translate("Rule34Downloader", "Download Limit:"))
        self.downloadLimit.setToolTip(_translate("Rule34Downloader", "-1 means no limit"))
        self.beginButton.setText(_translate("Rule34Downloader", "Begin"))
        self.cancelButton.setText(_translate("Rule34Downloader", "Cancel"))
        self.quitButton.setText(_translate("Rule34Downloader", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rule34Downloader = QtWidgets.QMainWindow()
    ui = Ui_Rule34Downloader()
    ui.setupUi(Rule34Downloader)
    Rule34Downloader.show()
    sys.exit(app.exec_())

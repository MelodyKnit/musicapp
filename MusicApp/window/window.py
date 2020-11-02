# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 460)
        Form.setMinimumSize(QSize(720, 460))
        Form.setMaximumSize(QSize(720, 460))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 40, 700, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(340, 50, 20, 401))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 701, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ctl_option = QComboBox(self.layoutWidget)
        self.ctl_option.addItem("")
        self.ctl_option.addItem("")
        self.ctl_option.addItem("")
        self.ctl_option.setObjectName(u"ctl_option")
        self.ctl_option.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ctl_option)

        self.ctl_input = QLineEdit(self.layoutWidget)
        self.ctl_input.setObjectName(u"ctl_input")

        self.horizontalLayout.addWidget(self.ctl_input)

        self.ctl_get = QPushButton(self.layoutWidget)
        self.ctl_get.setObjectName(u"ctl_get")
        self.ctl_get.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ctl_get)

        self.ctl_more = QPushButton(self.layoutWidget)
        self.ctl_more.setObjectName(u"ctl_more")
        self.ctl_more.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ctl_more)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 420, 331, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ctl_deselectAll = QPushButton(self.layoutWidget1)
        self.ctl_deselectAll.setObjectName(u"ctl_deselectAll")
        self.ctl_deselectAll.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.ctl_deselectAll)

        self.ctl_selectAll = QPushButton(self.layoutWidget1)
        self.ctl_selectAll.setObjectName(u"ctl_selectAll")
        self.ctl_selectAll.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.ctl_selectAll)

        self.ctl_deletes = QPushButton(self.layoutWidget1)
        self.ctl_deletes.setObjectName(u"ctl_deletes")
        self.ctl_deletes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.ctl_deletes)

        self.ctl_downloads = QPushButton(self.layoutWidget1)
        self.ctl_downloads.setObjectName(u"ctl_downloads")
        self.ctl_downloads.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.ctl_downloads)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(420, 420, 291, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ctl_progressBar = QProgressBar(self.horizontalLayoutWidget)
        self.ctl_progressBar.setObjectName(u"ctl_progressBar")
        self.ctl_progressBar.setValue(0)
        self.ctl_progressBar.setTextVisible(True)
        self.ctl_progressBar.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.ctl_progressBar)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 50, 71, 16))
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(360, 420, 61, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ctl_state = QLabel(self.horizontalLayoutWidget_2)
        self.ctl_state.setObjectName(u"ctl_state")
        self.ctl_state.setLayoutDirection(Qt.LeftToRight)
        self.ctl_state.setFrameShape(QFrame.NoFrame)
        self.ctl_state.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.ctl_state)

        self.ctl_musicList = QTableWidget(Form)
        if (self.ctl_musicList.columnCount() < 5):
            self.ctl_musicList.setColumnCount(5)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.ctl_musicList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ctl_musicList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ctl_musicList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ctl_musicList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ctl_musicList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.ctl_musicList.setObjectName(u"ctl_musicList")
        self.ctl_musicList.setGeometry(QRect(10, 70, 331, 311))
        self.ctl_musicList.setLineWidth(1)
        self.ctl_musicList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ctl_musicList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ctl_musicList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.ctl_musicList.setAutoScroll(True)
        self.ctl_musicList.setAlternatingRowColors(False)
        self.ctl_musicList.setRowCount(0)
        self.ctl_musicList.setColumnCount(5)
        self.ctl_musicList.horizontalHeader().setVisible(True)
        self.ctl_musicList.horizontalHeader().setCascadingSectionResizes(False)
        self.ctl_musicList.horizontalHeader().setMinimumSectionSize(25)
        self.ctl_musicList.horizontalHeader().setDefaultSectionSize(62)
        self.ctl_musicList.horizontalHeader().setHighlightSections(True)
        self.ctl_musicList.horizontalHeader().setProperty("showSortIndicator", False)
        self.ctl_musicList.horizontalHeader().setStretchLastSection(False)
        self.ctl_musicList.verticalHeader().setVisible(False)
        self.ctl_musicList.verticalHeader().setCascadingSectionResizes(False)
        self.ctl_musicList.verticalHeader().setMinimumSectionSize(26)
        self.ctl_musicList.verticalHeader().setDefaultSectionSize(26)
        self.ctl_musicList.verticalHeader().setHighlightSections(False)
        self.ctl_musicList.verticalHeader().setProperty("showSortIndicator", False)
        self.ctl_musicList.verticalHeader().setStretchLastSection(False)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 50, 31, 16))
        self.ctl_number = QLabel(Form)
        self.ctl_number.setObjectName(u"ctl_number")
        self.ctl_number.setGeometry(QRect(305, 50, 21, 16))
        self.ctl_number.setScaledContents(False)
        self.ctl_lyric = QTextEdit(Form)
        self.ctl_lyric.setObjectName(u"ctl_lyric")
        self.ctl_lyric.setGeometry(QRect(360, 120, 351, 261))
        self.gridLayoutWidget_3 = QWidget(Form)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(360, 50, 351, 61))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 2, 2, 1, 1)

        self.ctl_time = QLabel(self.gridLayoutWidget_3)
        self.ctl_time.setObjectName(u"ctl_time")

        self.gridLayout_3.addWidget(self.ctl_time, 2, 1, 1, 1)

        self.ctl_id = QLabel(self.gridLayoutWidget_3)
        self.ctl_id.setObjectName(u"ctl_id")

        self.gridLayout_3.addWidget(self.ctl_id, 2, 3, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.ctl_artists = QLabel(self.gridLayoutWidget_3)
        self.ctl_artists.setObjectName(u"ctl_artists")

        self.gridLayout_3.addWidget(self.ctl_artists, 1, 1, 1, 3)

        self.ctl_music = QLabel(self.gridLayoutWidget_3)
        self.ctl_music.setObjectName(u"ctl_music")

        self.gridLayout_3.addWidget(self.ctl_music, 0, 1, 1, 3)

        self.horizontalLayoutWidget_4 = QWidget(Form)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(360, 390, 351, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ctl_path = QLineEdit(self.horizontalLayoutWidget_4)
        self.ctl_path.setObjectName(u"ctl_path")
        self.ctl_path.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.ctl_path)

        self.ctl_setPath = QPushButton(self.horizontalLayoutWidget_4)
        self.ctl_setPath.setObjectName(u"ctl_setPath")

        self.horizontalLayout_6.addWidget(self.ctl_setPath)

        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 390, 331, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.ctl_maxNumber = QSpinBox(self.horizontalLayoutWidget_3)
        self.ctl_maxNumber.setObjectName(u"ctl_maxNumber")
        self.ctl_maxNumber.setMinimum(1)
        self.ctl_maxNumber.setMaximum(10)
        self.ctl_maxNumber.setValue(5)

        self.horizontalLayout_2.addWidget(self.ctl_maxNumber)

        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_2.setStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(accessibility)
        Form.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.ctl_option.setItemText(0, QCoreApplication.translate("Form", u"\u8f93\u5165\u7f51\u5740", None))
        self.ctl_option.setItemText(1, QCoreApplication.translate("Form", u"\u97f3\u4e50ID", None))
        self.ctl_option.setItemText(2, QCoreApplication.translate("Form", u"\u5217\u8868ID", None))

        self.ctl_option.setPlaceholderText("")
        self.ctl_get.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6/\u7c98\u8d34", None))
        self.ctl_more.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.ctl_deselectAll.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88\u5168\u9009", None))
        self.ctl_selectAll.setText(QCoreApplication.translate("Form", u"\u5168\u9009", None))
        self.ctl_deletes.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.ctl_downloads.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"|\u5df2\u83b7\u53d6\u5185\u5bb9|", None))
        self.ctl_state.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u5185\u5bb9", None))
        ___qtablewidgetitem = self.ctl_musicList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u97f3\u4e50", None));
        ___qtablewidgetitem1 = self.ctl_musicList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005", None));
        ___qtablewidgetitem2 = self.ctl_musicList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u65f6\u957f", None));
        ___qtablewidgetitem3 = self.ctl_musicList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u6b4c\u8bcd", None));
        ___qtablewidgetitem4 = self.ctl_musicList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570\u91cf\uff1a", None))
        self.ctl_number.setText(QCoreApplication.translate("Form", u"0", None))
        self.ctl_lyric.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u65f6\u957f\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u97f3\u4e50ID:", None))
        self.ctl_time.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.ctl_id.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u97f3\u4e50\uff1a", None))
        self.ctl_artists.setText(QCoreApplication.translate("Form", u"\u65e0", None))
        self.ctl_music.setText(QCoreApplication.translate("Form", u"\u65e0", None))
        self.ctl_path.setText(QCoreApplication.translate("Form", u"C:/", None))
        self.ctl_setPath.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u8def\u5f84", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u540c\u65f6\u4e0b\u8f7d", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u53d6\u51b3\u4e8e\u7535\u8111\u6027\u80fd|\u82e5\u51fa\u73b0\u5d29\u6e83\u8bf7\u8c03\u5c0f\u53c2\u6570", None))
    # retranslateUi

# Error: untitled.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.


# while executing 'c:\users\27114\appdata\local\programs\python\python39\lib\site-packages\PySide2\uic -g python untitled.ui'

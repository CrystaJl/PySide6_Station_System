# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '(2)KeypadWindowKTbJck.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Keypad_window(object):
    def setupUi(self, Keypad_window):
        if not Keypad_window.objectName():
            Keypad_window.setObjectName(u"Keypad_window")
        Keypad_window.resize(300, 390)
        Keypad_window.setStyleSheet(u"border: 1px Solid black")
        self.title_text_label = QLabel(Keypad_window)
        self.title_text_label.setObjectName(u"title_text_label")
        self.title_text_label.setGeometry(QRect(0, 0, 300, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.title_text_label.setFont(font)
        self.title_text_label.setAlignment(Qt.AlignCenter)
        self.text_to_aply_label = QLabel(Keypad_window)
        self.text_to_aply_label.setObjectName(u"text_to_aply_label")
        self.text_to_aply_label.setGeometry(QRect(10, 50, 280, 50))
        self.text_to_aply_label.setFont(font)
        self.text_to_aply_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.number_7_pushButton = QPushButton(Keypad_window)
        self.number_7_pushButton.setObjectName(u"number_7_pushButton")
        self.number_7_pushButton.setGeometry(QRect(10, 110, 60, 60))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.number_7_pushButton.setFont(font1)
        self.number_8_pushButton = QPushButton(Keypad_window)
        self.number_8_pushButton.setObjectName(u"number_8_pushButton")
        self.number_8_pushButton.setGeometry(QRect(83, 110, 60, 60))
        self.number_8_pushButton.setFont(font1)
        self.number_9_pushButton = QPushButton(Keypad_window)
        self.number_9_pushButton.setObjectName(u"number_9_pushButton")
        self.number_9_pushButton.setGeometry(QRect(156, 110, 60, 60))
        self.number_9_pushButton.setFont(font1)
        self.number_4_pushButton = QPushButton(Keypad_window)
        self.number_4_pushButton.setObjectName(u"number_4_pushButton")
        self.number_4_pushButton.setGeometry(QRect(10, 180, 60, 60))
        self.number_4_pushButton.setFont(font1)
        self.clear_all_pushButton = QPushButton(Keypad_window)
        self.clear_all_pushButton.setObjectName(u"clear_all_pushButton")
        self.clear_all_pushButton.setGeometry(QRect(230, 110, 60, 60))
        self.clear_all_pushButton.setFont(font1)
        self.number_5_pushButton = QPushButton(Keypad_window)
        self.number_5_pushButton.setObjectName(u"number_5_pushButton")
        self.number_5_pushButton.setGeometry(QRect(83, 180, 60, 60))
        self.number_5_pushButton.setFont(font1)
        self.delete_previous_pushButton = QPushButton(Keypad_window)
        self.delete_previous_pushButton.setObjectName(u"delete_previous_pushButton")
        self.delete_previous_pushButton.setGeometry(QRect(230, 180, 60, 60))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.delete_previous_pushButton.setFont(font2)
        self.number_6_pushButton = QPushButton(Keypad_window)
        self.number_6_pushButton.setObjectName(u"number_6_pushButton")
        self.number_6_pushButton.setGeometry(QRect(156, 180, 60, 60))
        self.number_6_pushButton.setFont(font1)
        self.number_1_pushButton = QPushButton(Keypad_window)
        self.number_1_pushButton.setObjectName(u"number_1_pushButton")
        self.number_1_pushButton.setGeometry(QRect(10, 250, 60, 60))
        self.number_1_pushButton.setFont(font1)
        self.number_2_pushButton = QPushButton(Keypad_window)
        self.number_2_pushButton.setObjectName(u"number_2_pushButton")
        self.number_2_pushButton.setGeometry(QRect(83, 250, 60, 60))
        self.number_2_pushButton.setFont(font1)
        self.number_3_pushButton = QPushButton(Keypad_window)
        self.number_3_pushButton.setObjectName(u"number_3_pushButton")
        self.number_3_pushButton.setGeometry(QRect(156, 250, 60, 60))
        self.number_3_pushButton.setFont(font1)
        self.reject_pushButton = QPushButton(Keypad_window)
        self.reject_pushButton.setObjectName(u"reject_pushButton")
        self.reject_pushButton.setGeometry(QRect(230, 250, 60, 60))
        self.reject_pushButton.setFont(font2)
        self.set_comma_pushButton = QPushButton(Keypad_window)
        self.set_comma_pushButton.setObjectName(u"set_comma_pushButton")
        self.set_comma_pushButton.setGeometry(QRect(10, 320, 60, 60))
        self.set_comma_pushButton.setFont(font1)
        self.number_0_pushButton = QPushButton(Keypad_window)
        self.number_0_pushButton.setObjectName(u"number_0_pushButton")
        self.number_0_pushButton.setGeometry(QRect(83, 320, 60, 60))
        self.number_0_pushButton.setFont(font1)
        self.accept_pushButton = QPushButton(Keypad_window)
        self.accept_pushButton.setObjectName(u"accept_pushButton")
        self.accept_pushButton.setGeometry(QRect(156, 320, 134, 61))
        self.accept_pushButton.setFont(font1)

        self.retranslateUi(Keypad_window)
        self.reject_pushButton.clicked.connect(Keypad_window.close)

        QMetaObject.connectSlotsByName(Keypad_window)
    # setupUi

    def retranslateUi(self, Keypad_window):
        Keypad_window.setWindowTitle(QCoreApplication.translate("Keypad_window", u"Form", None))
        self.title_text_label.setText(QCoreApplication.translate("Keypad_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.text_to_aply_label.setText("")
        self.number_7_pushButton.setText(QCoreApplication.translate("Keypad_window", u"7", None))
        self.number_8_pushButton.setText(QCoreApplication.translate("Keypad_window", u"8", None))
        self.number_9_pushButton.setText(QCoreApplication.translate("Keypad_window", u"9", None))
        self.number_4_pushButton.setText(QCoreApplication.translate("Keypad_window", u"4", None))
        self.clear_all_pushButton.setText(QCoreApplication.translate("Keypad_window", u"C", None))
        self.number_5_pushButton.setText(QCoreApplication.translate("Keypad_window", u"5", None))
        self.delete_previous_pushButton.setText(QCoreApplication.translate("Keypad_window", u"<", None))
        self.number_6_pushButton.setText(QCoreApplication.translate("Keypad_window", u"6", None))
        self.number_1_pushButton.setText(QCoreApplication.translate("Keypad_window", u"1", None))
        self.number_2_pushButton.setText(QCoreApplication.translate("Keypad_window", u"2", None))
        self.number_3_pushButton.setText(QCoreApplication.translate("Keypad_window", u"3", None))
        self.reject_pushButton.setText(QCoreApplication.translate("Keypad_window", u"ESC", None))
        self.set_comma_pushButton.setText(QCoreApplication.translate("Keypad_window", u",", None))
        self.number_0_pushButton.setText(QCoreApplication.translate("Keypad_window", u"0", None))
        self.accept_pushButton.setText(QCoreApplication.translate("Keypad_window", u"Enter", None))
    # retranslateUi


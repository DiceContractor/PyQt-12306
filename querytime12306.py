# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'querytime12306.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(808, 591)
        self.graph = QWidget(Form)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(0, 160, 811, 431))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 331, 16))
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 30, 771, 131))
        self.tab_tui = QWidget()
        self.tab_tui.setObjectName(u"tab_tui")
        self.gridLayout_2 = QGridLayout(self.tab_tui)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.price_edit = QLineEdit(self.tab_tui)
        self.price_edit.setObjectName(u"price_edit")
        self.price_edit.setEnabled(True)
        self.price_edit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.price_edit, 1, 2, 1, 1)

        self.label_7 = QLabel(self.tab_tui)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)

        self.gridLayout_2.addWidget(self.label_7, 1, 3, 1, 1)

        self.query_button_tui = QPushButton(self.tab_tui)
        self.query_button_tui.setObjectName(u"query_button_tui")
        self.query_button_tui.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.query_button_tui, 2, 4, 1, 1)

        self.depart_time_edit = QDateTimeEdit(self.tab_tui)
        self.depart_time_edit.setObjectName(u"depart_time_edit")
        self.depart_time_edit.setEnabled(True)

        self.gridLayout_2.addWidget(self.depart_time_edit, 1, 4, 1, 1)

        self.label_8 = QLabel(self.tab_tui)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.changed_or_not_edit = QCheckBox(self.tab_tui)
        self.changed_or_not_edit.setObjectName(u"changed_or_not_edit")
        self.changed_or_not_edit.setEnabled(True)

        self.gridLayout_2.addWidget(self.changed_or_not_edit, 0, 0, 1, 1)

        self.hint_edit_2 = QTextEdit(self.tab_tui)
        self.hint_edit_2.setObjectName(u"hint_edit_2")
        self.hint_edit_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.hint_edit_2, 0, 5, 3, 1)

        self.tabWidget.addTab(self.tab_tui, "")
        self.tab_gai = QWidget()
        self.tab_gai.setObjectName(u"tab_gai")
        self.gridLayout = QGridLayout(self.tab_gai)
        self.gridLayout.setObjectName(u"gridLayout")
        self.depart_time_edit_new = QDateTimeEdit(self.tab_gai)
        self.depart_time_edit_new.setObjectName(u"depart_time_edit_new")

        self.gridLayout.addWidget(self.depart_time_edit_new, 1, 3, 1, 1)

        self.label_3 = QLabel(self.tab_gai)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.query_button_gai = QPushButton(self.tab_gai)
        self.query_button_gai.setObjectName(u"query_button_gai")
        self.query_button_gai.setMinimumSize(QSize(0, 0))
        self.query_button_gai.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.query_button_gai, 2, 3, 1, 1)

        self.label_5 = QLabel(self.tab_gai)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.price_edit_new = QLineEdit(self.tab_gai)
        self.price_edit_new.setObjectName(u"price_edit_new")
        self.price_edit_new.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.price_edit_new, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab_gai)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.depart_time_edit_old = QDateTimeEdit(self.tab_gai)
        self.depart_time_edit_old.setObjectName(u"depart_time_edit_old")
        self.depart_time_edit_old.setCurrentSection(QDateTimeEdit.Section.YearSection)

        self.gridLayout.addWidget(self.depart_time_edit_old, 0, 3, 1, 1)

        self.price_edit_old = QLineEdit(self.tab_gai)
        self.price_edit_old.setObjectName(u"price_edit_old")
        self.price_edit_old.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.price_edit_old, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab_gai)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.hint_edit = QTextEdit(self.tab_gai)
        self.hint_edit.setObjectName(u"hint_edit")
        self.hint_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.hint_edit, 0, 4, 3, 1)

        self.tabWidget.addTab(self.tab_gai, "")
        self.rule_button = QPushButton(Form)
        self.rule_button.setObjectName(u"rule_button")
        self.rule_button.setGeometry(QRect(590, 10, 201, 24))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"12306\u9000\u6539\u8d39\u8d70\u52bf\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6ce8\uff1a\u4ec5\u9650\u4e8e12306\u5b98\u7f51\u8d2d\u4e70\u7684\u8f66\u7968\uff0c\u5176\u4ed6\u6e20\u9053\u8bf7\u53c2\u7167\u76f8\u5e94\u89c4\u5219\u3002", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u53d1\u8f66\u65f6\u95f4\uff1a", None))
        self.query_button_tui.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u9000\u7968\u8d39", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7968\u9762\u4ef7\u683c\uff1a", None))
        self.changed_or_not_edit.setText(QCoreApplication.translate("Form", u"\u66fe\u6539\u7b7e\u8fc7", None))
        self.hint_edit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.hint_edit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u3010\u9000\u7968\u8d39\u3011\uff1a\u968f\u65f6\u95f4\u4e34\u8fd1\u53d1\u8f66\uff0c\u9000\u7968\u8d39\u5347\u9ad8\uff1b \u6ce8\uff1a\u66fe\u6539\u7b7e\u5230\u6625\u8fd0\u671f\u95f4\u7684\u8f66\u7968\uff0c\u518d\u9000\u7968\u65f6\u6309\u6700\u9ad8\u6bd4\u4f8b20%\u8ba1\u7b97\u9000\u7968\u8d39\u3002", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tui), QCoreApplication.translate("Form", u"\u9000\u7968", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u539f\u53d1\u8f66\u65f6\u95f4\uff1a", None))
        self.query_button_gai.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u6539\u7b7e\u8d39+\u5dee\u989d\u9000\u7968\u8d39", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u65b0\u53d1\u8f66\u65f6\u95f4\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u539f\u7968\u4ef7\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u65b0\u7968\u4ef7\uff1a", None))
        self.hint_edit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.hint_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u3010\u6539\u7b7e\u8d39\u3011\uff1a\u6539\u7b7e\u5230\u9694\u65e5\u6216\u66f4\u665a\u7684\u8f66\u7968\uff0c\u9700\u8981\u6539\u7b7e\u8d39\uff1b \u3010\u5dee\u989d\u9000\u7968\u8d39\u3011\uff1a\u6539\u7b7e\u66f4\u4fbf\u5b9c\u7684\u8f66\u7968\uff0c\u8fd4\u8fd8\u5dee\u989d\u90e8\u5206\u65f6\u6309\u9000\u7968\u89c4\u5219\u6536\u53d6\u9000\u7968\u8d39\u3002 ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gai), QCoreApplication.translate("Form", u"\u6539\u7b7e", None))
        self.rule_button.setText(QCoreApplication.translate("Form", u"\u67e5\u770b12306\u9000\u6539\u8d39\u89c4\u5219", None))
    # retranslateUi


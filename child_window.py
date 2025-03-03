# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'child_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_once_changed_info(object):
    def setupUi(self, once_changed_info):
        if not once_changed_info.objectName():
            once_changed_info.setObjectName(u"once_changed_info")
        once_changed_info.resize(243, 146)
        self.gridLayout = QGridLayout(once_changed_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.change_time_edit = QDateTimeEdit(once_changed_info)
        self.change_time_edit.setObjectName(u"change_time_edit")

        self.gridLayout.addWidget(self.change_time_edit, 0, 1, 1, 1)

        self.original_time_edit = QDateTimeEdit(once_changed_info)
        self.original_time_edit.setObjectName(u"original_time_edit")

        self.gridLayout.addWidget(self.original_time_edit, 1, 1, 1, 1)

        self.label = QLabel(once_changed_info)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(once_changed_info)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.yes_button = QPushButton(once_changed_info)
        self.yes_button.setObjectName(u"yes_button")

        self.gridLayout.addWidget(self.yes_button, 2, 1, 1, 1)


        self.retranslateUi(once_changed_info)

        QMetaObject.connectSlotsByName(once_changed_info)
    # setupUi

    def retranslateUi(self, once_changed_info):
        once_changed_info.setWindowTitle(QCoreApplication.translate("once_changed_info", u"\u6539\u7b7e\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("once_changed_info", u"\u6539\u7b7e\u64cd\u4f5c\u65f6\u95f4\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("once_changed_info", u"\u539f\u8f66\u7968\u53d1\u8f66\u65f6\u95f4\uff1a", None))
        self.yes_button.setText(QCoreApplication.translate("once_changed_info", u"\u786e\u5b9a", None))
    # retranslateUi


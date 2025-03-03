import sys
from datetime import datetime, timedelta

from PySide6.QtCore import QTime, QDateTime, QDate, QUrl
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMessageBox, QDialog
from PySide6.QtGui import QIcon, QDesktopServices

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
from matplotlib.collections import PathCollection  # 用于处理路径集
from matplotlib.backend_bases import PickEvent  # 用于处理事件

from querytime12306 import Ui_Form as MyUi
from child_window import Ui_once_changed_info as ChildUi


class MyChild(QDialog, ChildUi):
    def __init__(self):
        super().__init__()
        self.setupUi(once_changed_info=self)
        self.setFixedSize(243, 146)
        self.change_time_edit.setDate(QDate.currentDate())
        self.original_time_edit.setDate(QDate.currentDate())

        self.yes_button.clicked.connect(self.close)


class MyWidget(QWidget, MyUi):

    def __init__(self):
        super().__init__()
        self.setupUi(Form=self)
        self.setFixedSize(808, 591)
        self.depart_time_edit.setDate(QDate.currentDate())
        self.depart_time_edit_new.setDate(QDate.currentDate())
        self.depart_time_edit_old.setDate(QDate.currentDate())
        # self.price_edit.setValidator(QDoubleValidator)
        self.cw = MyChild()

        self.canvas = FigureCanvasQTAgg()
        self.graph.setLayout(QVBoxLayout())
        self.graph.layout().addWidget(self.canvas)

        self.query_button_tui.clicked.connect(self.ticket_return)
        self.query_button_gai.clicked.connect(self.ticket_change)
        self.rule_button.clicked.connect(self.open_12306)
        self.changed_or_not_edit.clicked.connect(self.open_child)

    def open_child(self):
        if self.changed_or_not_edit.isChecked():
            self.cw.show()
            self.cw.exec()

    def open_12306(self):
        QDesktopServices.openUrl(QUrl('https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/orderWarmTips.html'))

    def ticket_change(self):
        # 清空提示和图表
        self.canvas.figure.clear()
        self.canvas.draw()
        self.hint_edit.clear()

        # 检查输入合法性：
        if self.depart_time_edit_new.dateTime().toPython() < datetime.now():
            QMessageBox.about(self, '输入错误', '改签新票的开车时间已过，请检查输入')
            return
        elif self.depart_time_edit_old.date() < QDate.currentDate():
            QMessageBox.about(self, '输入错误', '已超过所购票发车当日，不可办理改签')
            return

        elif not (self.price_edit_old.text().isnumeric() and eval(self.price_edit_old.text()) > 0):
            QMessageBox.about(self, '输入错误', '请正确输入改签前原票价')
            return
        elif not (self.price_edit_new.text().isnumeric() and eval(self.price_edit_new.text()) > 0):
            QMessageBox.about(self, '输入错误', '请正确输入改签后新票价')
            return

        # 如果输入全都合法，准备输入的变量
        depart_new = self.depart_time_edit_new.dateTime().toPython()
        time0 = datetime.now()
        depart_old = self.depart_time_edit_old.dateTime().toPython()
        depart_old_day_off = (depart_old + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        time6 = (depart_old - timedelta(days=6)).replace(hour=0, minute=0, second=0)
        time2 = depart_old - timedelta(days=2)
        time1 = depart_old - timedelta(days=1)
        x=[]

        # 改签费-----------------------------------------------------------------------------------
        if self.depart_time_edit_new.date().addDays(-14) == QDate.currentDate():
            self.hint_edit.append('改签的新票今日开售，请关注12306开售时间')
        elif self.depart_time_edit_new.date().addDays(-14) > QDate.currentDate():
            depart_new_open = self.depart_time_edit_new.date().addDays(-14)
            m, d = depart_new_open.month(), depart_new_open.day()
            self.hint_edit.append('改签的新票将在{}月{}日开售，请在12306关注开售时间'.format(m, d))

        earlier=False
        if self.depart_time_edit_new.date() <= self.depart_time_edit_old.date():
            self.hint_edit.append('改签原车票开车当日或更早的车票，无改签费')
            earlier = True
        else:  # 改签更晚的车票，根据 改签操作时间（现在）距离原开车时间 计算改签费比例
            ax = self.canvas.figure.add_subplot()  # ax=子图
            font_l = FontProperties(fname="Dengl.ttf")  # 字体
            font_n = FontProperties(fname="Deng.ttf")
            font_b = FontProperties(fname="Dengb.ttf")

            x = [time0, time2, time1, depart_old, depart_old_day_off]

            price_min = min(eval(self.price_edit_new.text()), eval(self.price_edit_old.text()))
            y1 = [0, 0.05 * price_min, 0.15 * price_min, 0.4 * price_min]

            if time0 >= depart_old:
                ax.plot([time0, depart_old_day_off], [y1[3]] * 2, c='g', linestyle='--', label='改签费')
            else:
                ax.plot([depart_old, depart_old_day_off], [y1[3]] * 2, c='g', linestyle='--', label='改签费')
                ax.plot([depart_old] * 2, [y1[2], y1[3]], c='g', linestyle='--')
                if time0 >= time1:
                    ax.plot([time0, depart_old], [y1[2]] * 2, c='g', linestyle='--')
                else:
                    ax.plot([time1, depart_old], [y1[2]] * 2, c='g', linestyle='--')
                    ax.plot([time1] * 2, [y1[1], y1[2]], c='g', linestyle='--')
                    if time0 >= time2:
                        ax.plot([time0, time1], [y1[1]] * 2, c='g', linestyle='--')
                    else:
                        ax.plot([time2, time1], [y1[1]] * 2, c='g', linestyle='--')
                        ax.plot([time2] * 2, [0, y1[1]], c='g', linestyle='--')
                        ax.plot([time0, time2], [0, 0], c='g', linestyle='--')

        # 差价多退少补---------------------------------------------------------------------------------------
        price_new = eval(self.price_edit_new.text())
        price_old = eval(self.price_edit_old.text())

        if price_new > price_old:
            self.hint_edit.append('改签车票价格更高，需补差价{}元\n'.format(price_new - price_old))
        else:  # 差额退票费随 距离原开车时间 变化
            pr = price_old - price_new
            x = [time0, time6, time2, time1, depart_old, depart_old_day_off]
            y = [0, 0.05 * pr, 0.1 * pr, 0.2 * pr]

            if earlier:
                ax = self.canvas.figure.add_subplot()  # ax=子图
                font_l = FontProperties(fname="Dengl.ttf")  # 字体
                font_n = FontProperties(fname="Deng.ttf")
                font_b = FontProperties(fname="Dengb.ttf")

                ax.scatter(depart_new,0,s=25,c='r')
                ax.text(depart_new,0,'新改签发车时间',ha='left',va='bottom',fontsize=8,fontproperties=font_l)
                ax.axvline(x=depart_new,c='grey')


            ax.scatter([depart_old_day_off], [y[3]], s=25, c='r')
            if not earlier:
                ax.text(depart_old_day_off, y[3], '发车当日24::00后\n不可再改签', ha='left', va='bottom', fontsize=8,
                    fontproperties=font_l)
            else:
                ax.text(depart_old_day_off, y[3], '发车当日\n24::00', ha='left', va='bottom', fontsize=8,
                        fontproperties=font_l)

            if time0 <= depart_old:
                ax.scatter([depart_old], [y[3]], s=25, c='r')
                ax.text(depart_old, y[3], '原票\n发车时间', ha='left', va='bottom', fontsize=8, fontproperties=font_l)
            if time0 >= time1:
                ax.plot([time0, depart_old_day_off], [y[3]] * 2, c='#1f77b4', label='差额退票费')
            else:
                ax.plot([time1] * 2, y[2:4], c='r')
                ax.plot([time1, depart_old_day_off], [y[3]] * 2, c='#1f77b4', label='差额退票费')
                ax.scatter([time1], [y[3] - 0.3], marker='^', s=25, c='r')
                ax.text(time1, y[3], '￥' + str(pr * 0.2), ha='left', va='bottom', fontsize=8, fontproperties=font_l)
                if time0 >= time2:
                    ax.plot([time0, time1], [y[2]] * 2, c='#1f77b4')
                else:
                    ax.plot([time2] * 2, y[1:3], c='r')
                    ax.plot([time2, time1], [y[2]] * 2, c='#1f77b4')
                    ax.scatter([time2], [y[2] - 0.3], marker='^', s=25, c='r')
                    ax.text(time2, y[2], '￥' + str(pr * 0.1), ha='left', va='bottom', fontsize=8,
                            fontproperties=font_l)
                    if time0 >= time6:
                        ax.plot([time0, time2], [y[1]] * 2, c='#1f77b4')
                    else:
                        ax.plot([time6] * 2, y[0:2], c='r')
                        ax.plot([time6, time2], [y[1]] * 2, c='#1f77b4')
                        ax.scatter([time6], [y[1] - 0.3], marker='^', s=25, c='r')
                        ax.text(time6, y[1], '￥' + str(pr * 0.05), ha='left', va='bottom', fontsize=8,
                                fontproperties=font_l)

                        ax.plot([time0, time6], [0, 0], c='#1f77b4')

        if x != []:  # 如果画了任意一条曲线，调整坐标轴 并draw()
            ax.spines['top'].set_color('none')
            ax.spines['right'].set_color('none')
            # ax.spines['bottom'].set_position(('data',0))
            # ax.spines['left'].set_position(('data',time0))
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%H:%M'))
            # self.canvas.figure.autofmt_xdate(rotation=45)  # 旋转45度
            if earlier:
                x.append(depart_new)
            ax.set_xticks([i for i in x if i > time0])
            labels = ax.get_xticklabels()
            ax.set_xticklabels(labels, fontsize=8)

            ax.legend(prop=font_l)
            # ax.set_xlabel('时间', fontproperties=font_l)
            ax.set_ylabel('单位：(元)', fontproperties=font_l)
            # ax.set_title("差额退票费、改签费随时间变化", fontproperties=font_n)
            ax.grid(True)

        self.canvas.figure.tight_layout()
        self.canvas.draw()

    def ticket_return(self):
        self.canvas.figure.clear()
        self.canvas.draw()
        self.hint_edit_2.clear()

        if not (self.price_edit.text().isnumeric() and eval(self.price_edit.text()) > 0):
            QMessageBox.about(self, '输入错误', '请正确输入原票价')
            return
        elif self.depart_time_edit.dateTime().toPython() < datetime.now():
            QMessageBox.about(self, '输入错误', '开车时间已过，请检查输入')
            return

        price = eval(self.price_edit.text())
        depart_datetime = self.depart_time_edit.dateTime().toPython()
        time0 = datetime.now()
        time1 = (depart_datetime - timedelta(days=6)).replace(hour=0, minute=0, second=0)
        time2 = depart_datetime - timedelta(days=2)
        time3 = depart_datetime - timedelta(days=1)

        scape, spring = False, False
        if self.changed_or_not_edit.isChecked():
            cha = self.cw.change_time_edit.dateTime().toPython()
            ori = self.cw.original_time_edit.dateTime().toPython()

            scape = True if (ori - timedelta(days=6)).replace(hour=0, minute=0,second=0) < cha and time1 > cha else False
            spring = True if (datetime(year=2025, month=2, day=22, hour=23, minute=59, second=59) > depart_datetime >
                              datetime(year=2025, month=1, day=14)) else False

        ax = self.canvas.figure.add_subplot()  # ax=子图
        font_l = FontProperties(fname="Dengl.ttf")  # 字体
        font_n = FontProperties(fname="Deng.ttf")
        font_b = FontProperties(fname="Dengb.ttf")

        x = [time0, time1, time1, time2, time2, time3, time3, depart_datetime] if not spring else [time0,
                                                                                                   depart_datetime]
        y = [0, 0, 0.05 * price, 0.05 * price, 0.1 * price, 0.1 * price, 0.2 * price, 0.2 * price] if not spring else [
            0.2 * price, 0.2 * price]
        if not spring and scape:
            y[0], y[1] = 0.05 * price, 0.05 * price

        ax.scatter([depart_datetime], [0.2 * price], s=25, c='r')
        ax.text(depart_datetime, 0.2 * price, '发车', ha='left', va='bottom', fontsize=8, fontproperties=font_l)

        if spring:
            ax.plot(x, y, label='退票费', picker=True)
        else:
            if time0 >= time3:
                ax.plot([time0, depart_datetime], y[6:8], c='#1f77b4', label='退票费', picker=True)
            else:
                ax.plot(x[5:7], y[5:7], c='r')
                ax.plot(x[6:8], y[6:8], c='#1f77b4', label='退票费', picker=True)
                ax.scatter([time3], [0.2 * price], marker='^', s=25, c='r')
                ax.text(time3, 0.2 * price, '￥' + str(price * 0.2), ha='left', va='bottom',
                        fontsize=8, fontproperties=font_l)
                if time0 >= time2:
                    ax.plot([time0, time3], y[4:6], c='#1f77b4')
                else:
                    ax.plot(x[3:5], y[3:5], c='r')
                    ax.plot(x[4:6], y[4:6], c='#1f77b4')
                    ax.scatter([time2], [0.1 * price], marker='^', s=25, c='r')
                    ax.text(time2, 0.1 * price, '￥' + str(price * 0.1), ha='left', va='bottom',
                            fontsize=8, fontproperties=font_l)
                    if time0 >= time1:
                        ax.plot([time0, time2], y[2:4], c='#1f77b4')
                    else:
                        ax.plot(x[1:3], y[1:3], c='r')
                        ax.plot(x[2:4], y[2:4], c='#1f77b4')
                        ax.scatter([time1], [0.05 * price], marker='^', s=25, c='r')
                        ax.text(time1, 0.05 * price, '￥' + str(price * 0.05), ha='left', va='bottom',
                                fontsize=8, fontproperties=font_l)
                        if scape:
                            self.hint_edit_2.append('距票面乘车站开车前不足8天的车票，改签至开车前8天以上的列车，又在距开车前8天以上退票的，核收5%的退票费。')
                        ax.plot(x[0:2], y[0:2], c='#1f77b4')

        # 坐标轴
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        # ax.spines['bottom'].set_position(('data',0))
        # ax.spines['left'].set_position(('data',time0))
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        # ax.set_ylim((-1, 24))
        ax.set_xticks([i for i in x if i > time0])
        labels=ax.get_xticklabels()
        ax.set_xticklabels(labels,fontsize=8)

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%H:%M'))
        # self.canvas.figure.autofmt_xdate(rotation=45)  # 旋转45度

        ax.legend(prop=font_l)
        # ax.set_xlabel('时间', fontproperties=font_l)
        ax.set_ylabel('退票费（元）', fontproperties=font_l)
        # ax.set_title("退票费随时间变化", fontproperties=font_n)
        ax.grid(True)

        self.canvas.figure.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon('tickets.png'))
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())

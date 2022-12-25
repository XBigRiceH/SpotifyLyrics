from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Variables
import ui.raw
from . import LyricsScroller


class LyricsWindowView(QWidget, ui.raw.LyricsDisplay.Ui_LyricsDisplay):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.installEventFilter(self)
        self.visible = True

        # windows flags/attributes
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # stays on top
        self.update_always_on_top()

        # add lyrics display widgets
        self.lyrics_widgets_up = LyricsScroller.LyricsScroller(self.Lyrics)
        self.LyricsMain.addWidget(self.lyrics_widgets_up)
        self.lyrics_widgets_down = LyricsScroller.LyricsScroller(self.Lyrics2)
        self.LyricsMain2.addWidget(self.lyrics_widgets_down)

        # set font color
        stylesheet = f"color:rgb({Variables.font_color[0]}, {Variables.font_color[1]}, {Variables.font_color[2]})"
        self.lyrics_widgets_up.set_label_stylesheet(stylesheet)
        self.lyrics_widgets_down.set_label_stylesheet(stylesheet)

        # set font size
        family = Variables.font_family
        self.font = QtGui.QFont()
        self.font.setFamily(family)
        self.font.setPixelSize(int((self.height() - 60) / 3))
        self.lyrics_widgets_up.set_font(self.font)
        self.lyrics_widgets_down.set_font(self.font)

        # set font outline
        self.effect = QtWidgets.QGraphicsDropShadowEffect(self.lyrics_widgets_down.lyrics_label)
        self.effect.setBlurRadius(5)
        self.effect.setColor(
            QColor(int(Variables.font_blur_color[0]), int(Variables.font_blur_color[1]),
                   int(Variables.font_blur_color[2])))
        self.effect.setOffset(0, 0)
        self.lyrics_widgets_down.lyrics_label.setGraphicsEffect(self.effect)

        self.effect2 = QtWidgets.QGraphicsDropShadowEffect(self.lyrics_widgets_up.lyrics_label)
        self.effect2.setBlurRadius(5)
        self.effect2.setColor(
            QColor(int(Variables.font_blur_color[0]), int(Variables.font_blur_color[1]),
                   int(Variables.font_blur_color[2])))
        self.effect2.setOffset(0, 0)
        self.lyrics_widgets_up.lyrics_label.setGraphicsEffect(self.effect2)

        self.effect3 = QtWidgets.QGraphicsDropShadowEffect(self.lyrics_widgets_up.lyrics_label)
        self.effect3.setBlurRadius(0)
        self.effect3.setColor(QColor(50, 50, 50))
        self.effect3.setOffset(0, 0)
        self.PlayStatus.setGraphicsEffect(self.effect3)

        # resize / drag evt initialization
        self.x_index = -1
        self.y_index = -1
        self.clicked = False
        self._drag_cursor = []
        self.move_distance = 0
        self.init_drag_details()

        # mouse tracking
        self.setMouseTracking(True)
        self.Back.setMouseTracking(True)
        self.Lyrics.setMouseTracking(True)
        self.Lyrics2.setMouseTracking(True)
        self.lyrics_widgets_up.set_mouse_track()
        self.lyrics_widgets_down.set_mouse_track()
        self.ButtonsNav.setMouseTracking(True)

        # signal connection
        self.locked = False
        self.init_signals()

    def update_always_on_top(self):
        if not self.isHidden():
            self.hide()
            if Variables.always_top:
                self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()
        else:
            if Variables.always_top:
                self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)

    def init_signals(self):
        self.locked = False

    def init_drag_details(self):
        self.clicked = False
        self.x_index = self.y_index = -1
        self._drag_cursor = [
            (Qt.SizeFDiagCursor, Qt.SizeVerCursor, Qt.SizeBDiagCursor),
            (Qt.SizeHorCursor, Qt.SizeAllCursor, Qt.SizeHorCursor),
            (Qt.SizeBDiagCursor, Qt.SizeVerCursor, Qt.SizeFDiagCursor)
        ]
        self.move_distance = 0

    def set_font_family(self, new_font):
        self.font.setFamily(new_font)
        self.lyrics_widgets_up.set_font(self.font)
        self.lyrics_widgets_down.set_font(self.font)

    def set_font_size(self, size, resize_window=False):
        self.font.setPixelSize(size)
        self.lyrics_widgets_up.set_font(self.font)
        self.lyrics_widgets_down.set_font(self.font)
        if resize_window:
            height = int(size * 3 + 30)
            self.resize(self.width(), height)

    def set_cursor_icon(self, cursor):
        self.ButtonsNav.setCursor(cursor)
        self.lyrics_widgets_up.setCursor(cursor)
        self.lyrics_widgets_down.setCursor(cursor)

    def set_pause_button_icon(self, playing):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f":/icon/icon/{'play' if not playing else 'pause'}.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.PlayStatusButton.setIcon(icon)
        self.PlayStatusButton.setIconSize(QtCore.QSize(25, 25))

    def set_lyrics_text(self, line, content, roll_time):
        width = QFontMetrics(self.font).width(content)
        if line == 1:
            self.lyrics_widgets_up.set_text(content, self.width(), width, roll_time)
        if line == 2:
            self.lyrics_widgets_down.set_text(content, self.width(), width, roll_time)
        self.update()

    def enterEvent(self, evt):
        if not self.locked:
            self.set_transparent(False)
            self.set_buttons_hidden_status(False)
        else:
            self.PlayStatusButton.setHidden(False)

    def leaveEvent(self, evt):
        if self.locked and Variables.show_background_when_locked:
            self.set_transparent(False)
        elif not self.locked and Variables.show_background_when_unlocked:
            self.set_transparent(False)
        else:
            self.set_transparent(True)
            self.set_buttons_hidden_status(True)
            if self.locked:
                self.PlayStatusButton.setHidden(False)

    def mouseReleaseEvent(self, evt):
        self.lyrics_widgets_up.resize_label(QFontMetrics(self.font).width(self.lyrics_widgets_up.text))
        self.lyrics_widgets_down.resize_label(QFontMetrics(self.font).width(self.lyrics_widgets_down.text))
        self.init_drag_details()
        evt.accept()

    def mousePressEvent(self, evt):
        if not self.locked and evt.button() == Qt.LeftButton:
            self.clicked = True
            self.move_distance = evt.globalPos() - self.pos()
            evt.accept()

    def close(self):
        return super().close()

    def update_pos(self, pos):
        x_list = (-10, 10, self.width() - 10, self.width() + 10)
        y_list = (-10, 10, self.height() - 10, self.height() + 10)
        x = pos.x()
        y = pos.y()
        for i in range(3):
            if x_list[i] < x:
                self.x_index = i
        for i in range(3):
            if y_list[i] < y:
                self.y_index = i

    def lockEvent(self):
        self.effect3.setBlurRadius(5)
        self.locked = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayStatusButton.setIcon(icon)
        self.PlayStatusButton.setIconSize(QtCore.QSize(25, 25))
        if Variables.show_background_when_locked:
            self.set_transparent(False)
        else:
            self.set_transparent(True)
        self.set_buttons_hidden_status(True)
        self.PlayStatusButton.setHidden(False)

    def unlockEvent(self, paused):
        self.effect3.setBlurRadius(0)
        self.locked = False
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f":/icon/icon/{'pause' if paused else 'play'}.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.PlayStatusButton.setIcon(icon)
        self.PlayStatusButton.setIconSize(QtCore.QSize(25, 25))
        self.set_buttons_hidden_status(False)
        if Variables.show_background_when_unlocked:
            self.set_transparent(False)
        else:
            self.set_transparent(True)

    def mouseMoveEvent(self, evt):
        pos = evt.pos()

        if not self.clicked:
            self.update_pos(pos)
            if self.y_index == self.x_index == 1 and self.locked:
                self.set_cursor_icon(Qt.ArrowCursor)
            if not self.locked:
                self.set_cursor_icon(self._drag_cursor[self.y_index][self.x_index])

        if self.clicked:
            if self.x_index == self.y_index == 1:
                # 拖动窗口 不改变大小
                if self.move_distance:
                    self.move(evt.globalPos() - self.move_distance)
            elif self.x_index + self.y_index >= 3:
                height = pos.y() if self.y_index == 2 else self.height()
                width_ = pos.x() if self.x_index == 2 else self.width()
                self.resize(width_, height)
            else:
                # 先设置位置 再设置大小
                if self.x_index == 0:
                    new_geometry_y = pos.y() if self.y_index == 2 else self.height()
                    if not (self.width() == self.minimumWidth() and pos.x() > 0):
                        self.setGeometry(
                            self.geometry().x() + pos.x(),
                            self.geometry().y(),
                            self.width() - pos.x(),
                            new_geometry_y)

                if self.y_index == 0:
                    new_geometry_x = pos.x() if self.x_index == 2 else self.width()
                    if not ((self.height() == self.minimumHeight() and pos.y() > 0)
                            or (self.height() == self.maximumHeight() and pos.y() < 0)):
                        self.setGeometry(
                            self.geometry().x(),
                            self.geometry().y() + pos.y(),
                            new_geometry_x,
                            self.height() - pos.y())

            self.set_font_size(int((self.height() - 60) / 3))

        evt.accept()

    def set_buttons_hidden_status(self, status):
        self.AccountButton.setHidden(status)
        self.SettingsButton.setHidden(status)
        self.PreviousButton.setHidden(status)
        self.NextButton.setHidden(status)
        self.PlayStatusButton.setHidden(status)
        self.LockButton.setHidden(status)
        self.QuitButton.setHidden(status)

    def set_transparent(self, visible):
        self.visible = visible
        self.setStyleSheet(
            "*{border:none;}" if visible else "*{border:none;}#Back{background-color: rgba(" + str(
                Variables.background_color[0]) + "," + str(Variables.background_color[1]) + "," + str(
                Variables.background_color[2]) + "," + str(Variables.background_color[3]) + ");border-radius:10px}")

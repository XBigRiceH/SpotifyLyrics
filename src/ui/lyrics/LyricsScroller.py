import math
import threading
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Variables


class LyricsScroller(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lyrics_label = QtWidgets.QLabel()
        self.lyrics_label.setObjectName("LyricsLabel")
        self.lyrics_label.setAlignment(Qt.AlignCenter)

        self.setWidget(self.lyrics_label)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('border:none;background-color:transparent;')
        self.viewport().setStyleSheet("background-color:transparent;")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.text = ""
        self._scrollbar = self.horizontalScrollBar()
        self.timer = threading.Thread(target=self.timerHandle, daemon=True)
        self.current_roll_time = None
        self.start_time = None
        self.font_width = None
        self.timer.start()

    def timerHandle(self):
        while 1:
            time.sleep(float(1.0 / Variables.monitor_refresh_rate))

            if self.font_width is None or self.start_time is None or self.current_roll_time is None:
                continue
            if self.font_width > self.width():
                percent = int(time.time_ns() / 1000000) - self.start_time
                if percent >= self.current_roll_time:
                    self._scrollbar.setValue(self._scrollbar.maximum())
                    continue

                self.lyrics_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                percent = float(percent) / float(self.current_roll_time)
                self._scrollbar.setValue(math.floor(self._scrollbar.maximum() * percent))
            else:
                self.lyrics_label.setAlignment(Qt.AlignCenter)

    def set_text(self, text, containerWidth, width, roll_time):
        if text == self.text and roll_time == self.current_roll_time:
            return
        self.current_roll_time = roll_time
        self.start_time = int(time.time_ns() / 1000000)

        self.resize(QSize(containerWidth, self.height()))
        self.lyrics_label.setText(text)
        self.text = text
        self._scrollbar.setValue(0)
        self.resize_label(width)

    def set_font(self, font):
        self.lyrics_label.setFont(font)

    def set_mouse_track(self):
        self.setMouseTracking(True)
        self.lyrics_label.setMouseTracking(True)

    def resize_label(self, new_width):
        self.setWidgetResizable(True)
        self.lyrics_label.resize(self.size())
        self.lyrics_label.setAlignment(Qt.AlignCenter)
        self.font_width = new_width

    def setCursor(self, union, cursor=None, Qt_CursorShape=None):
        self.lyrics_label.setCursor(union)
        return super().setCursor(union)

    def set_label_stylesheet(self, stylesheet):
        self.lyrics_label.setStyleSheet(stylesheet)

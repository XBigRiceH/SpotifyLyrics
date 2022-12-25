# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LyricsDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from . import icons_rc

class Ui_LyricsDisplay(object):
    def setupUi(self, LyricsDisplay):
        LyricsDisplay.setObjectName("LyricsDisplay")
        LyricsDisplay.resize(750, 200)
        LyricsDisplay.setMinimumSize(QtCore.QSize(750, 200))
        LyricsDisplay.setMaximumSize(QtCore.QSize(8192, 380))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        LyricsDisplay.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/xh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LyricsDisplay.setWindowIcon(icon)
        LyricsDisplay.setStyleSheet("*\n"
"{\n"
"border:none;\n"
"}")
        self.MainLayout = QtWidgets.QGridLayout(LyricsDisplay)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName("MainLayout")
        self.Back = QtWidgets.QFrame(LyricsDisplay)
        self.Back.setMinimumSize(QtCore.QSize(750, 200))
        self.Back.setMaximumSize(QtCore.QSize(8192, 380))
        self.Back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Back.setObjectName("Back")
        self.BackLayout = QtWidgets.QGridLayout(self.Back)
        self.BackLayout.setContentsMargins(0, 0, 0, 0)
        self.BackLayout.setSpacing(0)
        self.BackLayout.setObjectName("BackLayout")

        self.Lyrics = QtWidgets.QFrame(self.Back)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.Lyrics.setFont(font)
        self.Lyrics.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Lyrics.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Lyrics.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Lyrics.setObjectName("Lyrics")
        self.LyricsMain = QtWidgets.QGridLayout(self.Lyrics)
        self.LyricsMain.setContentsMargins(0, 0, 0, 0)
        self.LyricsMain.setSpacing(0)
        self.LyricsMain.setObjectName("LyricsMain")
        self.BackLayout.addWidget(self.Lyrics, 1, 0, 1, 1)

        self.Lyrics2 = QtWidgets.QFrame(self.Back)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.Lyrics2.setFont(font)
        self.Lyrics2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Lyrics2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Lyrics2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Lyrics2.setObjectName("Lyrics2")
        self.LyricsMain2 = QtWidgets.QGridLayout(self.Lyrics2)
        self.LyricsMain2.setContentsMargins(0, 0, 0, 0)
        self.LyricsMain2.setSpacing(0)
        self.LyricsMain2.setObjectName("LyricsMain2")
        self.BackLayout.addWidget(self.Lyrics2, 2, 0, 1, 1)


        self.ButtonsNav = QtWidgets.QFrame(self.Back)
        self.ButtonsNav.setMinimumSize(QtCore.QSize(750, 60))
        self.ButtonsNav.setMaximumSize(QtCore.QSize(8192, 60))
        self.ButtonsNav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonsNav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsNav.setObjectName("ButtonsNav")
        self.ButtonsLayout = QtWidgets.QHBoxLayout(self.ButtonsNav)
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonsLayout.addItem(spacerItem)
        self.Account = QtWidgets.QFrame(self.ButtonsNav)
        self.Account.setMinimumSize(QtCore.QSize(40, 40))
        self.Account.setMaximumSize(QtCore.QSize(40, 40))
        self.Account.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Account.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Account.setObjectName("Account")
        self.AccountLayout = QtWidgets.QGridLayout(self.Account)
        self.AccountLayout.setContentsMargins(0, 0, 0, 0)
        self.AccountLayout.setSpacing(0)
        self.AccountLayout.setObjectName("AccountLayout")
        self.AccountButton = QtWidgets.QPushButton(self.Account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.AccountButton.sizePolicy().hasHeightForWidth())
        self.AccountButton.setSizePolicy(sizePolicy)
        self.AccountButton.setMinimumSize(QtCore.QSize(40, 40))
        self.AccountButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.AccountButton.setFont(font)
        self.AccountButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AccountButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AccountButton.setIcon(icon1)
        self.AccountButton.setIconSize(QtCore.QSize(25, 25))
        self.AccountButton.setObjectName("AccountButton")
        self.AccountLayout.addWidget(self.AccountButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.Account)
        self.Settings = QtWidgets.QFrame(self.ButtonsNav)
        self.Settings.setMinimumSize(QtCore.QSize(40, 40))
        self.Settings.setMaximumSize(QtCore.QSize(40, 40))
        self.Settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Settings.setObjectName("Settings")
        self.SettingsLayout = QtWidgets.QGridLayout(self.Settings)
        self.SettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingsLayout.setSpacing(0)
        self.SettingsLayout.setObjectName("SettingsLayout")
        self.SettingsButton = QtWidgets.QPushButton(self.Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy)
        self.SettingsButton.setMinimumSize(QtCore.QSize(40, 40))
        self.SettingsButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.SettingsButton.setFont(font)
        self.SettingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SettingsButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon2)
        self.SettingsButton.setIconSize(QtCore.QSize(25, 25))
        self.SettingsButton.setObjectName("SettingsButton")
        self.SettingsLayout.addWidget(self.SettingsButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.Settings)
        self.Previous = QtWidgets.QFrame(self.ButtonsNav)
        self.Previous.setMinimumSize(QtCore.QSize(40, 40))
        self.Previous.setMaximumSize(QtCore.QSize(40, 40))
        self.Previous.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Previous.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Previous.setObjectName("Previous")
        self.PreviousLayout = QtWidgets.QGridLayout(self.Previous)
        self.PreviousLayout.setContentsMargins(0, 0, 0, 0)
        self.PreviousLayout.setSpacing(0)
        self.PreviousLayout.setObjectName("PreviousLayout")
        self.PreviousButton = QtWidgets.QPushButton(self.Previous)
        self.PreviousButton.setMinimumSize(QtCore.QSize(40, 40))
        self.PreviousButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.PreviousButton.setFont(font)
        self.PreviousButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PreviousButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousButton.setIcon(icon3)
        self.PreviousButton.setIconSize(QtCore.QSize(25, 25))
        self.PreviousButton.setObjectName("PreviousButton")
        self.PreviousLayout.addWidget(self.PreviousButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.Previous)
        self.PlayStatus = QtWidgets.QFrame(self.ButtonsNav)
        self.PlayStatus.setMinimumSize(QtCore.QSize(40, 40))
        self.PlayStatus.setMaximumSize(QtCore.QSize(40, 40))
        self.PlayStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlayStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlayStatus.setObjectName("PlayStatus")
        self.PlayStatusLayout = QtWidgets.QGridLayout(self.PlayStatus)
        self.PlayStatusLayout.setContentsMargins(0, 0, 0, 0)
        self.PlayStatusLayout.setSpacing(0)
        self.PlayStatusLayout.setObjectName("PlayStatusLayout")
        self.PlayStatusButton = QtWidgets.QPushButton(self.PlayStatus)
        self.PlayStatusButton.setMinimumSize(QtCore.QSize(40, 40))
        self.PlayStatusButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.PlayStatusButton.setFont(font)
        self.PlayStatusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PlayStatusButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayStatusButton.setIcon(icon4)
        self.PlayStatusButton.setIconSize(QtCore.QSize(25, 25))
        self.PlayStatusButton.setObjectName("PlayStatusButton")
        self.PlayStatusLayout.addWidget(self.PlayStatusButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.PlayStatus)
        self.Next = QtWidgets.QFrame(self.ButtonsNav)
        self.Next.setMinimumSize(QtCore.QSize(40, 40))
        self.Next.setMaximumSize(QtCore.QSize(40, 40))
        self.Next.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Next.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Next.setObjectName("Next")
        self.NextLayout = QtWidgets.QGridLayout(self.Next)
        self.NextLayout.setContentsMargins(0, 0, 0, 0)
        self.NextLayout.setSpacing(0)
        self.NextLayout.setObjectName("NextLayout")
        self.NextButton = QtWidgets.QPushButton(self.Next)
        self.NextButton.setMinimumSize(QtCore.QSize(40, 40))
        self.NextButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.NextButton.setFont(font)
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon5)
        self.NextButton.setIconSize(QtCore.QSize(25, 25))
        self.NextButton.setObjectName("NextButton")
        self.NextLayout.addWidget(self.NextButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.Next)
        self.Lock = QtWidgets.QFrame(self.ButtonsNav)
        self.Lock.setMinimumSize(QtCore.QSize(40, 40))
        self.Lock.setMaximumSize(QtCore.QSize(40, 40))
        self.Lock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Lock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Lock.setObjectName("Lock")
        self.LockLayout = QtWidgets.QGridLayout(self.Lock)
        self.LockLayout.setContentsMargins(0, 0, 0, 0)
        self.LockLayout.setSpacing(0)
        self.LockLayout.setObjectName("LockLayout")
        self.LockButton = QtWidgets.QPushButton(self.Lock)
        self.LockButton.setMinimumSize(QtCore.QSize(40, 40))
        self.LockButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.LockButton.setFont(font)
        self.LockButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LockButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LockButton.setIcon(icon6)
        self.LockButton.setIconSize(QtCore.QSize(25, 25))
        self.LockButton.setObjectName("LockButton")
        self.LockLayout.addWidget(self.LockButton, 0, 0, 1, 1)
        self.ButtonsLayout.addWidget(self.Lock)
        self.Quit = QtWidgets.QFrame(self.ButtonsNav)
        self.Quit.setMinimumSize(QtCore.QSize(40, 40))
        self.Quit.setMaximumSize(QtCore.QSize(40, 40))
        self.Quit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Quit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Quit.setObjectName("Quit")
        self.QuitLayout = QtWidgets.QGridLayout(self.Quit)
        self.QuitLayout.setContentsMargins(0, 0, 0, 0)
        self.QuitLayout.setSpacing(0)
        self.QuitLayout.setObjectName("QuitLayout")
        self.QuitButton = QtWidgets.QPushButton(self.Quit)
        self.QuitButton.setMinimumSize(QtCore.QSize(40, 40))
        self.QuitButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.QuitButton.setFont(font)
        self.QuitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QuitButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuitButton.setIcon(icon7)
        self.QuitButton.setIconSize(QtCore.QSize(25, 25))
        self.QuitButton.setObjectName("QuitButton")
        self.QuitLayout.addWidget(self.QuitButton, 0, 1, 1, 1)
        self.ButtonsLayout.addWidget(self.Quit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonsLayout.addItem(spacerItem1)
        self.BackLayout.addWidget(self.ButtonsNav, 0, 0, 1, 1)
        self.MainLayout.addWidget(self.Back, 0, 0, 1, 1)

        self.retranslateUi(LyricsDisplay)
        QtCore.QMetaObject.connectSlotsByName(LyricsDisplay)

    def retranslateUi(self, LyricsDisplay):
        _translate = QtCore.QCoreApplication.translate
        LyricsDisplay.setWindowTitle(_translate("LyricsDisplay", "Lyrics"))
        self.Account.setToolTip(_translate("LyricsDisplay", "Spotify Login"))
        self.SettingsButton.setToolTip(_translate("LyricsDisplay", "Settings"))
        self.Previous.setToolTip(_translate("LyricsDisplay", "Previous"))
        self.PlayStatus.setToolTip(_translate("LyricsDisplay", "Play / Pause"))
        self.Next.setToolTip(_translate("LyricsDisplay", "Next"))
        self.Lock.setToolTip(_translate("LyricsDisplay", "Lock / Unlock"))
        self.QuitButton.setToolTip(_translate("LyricsDisplay", "Quit"))

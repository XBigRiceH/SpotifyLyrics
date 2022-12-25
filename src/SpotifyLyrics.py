import sys
import threading

import psutil
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Logger
import Settings
from ui.lyrics.LyricsWindow import LyricsWindow

if __name__ == '__main__':

    running_mode = "ONLINE"
    for i in psutil.pids():
        if psutil.Process(i).name() == "Spotify.exe":
            running_mode = "LOCAL"
            Logger.notice("Spotify process checker",
                          "Spotify is running on this pc, so we chose local media keys simulation to control music play.\nApplication starting...")
            break
    if running_mode == "ONLINE":
        Logger.notice("Spotify process checker",
                      "Spotify is not running on this pc, so we chose using spotify web-api to control music play.\nApplication starting...")

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = LyricsWindow(running_mode)
    threading.Thread(target=Settings.start, args=(QFontDatabase().families(), window,), daemon=True).start()
    window.show()
    sys.exit(app.exec_())

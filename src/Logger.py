import datetime

from plyer import notification

import Constants


def log(msg):
    print("[{0}] {1}".format(str(datetime.datetime.now()), msg), flush=True)


def notice(title, msg):
    notification.notify(
        title=title,
        message=msg,
        timeout=1,
        app_name="SpotifyLyrics",
        app_icon=Constants.resource_path("resources\\icon\\xh.ico")
    )

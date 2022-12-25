import os
import sys


class Lyrics:
    def __init__(self, track_id):
        self.track_id = track_id
        self.is_instrumental = False
        self.has_subtitle = False
        self.translated = False

        self.synced_lyrics = []
        self.translated_lyrics = []

    def get_lyrics_by_time(self, time):
        if not self.has_subtitle:
            return None
        try:
            for i in self.synced_lyrics[::-1]:
                if time >= i[0]:
                    next_index = self.synced_lyrics.index(i)
                    if next_index >= len(self.synced_lyrics) - 1:
                        roll_time = -1
                    else:
                        roll_time = self.synced_lyrics[self.synced_lyrics.index(i) + 1][0] - i[0]
                    return [str(i[1]), roll_time]
        except Exception as e:
            print(e)
        return None

    def get_translated_lyrics_by_time(self, time):
        if not self.translated:
            return None
        try:
            for i in self.translated_lyrics[::-1]:
                if time >= i[0]:
                    next_index = self.translated_lyrics.index(i)
                    if next_index >= len(self.translated_lyrics) - 1:
                        roll_time = -1
                    else:
                        roll_time = self.translated_lyrics[self.translated_lyrics.index(i) + 1][0] - i[0]
                    return [str(i[1]), roll_time]
        except Exception as e:
            print(e)
        return None


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

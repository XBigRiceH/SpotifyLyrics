import sys
import threading
import time
import webbrowser

import Logger
import Variables
import lyrics
import spotify
from . import LyricsWindowView


class LyricsWindow(LyricsWindowView.LyricsWindowView):
    def __init__(self, running_mode):
        super().__init__()
        super().init_signals()

        self.running_mode = running_mode

        self.AccountButton.clicked.connect(self.auth)
        self.SettingsButton.clicked.connect(self.settings)
        self.PreviousButton.clicked.connect(self.previous_track)
        self.NextButton.clicked.connect(self.next_track)
        self.PlayStatusButton.clicked.connect(self.play_or_pause)
        self.LockButton.clicked.connect(self.lock_or_unlock)
        self.QuitButton.clicked.connect(self.quit)

        self.profile: spotify.AuthManager.SpotifyAuthManager = None
        self.player_manager: spotify.PlayerControl.PlayerControl = None
        self.lyrics_checker_thread = threading.Thread(name="LyricsChecker",
                                                      target=self.lyrics_checker, daemon=True)
        self.current_playing_track = ""
        self.current_playing_lyrics = None
        self.current_playing_translated_lyrics = None

        self.netease_lyrics = lyrics.Netease.Netease()
        self.musixmatch_lyrics = lyrics.Musixmatch.Musixmatch()

        self.lyrics_checker_thread.start()
        self.updating_lyrics = False

        if len(Variables.refresh_token) > 10:
            self.auth()
            self.set_lyrics_text(1, "Logging in automatically...", 1)
            self.set_lyrics_text(2, "(●'◡'●)", 1)
        else:
            self.set_lyrics_text(1, "Waiting to log in...", 1)
            self.set_lyrics_text(2, "(❁´◡`❁)", 1)

    def lyrics_checker(self):
        while 1:
            time.sleep(0.5)
            try:
                if self.player_manager is None:
                    continue
                if not self.player_manager.ready or self.player_manager.play_status is None:
                    self.window().set_lyrics_text(1, "Playback not available or active", 1)
                    self.window().set_lyrics_text(2, "ˋ( ° ▽、° ) ", 1)
                    continue
                current_status: spotify.PlayerControl.PlayStatus = self.player_manager.play_status
                if current_status.track_type == 'ad':
                    self.window().set_lyrics_text(1, "Advertising time", 1)
                    self.window().set_lyrics_text(2, "(‾◡◝)", 1)
                    continue
                if current_status.current_track_id != self.current_playing_track and not self.updating_lyrics:
                    self.current_playing_track = current_status.current_track_id
                    self.current_playing_lyrics = None
                    self.current_playing_translated_lyrics = None
                    threading.Thread(target=self.update_lyrics).start()
                    threading.Thread(target=self.current_playing_translated_lyrics).start()

                if self.current_playing_lyrics is None or self.current_playing_translated_lyrics is None:
                    self.updating_lyrics = True
                    self.window().set_lyrics_text(1, current_status.current_track_name, 2000)
                    self.window().set_lyrics_text(2, "Updating lyrics...", 1)
                    continue

                musix_lyrics = self.current_playing_lyrics.get_lyrics_by_time(
                    current_status.progress_ms)
                netease_lyrics = self.current_playing_translated_lyrics.get_translated_lyrics_by_time(
                    current_status.progress_ms)

                if musix_lyrics is None:
                    netease_insteadof_musix_lyrics = self.current_playing_translated_lyrics.get_lyrics_by_time(
                        current_status.progress_ms)
                    if netease_insteadof_musix_lyrics is None:
                        self.window().set_lyrics_text(1, "I couldn't find lyrics of this song.", 1)
                        self.window().set_lyrics_text(2, "（；´д｀）ゞ", 1)
                    else:
                        self.window().set_lyrics_text(1, netease_insteadof_musix_lyrics[0],
                                                      netease_insteadof_musix_lyrics[1])
                else:
                    self.window().set_lyrics_text(1, musix_lyrics[0], musix_lyrics[1])

                if netease_lyrics is None:
                    self.window().set_lyrics_text(2, "Translation is not available now.", 2000)
                else:
                    self.window().set_lyrics_text(2, netease_lyrics[0], netease_lyrics[1])
            except Exception:
                pass

    def update_lyrics(self):
        self.current_playing_lyrics = self.musixmatch_lyrics.get_lyrics(self.player_manager.play_status)
        self.current_playing_translated_lyrics = self.netease_lyrics.get_lyrics(self.player_manager.play_status)
        self.updating_lyrics = False

    def auth(self):
        threading.Thread(target=self.real_auth).start()

    def real_auth(self):
        refresh = self.player_manager is not None
        if self.player_manager is not None:
            self.player_manager.kill = True
            self.profile.kill = True
            self.profile = None
            self.player_manager = None

        if refresh:
            self.set_lyrics_text(1, "Waiting to re-log in...", 1)
            self.set_lyrics_text(2, "( •̀ ω •́ )✧", 1)
        self.profile = spotify.AuthManager.SpotifyAuthManager(Variables.client_id, Variables.client_secret)
        self.profile.login(refresh)

        self.player_manager = spotify.PlayerControl.PlayerControl(self.running_mode, self.profile, self)

    def settings(self):
        webbrowser.open("http://127.0.0.1:60001/manage_page")
        pass

    def previous_track(self):
        if self.player_manager is not None:
            self.player_manager.previous_track()

    def next_track(self):
        if self.player_manager is not None:
            self.player_manager.next_track()

    def play_or_pause(self):
        if self.locked:
            self.lock_or_unlock()
            return
        if self.player_manager is not None:
            self.player_manager.play_or_pause()

    def lock_or_unlock(self):
        if not self.locked:
            self.lockEvent()
        else:
            if self.player_manager is None or self.player_manager.play_status is None:
                self.unlockEvent(False)
            else:
                self.unlockEvent(self.player_manager.play_status.is_playing)

    def quit(self):
        self.hide()
        Logger.notice("Exit", "SpotifyLyrics exited, goodbye.")
        sys.exit(0)

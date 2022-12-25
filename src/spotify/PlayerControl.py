import threading
import time

import requests
import win32api

import Logger
from . import AuthManager


class PlayStatus:
    def __init__(self):
        self.update_time = None
        self.is_playing = False
        self.progress_ms = 0
        self.current_track_id = None
        self.current_track_name = None
        self.current_artist_name = None
        self.track_type = None
        self.album_name = None
        self.duration = None


class PlayerControl:
    def __init__(self, running_mode, auth_manager: AuthManager.SpotifyAuthManager, window):
        self.kill = False
        self.running_mode = running_mode
        self.auth_manager = auth_manager
        self.current_playing_checker = threading.Thread(name="PlayStatusChecker", target=self.playing_checker,
                                                        daemon=True)
        self.current_playing_progress_updater = threading.Thread(name="PlayProgressUpdater",
                                                                 target=self.progress_updater, daemon=True)
        self.current_playing_checker.start()
        self.current_playing_progress_updater.start()

        self.window = window
        self.play_status: PlayStatus = PlayStatus()
        self.last_button_manual_control_time = time.time_ns()

        self.ready = False

    def progress_updater(self):
        Logger.log("PlayProgressUpdater Started")
        while 1:
            if self.kill:
                return
            time.sleep(0.05)
            try:
                if self.play_status.progress_ms is None or self.play_status.update_time is None:
                    continue
                if abs(int(time.time_ns() / 1000000) - self.play_status.progress_ms <= 1):
                    continue
                if not self.play_status.is_playing:
                    continue
                self.play_status.progress_ms = self.play_status.progress_ms + int(
                    time.time_ns() / 1000000) - self.play_status.update_time
                self.play_status.update_time = int(time.time_ns() / 1000000)
                # Logger.log("Updated progress_ms -> "+str(self.play_status.progress_ms))
            except Exception:
                pass

    def playing_checker(self):
        Logger.log("PlayStatusChecker Started")
        while 1:
            if self.kill:
                return
            try:
                time.sleep(1)
                if self.auth_manager.access_token is None:
                    pass
                request_start_time = time.time_ns()
                profile = requests.get("https://api.spotify.com/v1/me/player", headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.auth_manager.access_token
                })
                if profile.status_code == 200:
                    self.ready = True
                else:
                    self.ready = False
                self.play_status.is_playing = bool(profile.json()['is_playing'])
                if not self.window.locked and request_start_time > self.last_button_manual_control_time:
                    self.window.set_pause_button_icon(self.play_status.is_playing)
                self.play_status.progress_ms = profile.json()['progress_ms']
                self.play_status.track_type = profile.json()['currently_playing_type']
                self.play_status.current_artist_name = ", ".join(
                    art["name"] for art in profile.json()["item"]["artists"])
                self.play_status.current_track_name = profile.json()["item"]["name"]
                self.play_status.current_track_id = profile.json()["item"]["id"]
                self.play_status.album_name = profile.json()["item"]["album"]['name']
                self.play_status.duration = profile.json()['item']['duration_ms']
                self.play_status.update_time = int(time.time_ns() / 1000000)
            except Exception:
                pass

    def play_or_pause(self):
        if self.running_mode == "LOCAL":
            win32api.keybd_event(0xB3, win32api.MapVirtualKey(0xB3, 0))
            self.play_status.is_playing = not self.play_status.is_playing
            self.window.set_pause_button_icon(self.play_status.is_playing)
            self.last_button_manual_control_time = time.time_ns()
        else:
            if self.auth_manager.premium:
                profile = requests.put("https://api.spotify.com/v1/me/player/pause", headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.auth_manager.access_token
                })
                if profile.status_code != 204:
                    Logger.log("Play/Pause process failed")
            else:
                Logger.notice("Play / Pause",
                              "Only spotify premium user could use player control in 'spotify web-api' mode.")

    def next_track(self):
        if self.running_mode == "LOCAL":
            win32api.keybd_event(0xB0, win32api.MapVirtualKey(0xB0, 0))
            self.play_status.is_playing = True
            self.window.set_pause_button_icon(self.play_status.is_playing)
            self.last_button_manual_control_time = time.time_ns()
        else:
            if self.auth_manager.premium:
                profile = requests.post("https://api.spotify.com/v1/me/player/next", headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.auth_manager.access_token
                })
                if profile.status_code != 204:
                    Logger.log("Play/Pause process failed")
            else:
                Logger.notice("Next track",
                              "Only spotify premium user could use player control in 'spotify web-api' mode.")

    def previous_track(self):
        if self.running_mode == "LOCAL":
            win32api.keybd_event(0xB1, win32api.MapVirtualKey(0xB1, 0))
            self.play_status.is_playing = True
            self.window.set_pause_button_icon(self.play_status.is_playing)
            self.last_button_manual_control_time = time.time_ns()
        else:
            if self.auth_manager.premium:
                profile = requests.post("https://api.spotify.com/v1/me/player/previous", headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.auth_manager.access_token
                })
                if profile.status_code != 204:
                    Logger.log("Play/Pause process failed")
            else:
                Logger.notice("Previous track",
                              "Only spotify premium user could use player control in 'spotify web-api' mode.")

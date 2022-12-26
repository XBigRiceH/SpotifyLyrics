import base64
import threading
import time
import urllib.parse
import uuid
import webbrowser

import requests

import Logger
import Variables


class SpotifyAuthManager:
    def __init__(self, client_id, client_secret):
        self.kill = False
        self.updater = None
        self.auth_code = None
        self.access_token = None
        self.refresh_token = None
        self.tip = "Logging into spotify..."
        self.state = uuid.uuid4()
        self.return_state = None
        self.client_id = client_id
        self.client_secret = client_secret
        self.premium = False

    def login(self, refresh):
        if len(str(Variables.refresh_token)) > 10 and not refresh:
            self.refresh_token = Variables.refresh_token
            if self.real_refresh_user_token():
                self.check_user_product()
                return
        self.get_user_auth_code()
        self.get_user_token()
        self.check_user_product()

    def get_user_auth_code(self):
        scopes = [
            "user-read-playback-state",
            "user-modify-playback-state",
            "user-read-currently-playing",
            "user-read-private",
            "user-read-email"
        ]
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": "http://127.0.0.1:60001/callback",
            "scope": " ".join(scopes),
            "state": self.state
        }
        url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
        webbrowser.open(url)

        while 1:
            if self.auth_code is not None and self.return_state is not None:
                break
            time.sleep(.1)

        if str(self.return_state) == str(self.state):
            Logger.log("Got User Code -> " + self.auth_code)
        else:
            raise Exception("Invalid state, Cors detected.")

    def get_user_token(self):
        profile = requests.post("https://accounts.spotify.com/api/token", headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + base64.b64encode(
                (self.client_id + ":" + self.client_secret).encode("utf-8")).decode("utf-8")
        }, data={
            "grant_type": "authorization_code",
            "code": self.auth_code,
            "redirect_uri": "http://127.0.0.1:60001/callback"
        })
        self.access_token = profile.json()['access_token']
        self.refresh_token = profile.json()['refresh_token']
        Logger.log("Got User access_token -> " + self.access_token)
        Logger.log("Got User refresh_token -> " + self.refresh_token)
        self.updater = threading.Thread(name="UserAccessTokenUpdater", target=self.refresh_user_token, daemon=True)
        self.updater.start()
        Variables.refresh_token = self.refresh_token
        Variables.save_configs()
        return True

    def real_refresh_user_token(self):
        profile = requests.post("https://accounts.spotify.com/api/token", headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + base64.b64encode(
                (self.client_id + ":" + self.client_secret).encode("utf-8")).decode("utf-8")
        }, data={
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        })
        if not profile.status_code == 200:
            return False
        if len(profile.text) <= 10:
            return False
        if 'access_token' not in profile.json():
            return False
        self.access_token = profile.json()['access_token']
        Logger.log("Updated User access_token -> " + self.access_token)
        return True

    def refresh_user_token(self):
        Logger.log("UserAccessTokenUpdater Started")
        while 1:
            if self.kill:
                return
            time.sleep(1800)
            self.real_refresh_user_token()

    def check_user_product(self):
        profile = requests.get("https://api.spotify.com/v1/me", headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        })
        self.premium = (profile.json()['product'] == "premium")

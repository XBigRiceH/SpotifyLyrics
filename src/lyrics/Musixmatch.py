import hashlib
import sys
import time
import urllib.parse

import arrow
import requests

import Logger
import Variables
from Constants import Lyrics
from spotify.PlayerControl import PlayStatus


class Musixmatch:
    def __init__(self):
        self.user_token = Variables.musixmatch_token
        self.session = requests.session()
        self.session.headers = {
            "authority": "apic-desktop.musixmatch.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "cookie": "x-mxm-token-guid="
        }
        self.update_user_token()

    def get_new_user_token(self):
        result = requests.get(
            "https://apic-desktop.musixmatch.com/ws/1.1/token.get?" + urllib.parse.urlencode({
                "format": "json",
                "app_id": "web-desktop-app-v1.0",
                "signature_protocol": "sha1",
                "signature": hashlib.sha1(("secretsuper/ws/1.1/token.get" + arrow.get(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).to("UTC").strftime("%Y%m%d")).encode(
                    "utf-8")).hexdigest()
            }))
        if result.json()['message']['header']['status_code'] != 200:
            Logger.notice("Musixmatch service not available now", "Please wait for about 1 minute and then try again.")
            sys.exit()
        self.user_token = result.json()['message']['body']['user_token']
        Variables.musixmatch_token = self.user_token
        Variables.save_configs()

    def update_user_token(self):
        if len(self.user_token) > 10:
            result = self.session.get(
                "https://apic-desktop.musixmatch.com/ws/1.1/spotify.resource.get?" + urllib.parse.urlencode({
                    "format": "json",
                    "resource": "me",
                    "app_id": "web-desktop-app-v1.0",
                    "usertoken": self.user_token,
                    "guid": "",
                    "signature_protocol": "sha1",
                    "signature": hashlib.sha1(("secretsuper/ws/1.1/spotify.resource.get" + arrow.get(
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).to("UTC").strftime("%Y%m%d")).encode(
                        "utf-8")).hexdigest()
                }))
            if result.json()['message']['header']['status_code'] != 200:
                self.get_new_user_token()
        else:
            self.get_new_user_token()

    def get_lyrics(self, play_status: PlayStatus):
        lyrics_result = requests.get(
            "https://apic-desktop.musixmatch.com/ws/1.1/macro.subtitles.get?" + urllib.parse.urlencode({
                "format": "json",
                "namespace": "lyrics_synched",
                "part": "lyrics_crowd%2Cuser%2Clyrics_verified_by",
                "q_artist": play_status.current_artist_name,
                "q_artists": play_status.current_artist_name,
                "q_track": play_status.current_track_name,
                "q_album": play_status.album_name,
                "tags": "nowplaying",
                "track_spotify_id": "spotify:track:" + play_status.current_track_id,
                "subtitle_format": "lrc",
                "app_id": "web-desktop-app-v1.0",
                "usertoken": self.user_token,
                "signature_protocol": "sha1",
                "signature": hashlib.sha1(("secretsuper/ws/1.1/macro.subtitles.get" + arrow.get(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).to("UTC").strftime("%Y%m%d")).encode(
                    "utf-8")).hexdigest()
            }))

        lyrics_object = Lyrics(play_status.current_track_id)
        if lyrics_result.json()['message']['header']['status_code'] != 200:
            Logger.notice("Musixmatch service not available now", "Please wait for about 1 minute and then try again.")
            sys.exit()
        lyrics_object.is_instrumental = bool(
            lyrics_result.json()['message']['body']['macro_calls']['matcher.track.get']['message']['body']['track'][
                'instrumental'])
        lyrics_object.has_subtitle = bool(
            lyrics_result.json()['message']['body']['macro_calls']['matcher.track.get']['message']['body']['track'][
                'has_subtitles'])

        if not lyrics_object.is_instrumental and lyrics_object.has_subtitle:
            lyrics_object.synced_lyrics = []
            for j in str(
                    lyrics_result.json()['message']['body']['macro_calls']['track.subtitles.get']['message']['body'][
                        'subtitle_list'][0]['subtitle']['subtitle_body']).split('\n'):
                if len(j.replace(" ", "")) == 0:
                    continue

                closeBegin = j.find("]")
                progress = j[:closeBegin + 1]
                lyrics = j[closeBegin + 1:]
                if lyrics[:1] == " ":
                    lyrics = lyrics[1:]

                if len(lyrics.replace(" ", "")) == 0:
                    lyrics = "♪"
                lyrics_object.synced_lyrics.append([
                    int(int(progress[1:3]) * 60 * 1000 + float(progress[4:closeBegin].replace(":", ".")) * 1000),
                    lyrics
                ])

        return lyrics_object


Musixmatch()

import urllib.parse

import requests

from Constants import Lyrics
from spotify.PlayerControl import PlayStatus


class Netease:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\""
        }
        self.session.get("https://cloudmusic-xh.vercel.app/register/anonimous")

    def get_lyrics(self, play_status: PlayStatus):
        song_result = self.session.get("https://cloudmusic-xh.vercel.app/search?" + urllib.parse.urlencode({
            "keywords": play_status.current_track_name + " " + play_status.album_name + " " + play_status.current_artist_name,
            "realIP": "220.160.119.140",
            "type": 1
        }))

        lyrics_object = Lyrics(play_status.current_track_id)

        if 'songs' not in song_result.json()['result']:
            return lyrics_object
        if len((song_result.json()['result']['songs'])) == 0:
            return lyrics_object

        song_id = song_result.json()['result']['songs'][0]['id']
        lyrics_result = self.session.get("https://cloudmusic-xh.vercel.app/lyric?id=" + str(song_id))
        if 'lrc' not in lyrics_result.json():
            return lyrics_object

        lyrics_object.is_instrumental = lyrics_result.json()['lrc']['lyric'].count("纯音乐，请欣赏") > 0
        lyrics_object.has_subtitle = not lyrics_object.is_instrumental
        lyrics_object.translated = (
                'tlyric' in lyrics_result.json() and len(lyrics_result.json()['tlyric']['lyric']) > 0)
        if lyrics_object.has_subtitle:
            lyrics_object.synced_lyrics = []
            for j in str(
                    lyrics_result.json()['lrc']['lyric']).split('\n'):
                if len(j.replace(" ", "")) == 0:
                    continue
                closeBegin = j.find("]")

                if len(j) == closeBegin + 1:
                    progress = j
                    lyrics = ""
                else:
                    progress = j[:closeBegin + 1]
                    lyrics = j[closeBegin + 1:]
                    if lyrics[:1] == " ":
                        lyrics = lyrics[1:]

                lyrics_object.synced_lyrics.append([
                    int(int(progress[1:3]) * 60 * 1000 + float(progress[4:closeBegin].replace(":", ".")) * 1000),
                    lyrics
                ])

        if lyrics_object.translated:
            lyrics_object.translated_lyrics = []
            for j in str(
                    lyrics_result.json()['tlyric']['lyric']).split('\n'):
                if len(j.replace(" ", "")) == 0:
                    continue
                if j[1] != '0':
                    continue

                closeBegin = j.find("]")

                if len(j) == closeBegin + 1:
                    progress = j
                    lyrics = ""
                else:
                    progress = j[:closeBegin + 1]
                    lyrics = j[closeBegin + 1:]
                    if lyrics[:1] == " ":
                        lyrics = lyrics[1:]

                if len(lyrics.replace(" ", "")) == 0:
                    lyrics = "♪"

                lyrics_object.translated_lyrics.append([
                    int(int(progress[1:3]) * 60 * 1000 + float(progress[4:closeBegin].replace(":", ".")) * 1000),
                    lyrics
                ])
        return lyrics_object

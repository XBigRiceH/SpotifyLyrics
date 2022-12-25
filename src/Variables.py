import os

import win32api
import yaml

default_conf = '''font-color:
  r: 251
  g: 227
  b: 182
font-effect-color:
  r: 200
  g: 184
  b: 148
background-color:
  r: 50
  g: 50
  b: 50
  a: 0.2
font-family: "微软雅黑"
refresh-token: ""
musixmatch-token: ""
client-id: "d9bf564645704c3597edebc24df8ef58"
client-secret: "c3c2338a17fc43318ee5e0ed793260aa"
always-top: true
show-background-when-unlocked: false
show-background-when-locked: false
'''

if not os.path.exists("config.yml"):
    with open("config.yml", "a", encoding="utf-8") as f:
        f.write(default_conf)
        f.flush()

config = None
try:
    with open("config.yml", "r", encoding='utf-8') as f:
        config = yaml.load(f.read(), Loader=yaml.Loader)
except Exception:
    with open("config.yml", "rw", encoding="utf-8") as f:
        f.write(default_conf)
        f.flush()
        config = yaml.load(f.read(), Loader=yaml.Loader)

font_color = (config['font-color']['r'], config['font-color']['g'], config['font-color']['b'])
font_blur_color = (config['font-effect-color']['r'], config['font-effect-color']['g'], config['font-effect-color']['b'])
background_color = (config['background-color']['r'], config['background-color']['g'], config['background-color']['b'],
                    config['background-color']['a'])
font_family = config['font-family']
refresh_token = config['refresh-token']
musixmatch_token = config['musixmatch-token']
always_top = config['always-top']
client_id = config['client-id']
client_secret = config['client-secret']
show_background_when_locked = config['show-background-when-locked']
show_background_when_unlocked = config['show-background-when-unlocked']
monitor_refresh_rate = win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1).DisplayFrequency


def save_configs():
    with open("config.yml", "w") as io:
        yaml.dump({
            'font-color': {
                'r': font_color[0],
                'g': font_color[1],
                'b': font_color[2],
            },
            'font-effect-color': {
                'r': font_blur_color[0],
                'g': font_blur_color[1],
                'b': font_blur_color[2],
            },
            'background-color': {
                'r': background_color[0],
                'g': background_color[1],
                'b': background_color[2],
                'a': background_color[3]
            },
            'font-family': font_family,
            'refresh-token': refresh_token,
            'musixmatch-token': musixmatch_token,
            'always-top': always_top,
            'client-id': client_id,
            'client-secret': client_secret,
            'show-background-when-unlocked': show_background_when_unlocked,
            'show-background-when-locked': show_background_when_locked
        }, io)

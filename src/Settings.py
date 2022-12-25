import json

import bottle
from PyQt5.QtGui import QColor
from bottle import route, run, response, request, static_file

import Constants
import Variables
from ui.lyrics.LyricsWindow import LyricsWindow


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers[
            'Access-Control-Allow-Headers'] = 'content-type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            return fn(*args, **kwargs)

    return _enable_cors


@route('/settings', method=['GET', 'OPTIONS'])
@enable_cors
def settings():
    return json.dumps({
        'font-color': {
            'r': Variables.font_color[0],
            'g': Variables.font_color[1],
            'b': Variables.font_color[2],
        },
        'font-effect-color': {
            'r': Variables.font_blur_color[0],
            'g': Variables.font_blur_color[1],
            'b': Variables.font_blur_color[2],
        },
        'background-color': {
            'r': Variables.background_color[0],
            'g': Variables.background_color[1],
            'b': Variables.background_color[2],
            'a': Variables.background_color[3]
        },
        'font-family': Variables.font_family,
        'refresh-token': Variables.refresh_token,
        'musixmatch-token': Variables.musixmatch_token,
        'always-top': Variables.always_top,
        'client-id': Variables.client_id,
        'client-secret': Variables.client_secret,
        'show-background-when-unlocked': Variables.show_background_when_unlocked,
        'show-background-when-locked': Variables.show_background_when_locked
    }, ensure_ascii=False)


@route('/callback', method='GET')
@enable_cors
def callback():
    if window.profile is not None:
        if 'code' in request.query and window.profile.auth_code is None:
            window.profile.auth_code = request.query['code']
        if 'state' in request.query and window.profile.return_state is None:
            window.profile.return_state = request.query['state']
    return bottle.template('done')


@route("/update_settings", method=['POST', 'OPTIONS'])
@enable_cors
def update_settings():
    global window
    new_settings = json.load(request.body)
    Variables.font_color = (
        new_settings['font-color']['r'], new_settings['font-color']['g'], new_settings['font-color']['b'])
    Variables.font_blur_color = (new_settings['font-effect-color']['r'], new_settings['font-effect-color']['g'],
                                 new_settings['font-effect-color']['b'])
    Variables.background_color = (
        new_settings['background-color']['r'], new_settings['background-color']['g'],
        new_settings['background-color']['b'],
        new_settings['background-color']['a'])
    Variables.font_family = new_settings['font-family']
    Variables.refresh_token = new_settings['refresh-token']
    Variables.musixmatch_token = new_settings['musixmatch-token']
    Variables.always_top = new_settings['always-top']
    Variables.show_background_when_unlocked = new_settings['show-background-when-unlocked']
    Variables.show_background_when_locked = new_settings['show-background-when-locked']
    Variables.client_id = new_settings['client-id']
    Variables.client_secret = new_settings['client-secret']
    Variables.save_configs()

    stylesheet = f"color:rgb({Variables.font_color[0]}, {Variables.font_color[1]}, {Variables.font_color[2]})"
    window.lyrics_widgets_up.set_label_stylesheet(stylesheet)
    window.lyrics_widgets_down.set_label_stylesheet(stylesheet)

    window.effect.setColor(
        QColor(int(Variables.font_blur_color[0]), int(Variables.font_blur_color[1]), int(Variables.font_blur_color[2])))
    window.effect2.setColor(
        QColor(int(Variables.font_blur_color[0]), int(Variables.font_blur_color[1]), int(Variables.font_blur_color[2])))

    window.font.setFamily(Variables.font_family)
    window.lyrics_widgets_up.set_font(window.font)
    window.lyrics_widgets_down.set_font(window.font)

    return json.dumps({
        "success": True
    })


app = bottle.default_app()


@app.get('/static/<filename:path>')
def get_static_files(filename):
    return static_file(filename, root=Constants.resource_path("resources\\static"))


@app.get('/manage_page')
def index():
    return bottle.template('index')


fonts = []
window = None


@route('/installed_fonts', method=['GET', 'OPTIONS'])
@enable_cors
def fonts():
    global fonts
    return json.dumps({
        'fonts': fonts
    }, ensure_ascii=False)


def start(installed_fonts, window_inst: LyricsWindow):
    global fonts, window, app
    window = window_inst
    fonts = installed_fonts
    bottle.TEMPLATE_PATH.insert(0, Constants.resource_path("resources\\templates"))
    run(app, host='127.0.0.1', port=60001, debug=True)

# Spotify Lyrics

### Features - 特性

* can control the playback of music - 可以控制音乐的播放
  * If Spotify is running locally, it will control through simulating media keys - 如果本地运行着Spotify, 会通过模拟媒体键来控制
  * If Spotify is not running locally, it will control using the Spotify Web-API(Premium user only) - 如果本地没有运行Spotify, 会使用Spotify Web-API来控制(由于官方限制,该控制方式仅Premium用户有效)
* The lyrics are synchronized with the playback progress - 歌词与播放进度同步
* The lyrics are fetched from Musixmatch and Netease CloudMusic - 歌词从Musixmatch和网易云音乐抓取
  * For foreign lyrics, Musixmatch is the first choice; if not available, Netease CloudMusic will be used - 外文歌词首选Musixmatch, 若无则使用网易云音乐
  * The Chinese lyrics translation comes from Netease CloudMusic - 中文翻译来自网易云音乐
* The size of the floating window can be adjusted freely - 悬浮窗大小可以自由调整
* The background color of the floating window, the color of the lyrics font, the color of the lyrics outline, and the font of the lyrics can all be modified - 悬浮窗背景颜色,歌词字体颜色,歌词描边颜色,歌词字体均可修改
* If the lyrics exceed the length of the floating window, they will automatically scroll - 如果歌词超出悬浮窗长度会自动滚动

### How to use - 使用教程

* Register on the [Spotify Developer Platform](https://developer.spotify.com/dashboard/login) and create an app - 在[Spotify开发者平台](https://developer.spotify.com/dashboard/login)上注册并且创建一个app
* Click the **EDIT SETTINGS** button and add **http://127.0.0.1:60001/callback** as a **Redirect URL** - 点击 **EDIT SETTINGS**按钮,添加**http://127.0.0.1:60001/callback**为一个**Redirect URL**
* Go to the **USERS AND ACCESS** menu and add your own Spotify account - 转到**USERS AND ACCESS**菜单 添加你自己的账号
* Run this project, click the second setting button, and enter the obtained Client ID and Client Secret in the web interface, then click save button - 运行本项目,点击悬浮窗上第二个设置按钮,在Web界面中填入刚刚获取的Client ID和Client Secret,点击保存
* Click the first login button and log in to your Spotify account - 点击悬浮窗上第一个登录按钮,登录你的Spotify账号
* Enjoy it - 好了

### Screenshots - 程序截图

![Unlocked](readme_images\1.jpg)

![Locked](readme_images\2.jpg)

![Win10+ToastNotice](readme_images\3.jpg)

![WebSettingUI](readme_images\4.jpg)

![Running](readme_images\5.gif)



### Package as an executable file - 打包为一个可执行文件

* Install `pyinstaller` - 安装 `pyinstaller`

* Switch to folder `src` - 转到`src`目录下

* Use the following command to generate the .spec file - 使用以下指令创建.spec文件

  * ```bash
    pyi-makespec --onefile --icon "F:/PythonProjects/SpotifyLyrics/src/resources/static/favicon.ico" --add-data "F:/PythonProjects/SpotifyLyrics/src/resources;resources/" --paths "F:/PythonProjects/SpotifyLyrics/src/lyrics" --paths "F:/PythonProjects/SpotifyLyrics/src/spotify" --paths "F:/PythonProjects/SpotifyLyrics/src/ui"  "F:/PythonProjects/SpotifyLyrics/src/SpotifyLyrics.py" --noconsole --hidden-import "plyer.playforms" --hidden-import "plyer.platforms.win" --hidden-import "plyer.platforms.win.notification" --hidden-import "plyer.platforms.win.libs"
    ```

* Locate line 8 and add following items to the list: `'./Constants.py', './Logger.py', './Settings.py', './Variables.py'` - 在第8行的第一个数组中加入以上几个内容

* Edit your `bottle` module library file `bottle.py` and use following codes to redefine `_stdout` and `_stderr` on line 71 - 转到`bottle`库文件`bottle.py`的71行,使用以下代码重定义 `_stdout` 和`_stderr`

  * ```python
    import tempfile
    tempf = tempfile.TemporaryFile()
    def redefine_write(msg):
        global tempf
        tempf.write(msg.encode("utf-8"))
    _stdout, _stderr = redefine_write, redefine_write

* Use the following command to package the .exe file - 使用以下指令打包.exe
  * ```bash
      pyinstaller ./SpotifyLyrics.spec
      ```

* Now you could find your .exe file in folder `dist` - 可执行文件已打包到`dist`目录下
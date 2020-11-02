import asyncio
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QByteArray
from PySide2.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QGuiApplication
from window.window import Ui_Form
from music163.get_music import GetMusic
from config.edit import fileRW, download, getConfig, setPath


class Method(QMainWindow, Ui_Form):
    loop = None  # 事件循环
    pgs: int = 0    # 下载时进度条计数
    column: int = 0  # 音乐列表的列,也表示已经获取的音乐的数量
    max_num: int = 5  # 最大下载数量
    counter: int = 0  # 执行时计数器
    music_data = list()  # 获取的音乐内容
    detailed_info: int = 0  # 展示数据的索引
    load_title: str = None  # 下载的标题
    get_music: GetMusic = None  # 获取音乐的API
    clipboard = QGuiApplication  # 用于粘贴复制
    error_list = {
        '200': ['警告', '勿频繁点击，可能会导致程序崩溃！请稍后重试！'],
        'stop': ['警告', '任务已中止！'],
        'InputError': ['警告', '检查是否输入有误!']
    }

    # 设置软件配置文件
    def setConfig(self, cfg: dict = None):
        if not cfg: cfg = getConfig()
        self.setWindowTitle(cfg['app_name'])
        self.ctl_path.setText(cfg['path_download'])
        self.ctl_maxNumber.setValue(cfg['max_download_number'])
        self.setWindowIcon(self.icon(cfg['path_icon'] or cfg['base64_icon']))

    # 在结束时保存配置文件
    def closeSaveConfig(self, cfg: dict = None):
        if not cfg: cfg = getConfig()
        cfg['path_app'] = setPath()
        cfg['path_download'] = self.ctl_path.text()
        cfg['max_download_number'] = self.ctl_maxNumber.value()
        fileRW('./', 'config.json', 'w', cfg)

    @staticmethod
    def icon(base64=None, icon=None):
        if not icon:
            icon = QPixmap()
            base64 = bytes(base64, encoding='utf-8')
            icon.loadFromData(QByteArray.fromBase64(base64))
        return QIcon(icon)

    @staticmethod
    def regExp(string: str, *args):
        for i in args:
            if not(i in string):
                return False
        return True

    # 获取需要保存的路径
    def getDirectory(self):
        return QFileDialog.getExistingDirectory(None, "选择文件", self.ctl_path.text())

    # 粘贴
    @staticmethod
    def paste():
        return QGuiApplication.clipboard().mimeData().text()

    # 复制
    @staticmethod
    def copy(text):
        QGuiApplication.clipboard().setText(text)

    # 弹窗
    def popUp(self, title: str = None, msg=None, state=None):
        if state:
            title = self.error_list[state][0]
            msg = self.error_list[state][1]
        QMessageBox.information(self, title, self.tr(msg))

    # 进度条
    def progressBar(self, value: int = 0, title: str = None, ):
        if value > 99:
            value = 0
            title = '已完成'
        if title:
            self.ctl_state.setText(title)
        self.ctl_progressBar.setValue(value)
        return value

    # 在点击时
    def onClick(self, element):
        def _(func):
            @element.clicked.connect
            def _():
                asyncio.ensure_future(func(), loop=self.loop)

        return _

    # 设置音乐数量
    def setMusicNumber(self, number=1):
        self.column += number
        self.ctl_number.setText(str(self.column))

    # 添加到表单
    def addToTable(self, music: str, artists: str, playtime: str, mid: int, **kwargs):
        """
        :param music: 音乐名字
        :param artists: 作者名字
        :param playtime: 播放事件
        :param mid: 音乐ID
        """
        self.ctl_musicList.setRowCount(self.column + 1)
        self.music_data.append(dict(kwargs, **{
            'mid': mid,
            'music': self._newWidget(music, mid, 0),
            'artists': self._newWidget(artists, mid, 1),
            'playtime': self._newWidget(playtime, mid, 2),
            'lyric': self._newCheckbox(3),
            'download': self._newCheckbox(4)
        }))
        self.setMusicNumber()

    # 新单元格并且将新单元格添加到表格里面，并且返回text
    def _newWidget(self, text: str, mid: int, row: int, ):
        button = QPushButton()
        button.setCursor(Qt.PointingHandCursor)
        button.setStyleSheet('background-color: white;border:0')
        button.setText(text)
        self._widgetClick(button, mid)
        self.ctl_musicList.setCellWidget(self.column, row, button)
        return text

    # 新单元格点击时
    def _widgetClick(self, element, mid: int):
        @self.onClick(element)
        async def _():
            if self.detailed_info != mid:
                for msg in self.queryList():
                    if msg['mid'] == mid:
                        self.detailed_info = mid
                        self.setDetailedInfo(msg)

    # 新复选框并且将复选框添加到表格里面
    def _newCheckbox(self, row: int):
        """
        :param row:行号
        :return:
        """
        checkbox = QCheckBox()
        checkbox.setChecked(True)
        checkbox.setStyleSheet('margin-left: 25px')
        self.ctl_musicList.setCellWidget(self.column, row, checkbox)
        return checkbox

    # 设置展示
    def setDetailedInfo(self, msg: dict):
        self.ctl_music.setText(msg['music'])
        self.ctl_artists.setText(msg['artists'])
        self.ctl_time.setText(msg['playtime'])
        self.ctl_id.setText(str(msg['mid']))
        asyncio.ensure_future(self.addLyrics(mid=msg['mid']))

    # 删除
    def delete(self):
        self.music_data.pop(self.counter)
        self.ctl_musicList.removeRow(self.counter)
        self.setMusicNumber(-1)

    # 获取音乐列表所有音乐
    def queryList(self, key: str = None, arg__1: bool = True):
        """
        :param key: 复选框键值，依靠键值来做判断，如果该键值是满足arg__1则返回该迭代
        :param arg__1: 判断点击值
        :return: 音乐列表生成器
        """
        self.counter = self.column
        while self.counter > 0:
            self.counter -= 1
            if key:
                if self.music_data[self.counter][key].isChecked() is arg__1:
                    yield self.music_data[self.counter]
            else:
                yield self.music_data[self.counter]

    # 添加歌词
    async def addLyrics(self, lyric: str = None, *, mid: int = None):
        """
        :param lyric: 传入歌词，如果没有歌词可以传入mid
        :param mid: 利用mid发送请求获取歌词
        利用mid获取歌词
        获取后清空之前的文本
        清空后填入歌词
        :return:
        """
        if mid:
            lyric = await self.get_music.get_lyrics(mid)
            lyric = '<br>'.join(lyric.split('\n'))
        self.ctl_lyric.clear()
        self.ctl_lyric.append(rf'<p align="center">{lyric}<\p>')

    async def downloadMusic(self, msg: dict, path: str = None):
        """
        :param num:
        :param path:
        :param msg:音乐的数据
        先进行下载任务，下载完成后进行音乐下载
        目的是为了防止下载时候出现音乐下载失败就只有歌词
        isChecked 看音乐或歌词是否有被选中，选中的进行下载
        loader 下载完成后告诉进度条自己下载到某处
        :return:
        """
        self.counter += 1
        path = self.ctl_path.text()
        if msg['download'].isChecked():
            download(await self.get_music.get_music(msg['mid']), path, msg['music'], msg['extension'])
        if msg['lyric'].isChecked():
            fileRW(path, f'{msg["music"]}.txt', 'w', await self.get_music.get_lyrics(msg['mid']))
        self.pgs += 1
        self.progressBar(100 if self.column <= self.pgs else 100 // self.column * self.pgs)

    async def tasks(self):
        """
        任务函数
        查看music_data下一个是否有未被做的任务，如果有就拿过来做
        工作时等待任务执行
        执行完成后查看任务是否被做完，如果做完了则结束该任务函数
        :return: 无任务，结束函数
        """
        while True:
            if self.counter < self.column:
                await self.downloadMusic(self.music_data[self.counter])
            else:
                break

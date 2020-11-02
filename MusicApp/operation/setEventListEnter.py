from operation.method import Method, asyncio
from webbrowser import open


class SetEventListEnter(Method):
    async def onGet(self):
        value = self.ctl_input.text()
        option = self.ctl_option.currentText()
        if value:
            func = None
            if '网址' in option and self.regExp(value, 'http', 'music', 'id'):
                func = self.get_music.get_url
            else:
                try:
                    value = int(value)
                    if '音乐' in option:
                        func = self.get_music.get_song
                    elif '列表' in option:
                        func = self.get_music.get_playlist
                except ValueError:
                    self.popUp(state='InputError')
            if func:
                async for msg in func(value):
                    try:
                        self.addToTable(**msg['msg'])
                        self.progressBar(msg['load'])
                    except TypeError:
                        self.popUp(state=str(msg))
        else:
            text = self.paste()
            if '网址' in option:
                if self.regExp(text, 'http', 'music', 'id'):
                    self.ctl_input.setText(text)
            else:
                try:
                    int(text)
                    self.ctl_input.setText(text)
                except ValueError:
                    ...

    async def onDownloads(self):
        self.pgs = 0
        self.counter = 0
        if self.column:
            self.progressBar(title='开始下载')
            for i in range(self.ctl_maxNumber.value()):
                asyncio.ensure_future(self.tasks())

    @staticmethod
    async def onMore():
        open('https://github.com/Melodyknit/musicapp')

    def onDeletes(self):
        if self.column:
            for i in self.queryList('download', False): self.delete()

    def onPath(self):
        path = self.getDirectory()
        if path:
            self.ctl_path.setText(path)

    def onSelectAll(self, arg__1: bool):
        for i in self.queryList():
            i['lyric'].setChecked(arg__1)
            i['download'].setChecked(arg__1)



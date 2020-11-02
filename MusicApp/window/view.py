from PySide2.QtWidgets import QApplication
from operation.operation import Operation, asyncio
from music163.get_music import GetMusic
from quamash import QEventLoop
import sys


class Window(Operation):
    def __init__(self, loop, parent=None):
        super(Window, self).__init__(parent)
        self.loop = loop
        self.get_music = GetMusic()
        self.setupUi(self)
        self.setConfig()

    def closeEvent(self, event):
        self.closeSaveConfig()
        super(Window, self).closeEvent(event)


class App:
    window: Window = None

    def __init__(self):
        self.app = QApplication(sys.argv)

    def run(self):
        with QEventLoop(self.app) as loop:
            asyncio.set_event_loop(loop)
            self.window = Window(loop)
            self.window.setTrigger()
            self.window.show()
            loop.run_forever()


"pyinstaller -F -w -i icon.ico run.py"




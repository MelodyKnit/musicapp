import aiohttp
from time import localtime, strftime
from json import loads

PLAYLIST = "https://music.163.com/api/playlist/detail?id=%s"  # 获取歌单
MUSIC163 = "http://music.163.com/song/media/outer/url?id=%s"  # 获取音乐
LYRIC = "https://music.163.com/api/song/lyric?id=%s&lv=100"  # 获取歌词
DETAIL = "http://music.163.com/api/song/detail/?id={mid}&ids=%5B{mid}%5D"  # 歌曲信息


class GetMusic:
    status: int = 200

    @staticmethod
    def playtime(timestamp):
        return strftime('%M:%S', localtime(timestamp / 1000))

    def _pack(self, msg, mid: int = None):
        return {'music': msg['name'],
                'artists': '/'.join([i['name'] for i in msg['artists']]),
                'playtime': self.playtime(msg['bMusic']['playTime']),
                'extension': msg['bMusic']['extension'],
                'mid': mid or msg['id']}

    # 获取url进行分析然后调用get_song或get_playlist
    async def get_url(self, url: str):
        for key in self._types:
            if key in url:
                url = url.split('?')[1]
                for i in url.split('&'):
                    if 'id=' in i:
                        mid = int(i.split('id=')[1])
                        async for val in self._types[key](self, mid):
                            yield val

    @classmethod
    def _json(cls, msg, *args):
        try:
            msg = loads(msg)
            for key in args:
                msg = msg[key]
            return msg
        except IndexError and KeyError:
            ...

    # 获取歌曲信息
    async def get_song(self, mid: int):
        try:
            msg = loads(await self.get(DETAIL.format(mid=mid)))['songs'][0]
            yield {'msg': self._pack(msg, mid),
                   'load': 100}
        except KeyError:
            yield self.status
        except IndexError:
            yield 'InputError'

    # 获取音乐
    async def get_music(self, mid: int,):
        return await self.get(MUSIC163 % mid)

    # 获取歌词
    async def get_lyrics(self, mid: int):
        try:
            return loads(await self.get(LYRIC % mid))['lrc']['lyric']
        except KeyError:
            return '未发现歌词'

    # 获取音乐列表生成器
    async def get_playlist(self, mid: int):
        try:
            msg = loads(await self.get(PLAYLIST % mid))['result']['tracks']
            for i, v in enumerate(msg):
                yield {'msg': self._pack(v),
                       'load': 100 // len(msg) * (i + 1)}
        except KeyError:
            yield self.status
        except IndexError:
            yield 'InputError'

    @classmethod
    async def get(cls, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                cls.status = response.status
                return await response.read()

    _types = {
        'song': get_song,
        'playlist': get_playlist
    }


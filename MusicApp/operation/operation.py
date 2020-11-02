from operation.setEventListEnter import SetEventListEnter, asyncio


class Operation(SetEventListEnter):
    # 设置触发器
    def setTrigger(self):
        # 获取按钮被点击时
        @self.onClick(self.ctl_get)
        async def _():
            await self.onGet()

        # 全选按钮被点击时
        @self.onClick(self.ctl_selectAll)
        async def _():
            self.onSelectAll(True)

        # 取消全选按钮被点击时
        @self.onClick(self.ctl_deselectAll)
        async def _():
            self.onSelectAll(False)

        # 输出按钮被点击时
        @self.onClick(self.ctl_deletes)
        async def _():
            self.onDeletes()

        # 下载按钮
        @self.onClick(self.ctl_downloads)
        async def _():
            await self.onDownloads()
            self.counter = 0

        # 更多按钮
        @self.onClick(self.ctl_more)
        async def _():
            await self.onMore()

        # 设置路径按钮
        @self.onClick(self.ctl_setPath)
        async def _():
            self.onPath()



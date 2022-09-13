import pkgutil
from BotEvent import BotEvent
from Plugin import Plugin
__PluginNames__ = [name for _, name,
                   _ in pkgutil.iter_modules(['./plugins']) if name!='HelpMenu']  # 获取插件类的名称
__Plugins__ = []
for name in __PluginNames__:
    exec('from plugins.%s import %s' % (name, name))
    exec('__Plugins__.append(%s())' % (name))  # 将插件加入到列表中


class HelpMenu(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.ans = '当前插件：'
        for i in range(len(__PluginNames__)):
            self.ans += "\n%s: %s" % (__PluginNames__[i],
                                      __Plugins__[i].__doc__)

    def run(self):
        while (True):
            event = self.eventBox.get(block=True)
            param = self.__DecodeCommand__(event)

            if (len(param) > 0 and param[0] == 'help'):
                # self.SendGroupMsg(json['group_id'], self.ans)
                self.PutEvent2Bot(
                    BotEvent('group', event['group_id'], self.ans))

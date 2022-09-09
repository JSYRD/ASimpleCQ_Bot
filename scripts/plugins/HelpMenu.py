import pkgutil
from BotEvent import BotEvent
from Plugin import Plugin
class HelpMenu(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.FunctionNames = [name for _, name, _ in pkgutil.iter_modules(['./plugins'])]
        self.ans = '当前插件：'
        for functionName in self.FunctionNames:
            self.ans+='\n'+functionName
    # def CommandOperate(self, param, json):
    #     if(len(param) > 0 and param[0]=='help'):
    #         self.SendGroupMsg(json['group_id'], self.ans)
    def run(self):
        while(True):
            event = self.eventBox.get(block=True)
            param = self.__DecodeCommand__(event)

            if(len(param) > 0 and param[0]=='help'):
                # self.SendGroupMsg(json['group_id'], self.ans)
                self.PutEvent2Bot(BotEvent('group', event['group_id'], self.ans))
import abc, pkgutil
from BotCommandFunction import BotCommandFunction
import CONFIG
class HelpMenu(BotCommandFunction):
    def __init__(self) -> None:
        super().__init__()
        self.FunctionNames = [name for _, name, _ in pkgutil.iter_modules(['./plugins'])]
        self.ans = '当前插件：'
        for functionName in self.FunctionNames:
            self.ans+='\n'+functionName
    def CommandOperate(self, param, json):
        if(len(param) > 0 and param[0]=='help'):
            self.SendGroupMsg(json['group_id'], self.ans)
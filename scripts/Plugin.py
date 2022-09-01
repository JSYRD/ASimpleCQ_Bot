import abc
import threading
from queue import Queue
from Bot import Bot
from BotEvent import BotEvent
class Plugin(threading.Thread,metaclass = abc.ABCMeta):
    def __init__(self):
        super().__init__()
        self.state = True
        self.eventBox = Queue(maxsize=100)

    @abc.abstractmethod
    def run(self):
        pass
    def __DecodeCommand__(self, json) :
        """
        解码Command，Command格式：
        ```
        commandName param0, param1, ...
        ```
        若非command格式返回空列表。
        """
        if json['post_type'] == 'message' and json['raw_message'][0] == '/':
            if(json['raw_message'][0]=='/'):
                return json['raw_message'][1:].split(' ')
        else:
            return []

    def PutEvent2Bot(self, event: BotEvent):
        Bot.eventBox.put(event)
    
    def TrySwitchState(self, event, pluginName):
        param = self.__DecodeCommand__(event)
        if(len(param) >= 2 and param[0] == pluginName):
            if(param[1] == 'True' or param[1] == 'False'):
                state = True if param[1] == 'True' else False
                self.state = state
                self.PutEvent2Bot(BotEvent('group', event['group_id'], '已成功 %s %s 功能' %('打开' if state==True else '关闭' , pluginName)))
            else:
                self.PutEvent2Bot(BotEvent('group', event['group_id'], '参数错误！\n用法：/%s [state: True or False]' %(pluginName)))

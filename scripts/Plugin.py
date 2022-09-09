import abc
import threading
from queue import Queue
from Bot import Bot
from BotEvent import BotEvent
class Plugin(threading.Thread,metaclass = abc.ABCMeta):
    """
    Plugin类，开发插件只需继承该类并重写`run`函数即可。
    Plugin类内置了两个参数：
    ```python
    self.state = True
    self.eventBox = Queue(maxsize=100)
    ```
    其中state是预留的可以选择是否使用的参数。
    eventBox中存放有新发生的所有事件(json)。

    Plugin类中内置了一个`__DecodeCommand__(self, json)`函数，可以快速解码Command，详情请阅读该函数说明。
    """
    def __init__(self):
        super().__init__()
        self.state = True
        self.eventBox = Queue(maxsize=100)

    @abc.abstractmethod
    def run(self):
        """
        `main.py`在开始运行时会自动调用一次该方法。
        注意仅调用一次。
        """
        pass
    def __DecodeCommand__(self, json) :
        """
        解码Command，Command格式：
        ```
        commandName param0, param1, ...
        ```
        若非command格式返回空列表。\n
        注意返回的param[0]是不带'/'的
        """
        if json['post_type'] == 'message' and json['raw_message'][0] == '/':
            if(json['raw_message'][0]=='/'):
                return json['raw_message'][1:].split(' ')
        else:
            return []

    def PutEvent2Bot(self, event: BotEvent):
        """
        将事件放入Bot.eventBox中。\n
        注意参数event的类型是BotEvent。可以直接使用生成函数实例化，例如:
        ```python
        self.PutEvent2Bot(BoxEvent('group', event['group_id'], '示例'))
        ```
        """
        Bot.eventBox.put(event)
    
    def TrySwitchState(self, event, pluginName):
        """
        切换插件状态函数。参数`pluginName`的类型是`<class str>`
        """
        param = self.__DecodeCommand__(event)
        if(len(param) >= 2 and param[0] == pluginName):
            if(param[1] == 'True' or param[1] == 'False'):
                state = True if param[1] == 'True' else False
                self.state = state
                self.PutEvent2Bot(BotEvent('group', event['group_id'], '已成功 %s %s 功能' %('打开' if state==True else '关闭' , pluginName)))
            else:
                self.PutEvent2Bot(BotEvent('group', event['group_id'], '参数错误！\n用法：/%s [state: True or False]' %(pluginName)))

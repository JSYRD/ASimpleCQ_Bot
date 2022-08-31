from BotCommandFunction import BotCommandFunction
from BotOperatingFunction import BotFunction, BotOperatingFunction
import threading
class Bot(threading.Thread):
    functionObjects = []                                                                #所有插件类的实例
    state = True                                                                        #Bot的state，暂时保留
    def __init__(self, functionNames, functions):
        super().__init__()
        self.functionNames = functionNames
        self.functions = functions
        for functionObject in self.functions:
            self.functionObjects.append(functionObject())                               #初始化插件类的实例并放入列表
    def __DecodeCommand__(self, msg) :
        """
        解码Command，Command格式：
        ```
        commandName param0, param1, ...
        ```
        若非command格式返回空列表。
        """
        if(msg[0]=='/'):
            return msg[1:].split(' ')
        else:
            return []
    def handle(self, json):
        """
        Bot处理新事件，流程为：
        ```python 
        if(self.state == False):    
            pass                    #Bot state，暂时保留
        else:
            for functionObject in self.functionObjects:
                if functionObject.state == True:
                    if(isinstance(functionObject, BotOperatingFunction)):
                        functionObject.FunctionOperate(json)
                if(isinstance(functionObject, BotCommandFunction)):                         #CLI
                    if(json['post_type'] == 'message' and json['raw_message'][0] == '/'):
                        functionObject.CommandOperate(self.__DecodeCommand__(json['raw_message']), json)
        ```
        """
        if(self.state == False):
            pass
        else:
            for functionObject in self.functionObjects:
                if functionObject.state == True:
                    if(isinstance(functionObject, BotOperatingFunction)):
                        functionObject.FunctionOperate(json)
                if(isinstance(functionObject, BotCommandFunction)):                         #CLI
                    if(json['post_type'] == 'message' and json['raw_message'][0] == '/'):
                        functionObject.CommandOperate(self.__DecodeCommand__(json['raw_message']), json)
    def run(self):
        while(True):
            pass

import abc
from BotCommandFunction import BotCommandFunction
from BotOperatingFunction import BotOperatingFunction
import CONFIG
class Echo(BotOperatingFunction, BotCommandFunction):
    """
    自动复读`echoList`中的内容
    ```python
    self.echoList = ['？','?','好好好','111']
    ```
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.echoList = ['？','?','好好好','111']
    def FunctionOperate(self, json, Reserved=None):
        if(json['post_type'] == 'message' and json['raw_message'] in self.echoList):
            # if(json['raw_message'][0] != '/' and json['group_id'] != 732837179):
            #     super().SendGroupMsg(json['group_id'], json['raw_message'])
            self.SendGroupMsg(json['group_id'],json['raw_message'])

    def CommandOperate(self, param, json):
        if(len(param) == 2 and param[0] == 'echo'):
            if(param[1] == 'True' or param[1] == 'False'):
                state = True if param[1] == 'True' else False
                self.state = state
                self.SendGroupMsg(json['group_id'], '已成功%s复读功能' %('打开' if state==True else '关闭'))
            else:
                self.SendGroupMsg(json['group_id'], '参数错误！\n用法：/echo [state]')
import abc
from BotCommandFunction import BotCommandFunction
from BotOperatingFunction import BotOperatingFunction
from datetime import datetime
import requests
import CONFIG

class AntiDrawback(BotCommandFunction, BotOperatingFunction):
    """
    防撤回
    """
    def __init__(self) -> None:
        super().__init__()
    def FunctionOperate(self, json, Reseved = None):
        if(json['post_type'] == 'notice' and json['notice_type'] == 'group_recall'):
            try:
                retJson = requests.get(CONFIG.serverUrl+'get_msg',{'message_id':json['message_id']}).json()
                self.SendGroupMsg(json['group_id'], '%d 在 %s 撤回了 %d 的消息：\n%s' % (json['operator_id'], str(datetime.fromtimestamp(json['time'])), json['user_id'], retJson['data']['message']))
            except:
                raise
    def CommandOperate(self, param, json):
        if(len(param) == 2 and param[0] == 'AntiDrawback'):
            if(param[1] == 'True' or param[1] == 'False'):
                state = True if param[1] == 'True' else False
                self.state = state
                self.SendGroupMsg(json['group_id'], '已成功%s防撤回功能' %('打开' if state==True else '关闭'))
            else:
                self.SendGroupMsg(json['group_id'], '参数错误！\n用法：/AntiDrawback [state]')
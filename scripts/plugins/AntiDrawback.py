from BotEvent import BotEvent
from Plugin import Plugin
from datetime import datetime
import requests
import CONFIG

class AntiDrawback(Plugin):
    """
    防撤回
    """
    def __init__(self) -> None:
        super().__init__()
        # self.state = True
    def run(self):
        while(True):
            event = self.eventBox.get(block=True)
            if(self.state and event['post_type'] == 'notice' and event['notice_type'] == 'group_recall'):
                try:
                    retJson = requests.get(CONFIG.serverUrl+'get_msg',{'message_id':event['message_id']}).json()
                    self.PutEvent2Bot(BotEvent('group', event['group_id'], '%s 在 %s 撤回了 %s 的消息：\n%s' % ("[CQ:at,qq=%d]" % event['operator_id'], str(datetime.fromtimestamp(event['time'])), "[CQ:at,qq=%d]" % event['user_id'], retJson['data']['message'])))
                    # self.SendGroupMsg(event['group_id'], '%d 在 %s 撤回了 %d 的消息：\n%s' % (event['operator_id'], str(datetime.fromtimestamp(event['time'])), event['user_id'], retJson['data']['message']))
                except:
                    raise
            else:
                self.TrySwitchState(event, 'AntiDrawback')

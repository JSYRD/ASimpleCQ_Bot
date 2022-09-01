import threading
from queue import Queue
import requests
from BotEvent import BotEvent
import CONFIG
class Bot(threading.Thread):
    state = True                                                                        #Bot的state，暂时保留
    eventBox = Queue(maxsize=100)
    def __init__(self):
        super().__init__()
    def handle(self, event:BotEvent):
        if(event.eventType == 'group'):
            self.SendGroupMsg(event.id, event.raw_message)
        elif(event.eventType == 'private'):
            self.SendPrivateMsg(event.id, event.raw_message)
    def run(self):
        while(True):
            event = Bot.eventBox.get(block=True)
            self.handle(event)


    def SendPrivateMsg(self, privateId, privateMsg):
        """
        Try send `privateMsg` to `privateId`
        """
        try:
            requests.get(CONFIG.serverUrl+'send_private_msg',{'user_id':privateId, 'message':privateMsg})
        except:
            raise
    def SendGroupMsg(self, groupId, groupMsg):
        """
        Try send `groupMsg` to `groupId`
        """
        try:
            requests.get(CONFIG.serverUrl+'send_group_msg',{'group_id':groupId, 'message':groupMsg})
        except:
            raise

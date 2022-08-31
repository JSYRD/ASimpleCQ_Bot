import abc
import requests
import CONFIG
class BotFunction(metaclass = abc.ABCMeta):
    state = True
    def __init__(self) -> None:
        pass
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
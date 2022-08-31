from re import L
from flask import Flask, request, jsonify
from encodings import utf_8
import requests

# from BotFunction import BotFunction
app = Flask(__name__)
class Bot():

    def __init__(self):
        self.serverUrl = 'http://127.0.0.1:5700/'
        self.testGroupId = '639133624'
        self.echo = True

    def decodeMsg(self, Json):
        qMessage = Json['raw_message']
        if(qMessage[0] == '/'):
            command = qMessage[1:].split(' ')
            if(len(command)!=0):
                if(command[0] == 'help'):
                    self.help_menu(self.testGroupId)
                if(command[0] == 'echo'):
                    print(len(command))
                    if(len(command) == 1 or (command[1]!='True' and command[1]!='False')):
                        self.SendGroupMsg(self.testGroupId, "未知参数，请重试")
                    else:
                        param0 = True if command[1] == 'True' else False
                        self.SwitchFunctions(command[0], param0)
        else:
            self.Echo(self.testGroupId, qMessage)
    def SwitchFunctions(self, functionName, status):
        if(functionName == 'echo'):
            self.echo = status
            if(status == True):
                self.SendGroupMsg(self.testGroupId, "已成功打开复读功能")
            else:
                self.SendGroupMsg(self.testGroupId, "已成功关闭复读功能")
    def Echo(self, groupId, Msg):
        if(self.echo == True):
            self.SendGroupMsg(groupId, Msg)
    def SendPrivateMsg(self, privateId, privateMsg):
        try:
            requests.get(self.serverUrl+'send_private_msg',{'user_id':privateId, 'message':privateMsg})
        except:
            raise
    def SendGroupMsg(self, groupId, groupMsg):
        try:
            requests.get(self.serverUrl+'send_group_msg',{'group_id':groupId, 'message':groupMsg})
        except:
            raise
    def help_menu(self, groupId):
        requests.get(self.serverUrl+'send_group_msg',{'group_id':groupId,'message':'目前功能：\n复读(echo)'})
bot = Bot()

@app.route('/', methods = ["GET","POST"])
def func():
    # if(request.is_json == True):
        # if(request.json['post_type'] == 'message'):  #message
    #         # print(request.json['raw_message'])                // cq raw_message
    #         # print(type(request.json['raw_message']))          // <class 'str'>
    #         if(request.json['raw_message']=="/help"):
    #             help_menu()
    #         else:
    #             requests.get('http://127.0.0.1:5700/send_group_msg',{'group_id':'639133624','message':str(request.json['raw_message'])})
    if(request.json['post_type'] == 'message'):     #记得考虑heartbeat
        if(request.json['group_id'] == 732837179):
            pass
        else:
            bot.decodeMsg(request.json)

    return '114514'

if(__name__ == '__main__'):
    app.run('127.0.0.1', debug = True, port = 5701)
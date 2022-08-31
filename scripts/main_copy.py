from re import L
from flask import Flask, request, jsonify
import json
from encodings import utf_8
import requests
import os, pkgutil
from BotCommandFunction import BotCommandFunction
from BotOperatingFunction import BotFunction, BotOperatingFunction

__FunctionNames__ = [name for _, name, _ in pkgutil.iter_modules(['./plugins'])]
__Functions__ = []
for name in __FunctionNames__:
    exec('from plugins.%s import %s' % (name, name))
    exec('__Functions__.append(%s)' %(name))

app = Flask(__name__)
class Bot():
    functionNames = __FunctionNames__
    functions = __Functions__
    functionObjects = []
    state = True
    def __init__(self):
        for functionObject in self.functions:
            self.functionObjects.append(functionObject())
    def __DecodeCommand__(self, msg) :
        if(msg[0]=='/'):
            return msg[1:].split(' ')
        else:
            return []
    def run(self, json):
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

bot = Bot()

@app.route('/', methods = ["GET","POST"])
def func():
    if(request.json['post_type'] == 'meta_event' and request.json['meta_event_type'] == 'heartbeat'):
    #记得考虑heartbeat
        pass
    else:
        bot.run(request.json)

    return '114514'

if(__name__ == '__main__'):
    app.run('127.0.0.1', debug = True, port = 5701)
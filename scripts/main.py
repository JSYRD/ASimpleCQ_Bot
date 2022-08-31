from re import L
from flask import Flask, request, jsonify
import pkgutil
from Bot import Bot

__FunctionNames__ = [name for _, name, _ in pkgutil.iter_modules(['./plugins'])]        #获取插件类的名称
__Functions__ = []
for name in __FunctionNames__:
    exec('from plugins.%s import %s' % (name, name))                                    
    exec('__Functions__.append(%s)' %(name))                                            #将插件加入到列表中

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def func():
    if(request.json['post_type'] == 'meta_event' and request.json['meta_event_type'] == 'heartbeat'):
    #记得考虑heartbeat
        pass
    else:
        bot.handle(request.json)

    return '114514'

if(__name__ == '__main__'):
    bot = Bot(__FunctionNames__, __Functions__)
    bot.start()
    app.run('127.0.0.1', debug = True, port = 5701)
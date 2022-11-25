# from re import L
# from threading import Thread
from flask import Flask, request
import pkgutil
from Bot import Bot
from PluginsController import PluginsController
import CONFIG

__PluginNames__ = [name for _, name, _ in pkgutil.iter_modules(['./plugins'])]        #获取插件类的名称
__Plugins__ = []
for name in __PluginNames__:
    exec('from plugins.%s import %s' % (name, name))                                    
    exec('__Plugins__.append(%s())' %(name))                                            #将插件加入到列表中

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def SendEvent2Plugins():
    if(request.json['post_type'] == 'meta_event' and request.json['meta_event_type'] == 'heartbeat'):
    #记得考虑heartbeat
        pass
    else:
        pluginsController.PutEvent2plugin(request.json)
        # pass
    return '114514'

if(__name__ == '__main__'):
    bot = Bot()
    bot.start()
    pluginsController = PluginsController(__Plugins__)
    app.run(CONFIG.listeningUrl, debug = False, port = CONFIG.listeningPort, threaded = False)
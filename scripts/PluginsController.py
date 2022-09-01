from queue import Queue
class PluginsController():                  #单例
    def __init__(self, plugins) -> None:
        self.plugins = plugins
        for plugin in self.plugins:
            plugin.start()
    def PutEvent2plugin(self, json):
        for plugin in self.plugins:
            plugin.eventBox.put(json)

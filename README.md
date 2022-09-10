# ASimpleCQ_Bot

**ASimpleCQ_Bot**是基于 [Python Flask](https://github.com/pallets/flask)，使用 cqhttp(如[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)) 实现的简单Bot。通过添加plugin的方式添加功能。

## 食用方法

确保运行`cqhttp`后，将`./scripts/CONFIG.py`中的 相关参数修改为本地对应参数。

```shell
$ python3 main.py
```

即可。



## 添加功能

只需新建python文件，声明一个类并继承Plugin类，重写抽象方法：

```python
from BotEvent import BotEvent
from Plugin import Plugin
def YourPlugin(Plugin):
    def __init__(self):
        super().__init__()
    def run(self):
        while(True):
            #do your things
            
```

将该文件放入`./scripts/plugins ` 中并重新运行即可。
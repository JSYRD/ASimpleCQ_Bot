from BotEvent import BotEvent
from Plugin import Plugin
class Echo(Plugin):
    """
    自动复读`echoList`中的内容
    ```python
    self.echoList = ['？','?','好好好','111']
    ```
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.echoList = ['？','?','好好好','111']
        # self.state = True
    def run(self):
        while(True):
            event = self.eventBox.get(block=True)
            if(self.state and event['post_type'] == 'message' and event['raw_message'] in self.echoList):
                self.PutEvent2Bot(BotEvent('group', event['group_id'], event['raw_message']))
            else:
                self.TrySwitchState(event, 'echo')
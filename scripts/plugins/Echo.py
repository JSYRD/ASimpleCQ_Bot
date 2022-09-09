from enum import Enum
from BotEvent import BotEvent
from Plugin import Plugin
from datetime import datetime

SLEEP_SECONDS = 60


class GameState(Enum):
    preparing = "preparing"
    gaming = "gaming"


class Echo(Plugin):
    """
    自动复读`echoList`中的内容
    ```python
    self.echoList = ['？','?','好好好','111']
    ```

    """

    def __init__(self) -> None:
        super().__init__()
        self.echoList = ["？", "?", "好好好", "111"]
        # self.state = True
        self.last_msg_datetime = 0

    def run(self):
        while True:
            event = self.eventBox.get(block=True)
            if (
                self.state
                and event["post_type"] == "message"
                and event["raw_message"] in self.echoList
            ):
                now_datetime = datetime.now().timestamp()
                seconds_elapsed = now_datetime - self.last_msg_datetime
                if seconds_elapsed < SLEEP_SECONDS:
                    continue
                self.last_msg_datetime = now_datetime
                self.PutEvent2Bot(
                    BotEvent("group", event["group_id"], event["raw_message"])
                )
            else:
                self.TrySwitchState(event, "echo")

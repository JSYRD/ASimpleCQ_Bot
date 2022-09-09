class BotEvent():
    """
    Bot的事件类型。包含三个参数
    ```python
    def __init__(self, eventType: str, id: int, raw_message: str) -> None
    """
    def __init__(self, eventType, id, raw_message) -> None:
        self.eventType = eventType
        self.id = id
        self.raw_message = raw_message
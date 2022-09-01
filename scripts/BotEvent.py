class BotEvent():
    def __init__(self, eventType, id, raw_message) -> None:
        self.eventType = eventType
        self.id = id
        self.raw_message = raw_message
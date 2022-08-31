import abc
from BotFunction import BotFunction
class BotCommandFunction(BotFunction):
    def __init__(self) -> None:
        pass
    @abc.abstractmethod
    def CommandOperate(self, param, json):
        """
        Operate with `param`
        """
        pass
import abc
import requests
from BotFunction import BotFunction
import CONFIG
class BotOperatingFunction(BotFunction):
    def __init__(self) -> None:
        pass
    @abc.abstractmethod
    def FunctionOperate(self, Json, Reserved = None):
        """
        Function operates.
        """
        pass
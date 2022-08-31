import abc
from enum import Enum
from BotCommandFunction import BotCommandFunction
import sqlite3
dictConn = sqlite3.connect('./plugins/Databases/dictDatabase.db')
dictCur = dictConn.cursor()
balanceConn = sqlite3.connect('./plugins/Databases/userBalance.db')
balanceCur = balanceConn.cursor()
class GameState(Enum):
    preparing = 'preparing'
    gaming = 'gaming'
class MiniGame(BotCommandFunction):
    def __init__(self) -> None:
        super().__init__()
        self.state = GameState.preparing
    def CommandOperate(self, param, json):
        if(self.state == GameState.preparing):
            if(len(param) > 0 and param[0] == 'minigame'):
                if(len(param) == 2 and param[1] == '成语接龙'):
                    pass
        elif(self.state == GameState.gaming):
            pass

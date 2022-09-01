from enum import Enum
from BotEvent import BotEvent
from Plugin import Plugin
import sqlite3
from atexit import register
N = 30895
# dictConn = sqlite3.connect('./plugins/Databases/dictDatabase.db')
# dictCur = dictConn.cursor()
# balanceConn = sqlite3.connect('./plugins/Databases/userBalance.db')
# balanceCur = balanceConn.cursor()
class GameState(Enum):
    preparing = 'preparing'
    gaming = 'gaming'
class MiniGame(Plugin):
    """
    小游戏
    """
    def __init__(self):
        super().__init__()
        self.state = True
        self.gameState = GameState.preparing
        self.currentDict = ''
        self.dictConn = sqlite3.connect('./plugins/Databases/dictDatabase.db', check_same_thread=False)
        self.dictCur = self.dictConn.cursor()
        self.balanceConn = sqlite3.connect('./plugins/Databases/userBalance.db', check_same_thread=False)
        self.balanceCur = self.balanceConn.cursor()
    def run(self):
        while(True):
            event = self.eventBox.get(block=True)
            if((not self.state) or event['post_type'] != 'message'):
                pass
            else:
                if(self.gameState == GameState.preparing):
                    param = self.__DecodeCommand__(event)
                    if(len(param) == 2 and param[0] == 'game' and param[1] == '成语接龙'):
                        self.gameState = GameState.gaming
                        self.dictCur.execute('select * from (select a.dict from  dicts a  where substr(a.dict,length(a.dict),1) in (select substr(dict,1,1) last from dicts)) as a order by random() limit 1;')
                        self.currentDict = '一个顶俩'
                        for dict in self.dictCur:
                            self.currentDict = dict[0]
                        self.PutEvent2Bot(BotEvent('group', event['group_id'], '成语接龙开始，所有病友均可参加。\n第一个词汇：%s' %(self.currentDict)))
                elif(self.gameState == GameState.gaming):
                    param = self.__DecodeCommand__(event)
                    if(len(param) == 2 and param[0] == 'game' and param[1] == 'stop'):
                        self.gameState = GameState.preparing
                        self.PutEvent2Bot(BotEvent('group', event['group_id'], '游戏停止。'))
                    raw_message = event['raw_message']
                    self.dictCur.execute("select count(*) from dicts where dict = '%s';" %(raw_message))
                    count = 0
                    for _ in self.dictCur:
                        count = _[0]
                    if(count != 0 and raw_message[0]==self.currentDict[-1]):
                        self.currentDict = raw_message
                        self.PutEvent2Bot(BotEvent('group', event['group_id'], '恭喜%d接龙成功，当前词汇：%s' %(event['user_id'], raw_message)))
                    
                    self.dictCur.execute("select count(*) from dicts where dict like '"+self.currentDict[-1]+"%';")
                    count = 0
                    for _ in self.dictCur:
                        count = _[0]
                    if(count == 0):
                        self.gameState = GameState.preparing
                        self.PutEvent2Bot(BotEvent('group', event['group_id'], '当前成语：%s,已经没有其他成语可以接龙，游戏结束。'%(self.currentDict)))

# @register
# def _atexit():
#     dictConn.commit()
#     dictConn.close()
#     dictCur.close()
#     balanceConn.commit()
#     balanceConn.close()
#     balanceCur.close()


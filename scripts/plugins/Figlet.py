import optparse
from BotEvent import BotEvent
from Plugin import Plugin
from optparse import OptionParser
from pyfiglet import Figlet as F
from PIL import Image, ImageDraw, ImageFont
# import Image, ImageDraw, ImageFont

class MyOptionParser(OptionParser):
    # def __init__(self, usage, option_list, option_class, version, conflict_handler, description, formatter, add_help_option, prog, epilog, plugin) -> None:
    #     super().__init__(usage, option_list, option_class, version, conflict_handler, description, formatter, add_help_option, prog, epilog)
    #     self.plugin = plugin
    def exit(self, status=0, msg=None):  #error会调用，help会调用(NULL)
        # self.plugin.PutEvent2Bot(BotEvent(eventType="group",id=event["group_id"],raw_message = Figlet.parser.format_help()))
        pass
    def error(self, msg):
        #error调用，说明此时有错误发生，应该exit(假)
        Figlet.errorno = 1
        self.exit()
        pass

class Figlet(Plugin):
    parser = MyOptionParser(
    prog='/figlet',
    usage="%prog [OPTIONS] [ASCII CHARS TEXT]",
    description = "Figlet插件 将ASCII字符转换为炫酷字体",
    # formatter=NoWrapFormatter()
    )
    errorno = 0
    def __init__(self):
        super().__init__()
        Figlet.parser.add_option("-f", "--font", action="store", help="指定字体", default="standard")
        Figlet.parser.add_option("-e", "--example", action="store_true", help="随机展示部分字体样例")

    def run(self):
        while True:
            event = self.eventBox.get(block=True)
            if(
                event["post_type"] == "message"
            ):
                params = self.__DecodeCommand__(event)
                if(params and params[0]=='figlet'):
                    options, args = self.parser.parse_args(params[1:])
                    if(len(args) == 0 or Figlet.errorno !=0 ):
                        self.PutEvent2Bot(BotEvent(eventType="group",id=event["group_id"],raw_message = Figlet.parser.format_help()))
                        Figlet.errorno = 0
                    elif(options.example):
                        pass
                    else:
                        f = F(font=options.font)
                        self.PutEvent2Bot(BotEvent(eventType="group",id=event["group_id"],raw_message = f.renderText(' '.join(args))))

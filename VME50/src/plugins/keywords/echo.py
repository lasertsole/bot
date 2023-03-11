from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent,Bot

def echo():
    def _checker(event:GroupMessageEvent) ->bool :
        return event.to_me

    introduce_self=on_keyword({"你是谁","介绍你一下你自己"},rule=_checker)
    @introduce_self.handle()
    async def _(bot: Bot,event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await introduce_self.finish(Message(f"[CQ:at,qq={event.user_id}] 我是你的女仆，主人"))
        else:
            await introduce_self.finish(Message(f"[CQ:at,qq={event.user_id}] 我叫MOYA，服役于MOYE的自动人形鲨式VME50，编号(同时也是通讯号码)为"+bot.self_id+",先生"))
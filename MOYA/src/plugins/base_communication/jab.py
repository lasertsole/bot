from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, MessageSegment

def jab():#戳一戳事件
    def _check(event: PokeNotifyEvent):#event:PokeNotifyEvent限定必须是戳一戳事件
        return event.target_id == event.self_id
    
    poke=on_notice(rule=_check)
    @poke.handle()
    async def _(event:PokeNotifyEvent):
        if(event.user_id==3132225629):
            await poke.finish(MessageSegment.image(file=r"images/happy.gif"))
        else:
            await poke.finish(MessageSegment.image(file=r"images/startle.jpg"))
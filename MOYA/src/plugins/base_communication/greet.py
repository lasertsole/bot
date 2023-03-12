from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent, MessageSegment

def greet():
    def _checker(event:GroupMessageEvent) ->bool :#过滤at bot的信息
        return event.to_me
    
    ##################早安##################
    morning=on_keyword({"早安MOYA","MOYA早安"})
    @morning.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await morning.finish(Message("早安主人"))
        else:
            await morning.finish(Message("早安先生"))

    atMorning=on_keyword({"早安"},rule=_checker)
    @atMorning.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atMorning.finish(Message("早安主人"))
        else:
            await atMorning.finish(Message("早安先生"))

    ##################早上好##################
    good_morning=on_keyword({"早上好MOYA","MOYA早上好"})
    @good_morning.handle()
    async def _(event: GroupMessageEvent):
        if(event.user_id==3132225629):
            await good_morning.finish(Message("早上好主人"))
        else:
            await morning.finish(Message("早上好先生"))

    atGood_morning=on_keyword({"早上好"},rule=_checker)
    @atGood_morning.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atGood_morning.finish(Message("早上好主人"))
        else:
            await atGood_morning.finish(Message("早上好先生"))

    ##################中午好##################
    good_noon=on_keyword({"中午好MOYA","MOYA中午好"})
    @good_noon.handle()
    async def _(event: GroupMessageEvent):
        if(event.user_id==3132225629):
            await good_noon.finish(Message("中午好主人"))
        else:
            await morning.finish(Message("中午好先生"))
    
    atGood_noon=on_keyword({"中午好"},rule=_checker)
    @atGood_noon.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atGood_noon.finish(Message("中午好主人"))
        else:
            await atGood_noon.finish(Message("中午好先生"))

    ##################下午好##################
    good_afternoon=on_keyword({"下午好MOYA","MOYA下午好"})
    @good_afternoon.handle()
    async def _(event: GroupMessageEvent):
        if(event.user_id==3132225629):
            await good_afternoon.finish(Message("下午好主人"))
        else:
            await morning.finish(Message("下午好先生"))

    atGood_afternoon=on_keyword({"下午好"},rule=_checker)
    @atGood_afternoon.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atGood_afternoon.finish(Message("下午好主人"))
        else:
            await atGood_afternoon.finish(Message("下午好先生"))

    ##################晚上好##################
    good_evening=on_keyword({"晚上好MOYA","MOYA晚上好"})
    @good_evening.handle()
    async def _(event: GroupMessageEvent):
        if(event.user_id==3132225629):
            await good_evening.finish(Message("晚上好主人"))
        else:
            await morning.finish(Message("晚上好先生"))

    atGood_evening=on_keyword({"晚上好"},rule=_checker)
    @atGood_evening.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atGood_evening.finish(Message("晚上好主人"))
        else:
            await atGood_evening.finish(Message("晚上好先生"))

    ##################晚安##################
    good_night=on_keyword({"晚安MOYA","MOYA晚安"})
    @good_night.handle()
    async def _(event: GroupMessageEvent):
        if(event.user_id==3132225629):
            await good_night.finish(Message("晚安主人"))
        else:
            await morning.finish(Message("晚安先生"))

    atGood_night=on_keyword({"晚安"},rule=_checker)
    @atGood_night.handle()
    async def _(event: GroupMessageEvent):#空名函数，用于异步
        if(event.user_id==3132225629):
            await atGood_night.finish(Message("晚安主人"))
        else:
            await atGood_night.finish(Message("晚安先生"))
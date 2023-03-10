from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message

word=on_keyword({"呼叫MOYA"})

@word.handle()
async def _():
    await word.finish(Message("在的，我的主人"))
import orm
import asyncio
from models import User
async def test(loop,**kw):
    await orm.create_pool(loop=loop,user='root', password='root', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await orm.destory_pool()
    
data=dict(name='h3e', email='heru33i@qq.com', passwd='13133345', image='about:blank')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()



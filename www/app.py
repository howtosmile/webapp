import logging
logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>hello</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '115.29.33.91', 9000)
    logging.info('server started at http://115.29.33.91:9000...')
    return srv

loop = asyncio.get_event_loop()
print('first loop: %s' % (str(type(loop))))
loop.run_until_complete(init(loop))
print('second loop: %s' % (str(type(loop))))
loop.run_forever()

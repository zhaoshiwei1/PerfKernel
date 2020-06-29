import gevent
from gevent import monkey; monkey.patch_all()
from http_utils import HttpSession
from limitor import TokenBucket

headers = {
    'User-Agent': 'Xueqiu iPhone 11.8',
    'accept': 'application/json',
    'ept-language': 'zh-Hans-CN;q=1',
    'accept-encoding': 'br, gzip, deflate',
    'Cookie': 'u=1767539047; xq_a_token=26c5753ad9310c1d3e11d9c22ce1769b5263cec5'
}

client = HttpSession("")

bucket = TokenBucket()


def f():
    if bucket.consume(200, 1):
        client.request(method='GET',
                       url='http://10.10.21.27:8080/v5/stock/quote.json?symbol=SH000001&extend=detail',
                       name='health_check',
                       headers=headers)


def d():
    print("method: d")


task = []

task += [f for x in range(0, 9999)]

for func in task:
    print(type(func))

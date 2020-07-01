import gevent
from gevent import monkey; monkey.patch_all()
from http_utils import HttpSession
from limitor import TokenBucket
import time
import requests

headers = {
    'User-Agent': 'Xueqiu iPhone 11.8',
    'accept': 'application/json',
    'ept-language': 'zh-Hans-CN;q=1',
    'accept-encoding': 'br, gzip, deflate',
    'Cookie': 'u=1767539047; xq_a_token=26c5753ad9310c1d3e11d9c22ce1769b5263cec5'
}

client = HttpSession("")

# bucket = TokenBucket()
#
# time.sleep(1)


def single_attack():
    client.request(method='GET',
                   url='http://10.10.21.27:8080/v5/stock/quote.json?symbol=SH000001&extend=detail',
                   name='health_check',
                   headers=headers)


def ref_attack():
    requests.get(url='http://10.10.21.27:8080/v5/stock/quote.json?symbol=SH000001&extend=detail', headers=headers)


def group_attack(rate):
    single_greenlet = [gevent.spawn(ref_attack) for i in range(0, rate)]
    gevent.joinall(single_greenlet)


def concurrency(num, rate):
    greenlet = [gevent.spawn(group_attack, rate) for i in range(0, num)]
    gevent.joinall(greenlet)


t1 = time.time()
concurrency(2, 1000)
t2 = time.time()
print(t2 - t1)

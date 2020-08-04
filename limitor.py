import time


class TokenBucket(object):

    def __init__(self):
        self._current_amount = 0
        self._last_consume_time = int(time.time())

    # rate: token下发的速度
    # token_amount：每次获取的token的数量，建议token_amount根据rate数量变化，减少consume调用次数，节省CPU
    def consume(self, rate, token_amount):
        self._rate = rate
        self._capacity = 10 ** len(str(rate))

        increment = (int(time.time()) - self._last_consume_time) * self._rate  # 计算从上次发送到这次发送，新发放的令牌数量
        self._current_amount = min(increment + self._current_amount, self._capacity)  # 令牌数量不能超过桶的容量
        if token_amount > self._current_amount:  # 如果没有足够的令牌，则不能发送数据
            return False
        self._last_consume_time = int(time.time())
        self._current_amount -= token_amount
        return True

import gevent
from gevent import monkey; monkey.patch_all()
from http_utils import HttpSession
import random
from stats import global_stats, print_stats

statistics = global_stats
main_greenlet = []


def worker():
    def runner():
        client = HttpSession("http://127.0.0.1:8080")
        url_template = "/calculate?a={}&b={}"
        while True:
            url_parsed = url_template.format(random.randint(0, 100), random.randint(0, 100))
            client.request(method="get", url=url_parsed, name="/calculate")

    def stats_printer():
        while True:
            print("-" * 80)
            # print_stats(statistics)
            gevent.sleep(3)

    g_list = [gevent.spawn(runner) for i in range(0, 20)]
    g_list.append(gevent.spawn(stats_printer))

    gevent.joinall(g_list)


worker()

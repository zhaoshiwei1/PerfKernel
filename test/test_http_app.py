import web
import time
import random
import json
urls = (
    '/calculate', 'Foo'
)


class Foo:
    def GET(self):
        print(web.input().keys())
        a = int(web.input().a)
        b = int(web.input().b)
        seed = random.randint(5, 10)
        time.sleep(5)
        print(seed)
        result = {"result": a+b}
        return json.dumps(result)

    def POST(self):
        print(web.input().keys())
        a = int(web.input().a)
        b = int(web.input().b)
        return a-b

    def DELETE(self):
        print(web.input().keys())
        a = int(web.input().a)
        b = int(web.input().b)
        return a*b


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

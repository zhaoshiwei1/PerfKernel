import web

urls = (
    '/calculate', 'Foo'
)


class Foo:
    def GET(self):
        # print(web.input().keys())
        a = int(web.input().a)
        b = int(web.input().b)
        return a+b

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

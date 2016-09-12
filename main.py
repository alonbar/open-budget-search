import elastic
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class SearchHandler(tornado.web.RequestHandler):
    def get(self, search_term):
        self.write("Hello, %s" % search_term)


class IndexDocumentHandler(tornado.web.RequestHandler):
    def post(self, type_name):
        data = tornado.escape.json_decode(self.request.body)
        elastic.index_doc(type_name, data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search/(?P<search_term>[^\/]+)", SearchHandler),
        (r"/index/(?P<type_name>[^\/]+)", IndexDocumentHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
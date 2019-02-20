import falcon
import app.util.json as json
from falcon_jinja2 import FalconTemplate
falcon_template = FalconTemplate()


class RootResources(object):
    @falcon_template.render('index.html')
    def on_get(self, req, resp):
        #resp.body = json.dumps({
        #    "message": "Hello, World!",
        #})

        resp.context = {'framework': 'Falcon'}


class RootNameResources(object):
    def on_post(self, req, resp, name):
        resp.body = json.dumps({
            "message": "Hello, {}!".format(name.capitalize())
        })

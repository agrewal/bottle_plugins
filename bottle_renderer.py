from functools import wraps
from os.path import splitext
from bottle import request, response, template as simple_template, mako_template, cheetah_template, jinja2_template, simpletal_template
from json import dumps

def json_renderer(resp):
    response.content_type = 'application/json'
    return dumps(resp)

def string_renderer(resp):
    response.content_type = 'text/plain'
    if not isinstance(resp, basestring):
        resp = str(resp)
    return resp

def simple_renderer(template, resp):
    return simple_template(template, resp)

def mako_renderer(template, resp):
    return mako_template(template, resp)

def jinja2_renderer(template, resp):
    return jinja2_template(template, resp)

def cheetah_renderer(template, resp):
    return cheetah_template(template, resp)

def simpletal_renderer(template, resp):
    return simpletal_template(template, resp)

class RendererPlugin(object):
    name = 'renderer'

    def __init__(self, template_context=None):
        self._renderers = {}
        self._renderers['json'] = json_renderer
        self._renderers['string'] = string_renderer
        self._renderers['.stpl'] = simple_renderer
        self._renderers['.mako'] = mako_renderer
        self._renderers['.jinja2'] = jinja2_renderer
        self._renderers['.cheetah'] = cheetah_renderer
        self._renderers['.simpletal'] = simpletal_renderer
        if template_context is None:
            self.template_context = {}
        elif isinstance(template_context, dict):
            self.template_context = template_context
        else:
            raise Exception('template_context must be a dict')

    def add_renderer(self, name, renderer):
        if callable(renderer):
            self._renderers[name] = renderer
        else:
            raise Exception('Renderer must be callable')

    def apply(self, callback, context):
        renderer = context['config'].get('renderer')
        if renderer is None or not isinstance(renderer, basestring):
            return callback
        _, ext = splitext(renderer)
        if (ext == '' and renderer not in self._renderers) or (ext != '' and ext not in self._renderers):
            return callback

        @wraps(callback)
        def wrapper(*args, **kwargs):
            rv = callback(*args, **kwargs)
            if ext == '':
                return self._renderers[renderer](rv)
            else:
                self.template_context.update({
                    'R': rv,
                    'app': context['app'],
                    'request': request,
                    'response': response
                })
                return self._renderers[ext](renderer, self.template_context)
        return wrapper

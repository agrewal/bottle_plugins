bottle_renderer
===============

This plugin allows you to specify a renderer for per route. Here is an example

::

    from bottle import Bottle
    from bottle_renderer import RendererPlugin

    app = Bottle()
    renderer = RendererPlugin(template_context = {'FB_APP_ID': 1234}) # This will be available in templates

    # You can override the renderers by specifying your own.
    # renderer.add_renderer('json', your_json_renderer)

    app.install(renderer)
    app.uninstall('json') # no autojson

    # to use in a route, just specify the "renderer" attribute
    @app.get('/main', name='main', renderer='main.jinja2')
    def get_main():
        # do something
        return ret_value


In your templates (jinja2, mako, etc.)  you can access the following by default:

:R: return value of the function
:app:  The current app
:request: The current request
:response: The current response

The following renderers are available:

::

    @app.get(renderer='json', ..) # Renders return value as json
    @app.get(renderer='string', ..) # Renders return value as text/plain
    @app.get(renderer='<template_filename>.stpl', ..) # simple 
    @app.get(renderer='<template_filename>.mako', ..) 
    @app.get(renderer='<template_filename>.jinja2', ..) 
    @app.get(renderer='<template_filename>.cheetah', ..) 
    @app.get(renderer='<template_filename>.simpletal', ..)

Here are a couple of plugins I wrote `bottle web framework <https://github.com/defnull/bottle>`_. Tested somewhat. Use at own risk :-)

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

R : return value of the function
app : The current app
request: The current request
response: The current response


bottle_flash
============

This plugin enables flash messages in bottle. Again, learn by example

::
    from bottle import Bottle
    from bottle_flash import FlashPlugin

    app = Bottle()
    COOKIE_SECRET = 'super_secret_string'
    app.install(FlashPlugin(secret=COOKIE_SECRET))

    app.post('/create_user')
    def create_user():
        # Create the user
        app.flash('Created !')

To consume the flashed messages, you would do something like the following (jinja2). Here I am assuming that I get the "app" in the template context. This can be achieved with the bottle_renderer_ plugin.

::
    {% set messages = app.get_flashed_messages() %}
    {% if messages %}
    <div id="flash_messages">
        <ul>
            {% for m in messages %}
            <li>{{ m[0] }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}

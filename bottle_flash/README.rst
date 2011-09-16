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

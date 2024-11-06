#!/usr/bin/env python3
""" Then instantiate the Babel object in your app. Store it in
a module-level variable named babel.

In order to configure available languages in our app, you will
create a Config class that has a LANGUAGES class attribute equal
to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz


class Config:
    """Flask config class. Config class that has a
    LANGUAGES class attribute equal to ["en", "fr"].
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = pytz.utc


app = Flask(__name__, template_folder="templates")

app.config.from_object(Config)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


# Create a get_locale function with the babel.localeselector
# decorator. Use request.accept_languages to determine the best
# match with our supported languages.

@babel.localeselector
def get_locale():
    """Use request.accept_languages to determine the best
    match with our supported languages.

    detect if the incoming request contains locale argument and
    ifs value is a supported locale, return it. If not or if the
    parameter is not present, resort to the previous default behavior.
    """

    locale = request.args.get('locale')
    # check if locale is None
    if locale in app.config['LANGUAGES']:
        return locale

    # fall back to default
    return app.config['BABEL_DEFAULT_LOCALE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """that returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed.
    """
    user = request.args.get('login_as')

    if user:
        user_key = users.get(int(user))
        return user_key

    return None


@app.before_request
def before_request():
    """make it be executed before all other functions.
    before_request should use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ home route that handles a get request on the hompage
    also renders the template
    """
    return render_template("5-index.html", user=g.user)


if __name__ == '__main__':
    app.run(debug=True)

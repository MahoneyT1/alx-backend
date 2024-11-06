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


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ home route that handles a get request on the hompage
    also renders the template
    """
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)

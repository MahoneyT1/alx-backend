#!/usr/bin/env python3
""" Then instantiate the Babel object in your app. Store it in
a module-level variable named babel.

In order to configure available languages in our app, you will
create a Config class that has a LANGUAGES class attribute equal
to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel
import pytz

app = Flask(__name__, template_folder="templates")


class Config:
    """Flask config class. Config class that has a
    LANGUAGES class attribute equal to ["en", "fr"].
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = pytz.utc


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ home route that handles a get request on the hompage
    also renders the template
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)

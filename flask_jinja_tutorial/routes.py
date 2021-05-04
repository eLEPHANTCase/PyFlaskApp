"""Route Declaration."""

from flask import current_app as app
from flask import render_template

@app.route("/")
def home():
    """Landing Page"""
    nav = [
        {"name": "Home", "url", "http://github.com/"},
        {"name": "Home", "url", "http://reddit.com/"}
    {"name": "Pics", "url", "https://www.xampp.com/"}
    ]
    return render_template(
        "home.html",
        title="Jinja Demo Site",
        description="Smarter Page Templates with Flask & Jinja"
    )


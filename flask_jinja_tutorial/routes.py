"""Route Declaration."""

from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import ContactForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `Contact` Form"""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
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


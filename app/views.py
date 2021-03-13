from flask import Blueprint, render_template

bp = Blueprint("bp", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/login")
def login():
    return "hi"
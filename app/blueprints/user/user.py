from flask import Blueprint, render_template
from ...models import db

user_bp = Blueprint("user_bp", __name__, template_folder="templates")

@user_bp.route("/")
def user_index():
    return render_template("user/index.html")
from flask import Flask
from .models import db
from .views import bp
from .blueprints import user_bp

app = Flask(__name__)
app.register_blueprint(bp)
app.register_blueprint(user_bp, url_prefix="/user")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()
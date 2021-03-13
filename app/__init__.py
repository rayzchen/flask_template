from flask import Flask
from .models import db
from .views import bp

app = Flask(__name__)
app.register_blueprint(bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()
import os
from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv

mail = Mail()

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 465))
    app.config["MAIL_USE_SSL"] = os.getenv("MAIL_USE_SSL", "True") == "True"
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
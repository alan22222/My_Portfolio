from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'supersecret123'

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = "alanchacko42@gmail.com"
    app.config["MAIL_PASSWORD"] = "sjvoychbglsuxpxx"

    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
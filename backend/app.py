from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from routers import auth, dashboard, routes
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from core.config import APP_CONFIG
from db.database import db

ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG)
    app.json.sort_keys = False

    db.init_app(app)

    ma.init_app(app)
    JWTManager(app)

    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    script_name = APP_CONFIG.BASE_URL
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {script_name: app})

    @app.route("/")
    def app_info():
        info_data = {"name": f"keycloak-test"}
        return jsonify(info_data), 200

    return app


app = create_app()

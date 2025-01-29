from flask import Blueprint, redirect, url_for, request, session
from core.keycloak_client import keycloak_openid
from models.user import User
from db.database import db
import logging


bp = Blueprint('auth', __name__, url_prefix='/auth')

logger = logging.getLogger(__name__)


@bp.route("/login")
def login():
    auth_url = keycloak_openid.auth_url(redirect_uri=url_for("auth.callback", _external=True))
    logger.info("Redirecting user to Keycloak for authentication.")
    return redirect(auth_url)

@bp.route("/callback")
def callback():
    code = request.args.get("code")
    try:
        token = keycloak_openid.token(grant_type='authorization_code',
                                     code=code,
                                     redirect_uri=url_for("auth.callback", _external=True))
        user_info = keycloak_openid.userinfo(token['access_token'])

        session['user_info'] = user_info
        email = user_info.get('email')

        if email:
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(email=email)
                db.session.add(user)
                db.session.commit()
                logger.info(f"New user registered: {email}")
            logger.info(f"User {email} logged in successfully.")
        return redirect(url_for("dashboard.dashboard"))
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return "Login failed", 401

@bp.route("/logout")
def logout():
    session.clear()
    logger.info("User logged out successfully.")
    return redirect(url_for("index"))

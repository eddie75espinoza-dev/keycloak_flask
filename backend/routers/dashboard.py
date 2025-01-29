from flask import Blueprint, session, redirect, url_for


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route("/dashboard")
def dashboard():
    if "user_info" not in session:
        return redirect(url_for("auth.login"))
    return f"Welcome, {session['user_info']['email']}!"

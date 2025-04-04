from flask import Blueprint, render_template
from redis_client import redis_client

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_bp.route("/dashboard")
def dashboard():
    keys = redis_client.keys("rate_limit:*")
    data = {}
    for key in keys:
        ip = key.split(":")[1]
        count = redis_client.zcard(key)
        data[ip] = count
    return render_template("dashboard.html", data=data)
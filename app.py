from flask import Flask, request, jsonify
from limiter import RateLimiter
from dashboard import dashboard_bp

app = Flask(__name__)
app.register_blueprint(dashboard_bp)

rate_limiter = RateLimiter(max_requests=5, window_seconds=60)  # 5 requests per minute

@app.route("/api/data")
def api_data():
    user_ip = request.remote_addr
    if rate_limiter.is_allowed(user_ip):
        return jsonify({"message": "Success! Here's your data."})
    return jsonify({"error": "Rate limit exceeded. Try later."}), 429

if __name__ == "__main__":
    app.run(debug=True)
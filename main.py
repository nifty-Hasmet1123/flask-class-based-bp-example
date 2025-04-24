"""
REGISTERED ROUTES:
    - http://127.0.0.1:5000/api/user
"""

from user.views import user_bp
from flask import Flask


app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
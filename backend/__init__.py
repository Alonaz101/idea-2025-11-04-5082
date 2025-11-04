from flask import Flask
from .app import app as app_main
from .user_auth import user_auth

app = Flask(__name__)

# Register blueprints
app.register_blueprint(user_auth)
app.register_blueprint(app_main)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

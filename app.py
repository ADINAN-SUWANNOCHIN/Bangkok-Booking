import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'main.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.errorhandler(404)
def handle_404(e):
    # Return main.html for any 404 to enable SPA routing or fallback
    return send_from_directory(app.static_folder, 'main.html'), 404

if __name__ == '__main__':
    try:
        port = int(os.getenv("PORT", 8000))  # Azure จะกำหนด PORT ผ่าน environment variable นี้
        print(f"Starting server on port {port}...")
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error starting the server: {e}")

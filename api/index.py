import os
import re
import time
import json
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

# -------------------------
# CONFIG
# -------------------------
TARGET_BASE = os.getenv("TARGET_BASE", "https://example.com")  # Replace if needed
API_KEY = "mynkapi"  # your static key
COPYRIGHT = "👉🏻 @mynk_mynk_mynk"

# -------------------------
# HOME
# -------------------------
@app.route('/')
def home():
    return f"<h2>🇵🇰 Pakistan Number/CNIC Info API - Live Mode</h2><br><small>{COPYRIGHT}</small>"

# -------------------------
# HEALTH CHECK
# -------------------------
@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "allow_upstream": True,
        "copyright": COPYRIGHT
    })

# -------------------------
# LOOKUP ENDPOINT
# -------------------------
@app.route('/api/lookup')
def lookup():
    key = request.args.get("key")
    query = request.args.get("query")
    pretty = request.args.get("pretty")

    if key != API_KEY:
        return jsonify({"error": "Invalid API key", "copyright": COPYRIGHT}), 403

    if not query:
        return jsonify({"error": "Missing 'query' parameter", "copyright": COPYRIGHT}), 400

    # Determine query type
    query_type = "mobile" if re.match(r'^(92|03)\d{9}$', query) else "cnic"

    # Simulated lookup (replace this with your real scraping/requests logic)
    results = {
        "query": query,
        "query_type": query_type,
        "results_count": 1,
        "results": [
            {"name": "Demo Name", "city": "Karachi", "status": "Active"}
        ],
        "copyright": COPYRIGHT
    }

    if pretty == "1":
        return app.response_class(
            response=json.dumps(results, indent=2, ensure_ascii=False),
            mimetype='application/json'
        )
    return jsonify(results)

# -------------------------
# MAIN
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, Response
import requests, sys

app = Flask(__name__)

# 🌐 Target Streamlit Cloud app
TARGET = "https://kiosc-agent-app-csmqytqwhfcjow5zxzhyb6.streamlit.app"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(path):
    # Forward to Streamlit app directly
    if path == "":
        url = TARGET
    else:
        url = f"{TARGET}/{path}"

    if request.query_string:
        url = f"{url}?{request.query_string.decode('utf-8')}"

    print(f"➡️ Forwarding request to: {url}", file=sys.stderr)

    try:
        resp = requests.get(url, stream=True, allow_redirects=True, timeout=15)
    except Exception as e:
        return f"❌ Proxy error: {str(e)}", 502

    # Strip headers that break embedding
    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection"
    ]
    headers = [
        (name, value)
        for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]

    # ✅ Force allow embedding inside Power BI iframe
    headers.append(("X-Frame-Options", "ALLOWALL"))
    headers.append(("Content-Security-Policy", "frame-ancestors *"))

    return Response(resp.content, resp.status_code, headers)

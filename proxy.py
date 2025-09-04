from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Your Streamlit Cloud app URL (no trailing slash)
TARGET = "https://kiosc-agent-app-csmqytqwhfcjow5zxzhyb6.streamlit.app"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(path):
    # Always build full URL
    url = f"{TARGET}/{path}"
    if request.query_string:
        url = f"{url}?{request.query_string.decode('utf-8')}"

    resp = requests.get(url, stream=True)

    excluded_headers = [
        "content-encoding", "content-length", "transfer-encoding", "connection"
    ]
    headers = [
        (name, value)
        for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]

    # Allow embedding
    headers.append(("X-Frame-Options", "ALLOWALL"))
    headers.append(("Content-Security-Policy", "frame-ancestors *"))

    return Response(resp.content, resp.status_code, headers)

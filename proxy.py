from flask import Flask, request, Response
import requests

app = Flask(__name__)


TARGET = "https://kiosc-agent-app-csmqytqwhfcjow5zxzhyb6.streamlit.app/"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(path):
    url = f"{TARGET}/{path}"
    resp = requests.get(
    url,
    params=request.args.to_dict(flat=False),  # ✅ convert MultiDict to dict
    stream=True
)


    excluded_headers = [
        "content-encoding", "content-length", "transfer-encoding", "connection"
    ]
    headers = [
        (name, value)
        for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]

    # 🔑 Override headers to allow embedding in Power BI
    headers.append(("X-Frame-Options", "ALLOWALL"))
    headers.append(("Content-Security-Policy", "frame-ancestors *"))

    return Response(resp.content, resp.status_code, headers)

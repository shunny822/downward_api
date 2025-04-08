from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def info():
    pod_name = os.getenv("POD_NAME", "Unknown")
    node_name = os.getenv("NODE_NAME", "Unknown")
    pod_namespace = os.getenv("POD_NAMESPACE", "Unknown")
    return (
        f"<h2>Downward API Example</h2>"
        f"<p><strong>Pod Name:</strong> {pod_name}</p>"
        f"<p><strong>Node Name:</strong> {node_name}</p>"
        f"<p><strong>Namespace:</strong> {pod_namespace}</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

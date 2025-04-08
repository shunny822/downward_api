from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def info():
    pod_name = os.getenv("POD_NAME", "Unknown")
    node_name = os.getenv("NODE_NAME", "Unknown")
    pod_namespace = os.getenv("POD_NAMESPACE", "Unknown")
    return (
        f"Container EDU | POD Working : {pod_name}</p>"
        f" | nodename : {node_name}</p>"
        f" | namespace : {pod_namespace}</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

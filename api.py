from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)
from flask import send_file

@app.route('/')
def dashboard():
    return send_file('dashboard.html')

@app.route("/metrics")
def metrics():
    return jsonify({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "memory_total_mb": round(psutil.virtual_memory().total / 1024 / 1024, 2),
        "memory_used_mb": round(psutil.virtual_memory().used / 1024 / 1024, 2)
    })

@app.route("/history")
def history():
    import csv
    rows = []
    try:
        with open("system_log.csv") as f:
            reader = csv.DictReader(f)
            rows = list(reader)[-20:]  # last 20 entries
    except FileNotFoundError:
        return jsonify({"error": "No log file found"}), 404
    return jsonify(rows)

@app.route("/health")
def health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    status = "healthy" if cpu < 80 and mem < 80 else "warning"
    return jsonify({"status": status, "cpu": cpu, "memory": mem})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

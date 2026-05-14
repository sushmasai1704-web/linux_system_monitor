# 🖥️ Linux System Monitor Dashboard

A full-stack real-time system monitoring tool built with Python, Flask, and JavaScript.
Tracks CPU, memory, and disk usage live with a clean dark-theme dashboard.

## 🚀 Demo
![Dashboard](system_report.png)

## ✨ Features
- 📊 Real-time CPU, Memory, and Disk monitoring (updates every 3 seconds)
- 📈 Live line chart with 20-point scrolling history
- 🗄️ Automatic CSV logging every 10 seconds
- 🔔 Email alerts when thresholds are exceeded
- 🌐 REST API with JSON endpoints
- 🧠 Background-tab-resistant polling via Web Worker

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, psutil |
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Data | CSV logging, REST API |
| Alerts | smtplib (email notifications) |

## 📡 API Endpoints
| Endpoint | Description |
|----------|-------------|
| `GET /` | Dashboard UI |
| `GET /metrics` | Live CPU, memory, disk JSON |
| `GET /history` | Last 20 logged entries |
| `GET /health` | System health status |

## ⚙️ Installation & Setup
```bash
# Clone the repo
git clone https://github.com/sushmasai1704-web/linux_system_monitor.git
cd linux_system_monitor

# Install dependencies
pip install flask psutil

# Start the logger (background)
python3 logger.py &

# Start the API server
python3 api.py
```
Open **http://127.0.0.1:5000** in your browser.

## 📁 Project Structure
linux_system_monitor/
├── api.py          # Flask REST API
├── logger.py       # Background CSV logger
├── dashboard.html  # Real-time dashboard UI
├── analyse.py      # Data analysis & graph generation
├── email_alert.py  # Email alert system
└── system_log.csv  # Auto-generated metrics log
## 👩‍💻 Author
**M Sai Sushma**  
[GitHub](https://github.com/sushmasai1704-web)

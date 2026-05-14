import smtplib
import psutil
from email.mime.text import MIMEText

# Config — fill these in
SENDER = "your@gmail.com"
PASSWORD = "your_app_password"  # Gmail App Password
RECEIVER = "your@gmail.com"
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

def send_alert(metric, value):
    msg = MIMEText(f"ALERT: {metric} usage is {value}% — exceeds threshold!")
    msg["Subject"] = f"System Alert: High {metric} Usage"
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
    print(f"Alert sent for {metric}: {value}%")

def check_and_alert():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    if cpu > CPU_THRESHOLD:
        send_alert("CPU", cpu)
    if mem > MEM_THRESHOLD:
        send_alert("Memory", mem)

if __name__ == "__main__":
    check_and_alert()

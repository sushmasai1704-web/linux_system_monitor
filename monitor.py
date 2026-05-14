import psutil
import time
import datetime
import csv
import os

LOG_FILE = "system_log.csv"
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

def log_to_csv(timestamp, cpu, mem, disk):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU%", "Memory%", "Disk%"])
        writer.writerow([timestamp, cpu, mem, disk])

def monitor():
    print("=== Linux System Monitor ===")
    print("Press Ctrl+C to stop\n")
    while True:
        cpu    = psutil.cpu_percent(interval=1)
        mem    = psutil.virtual_memory().percent
        disk   = psutil.disk_usage('/').percent
        ts     = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{ts}] CPU: {cpu}% | RAM: {mem}% | Disk: {disk}%")

        # Alert system
        if cpu > CPU_THRESHOLD:
            print(f"  ⚠️  ALERT: CPU usage high ({cpu}%)")
        if mem > MEM_THRESHOLD:
            print(f"  ⚠️  ALERT: Memory usage high ({mem}%)")

        log_to_csv(ts, cpu, mem, disk)
        time.sleep(3)

if __name__ == "__main__":
    monitor()

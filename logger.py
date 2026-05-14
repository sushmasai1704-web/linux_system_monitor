import psutil, csv, datetime, time

while True:
    with open('system_log.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp','cpu','memory','disk'])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'cpu': psutil.cpu_percent(interval=1),
            'memory': psutil.virtual_memory().percent,
            'disk': psutil.disk_usage('/').percent
        })
    time.sleep(10)

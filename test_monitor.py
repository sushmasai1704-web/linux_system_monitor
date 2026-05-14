import pytest
import os
import csv
import psutil
from monitor import log_to_csv

# Test 1: CSV file gets created
def test_csv_created():
    log_to_csv("2026-05-14 10:00:00", 10.0, 50.0, 30.0)
    assert os.path.isfile("system_log.csv")

# Test 2: CSV has correct headers
def test_csv_headers():
    with open("system_log.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
    assert headers == ["Timestamp", "CPU%", "Memory%", "Disk%"]

# Test 3: CPU usage is a valid percentage
def test_cpu_range():
    cpu = psutil.cpu_percent(interval=1)
    assert 0.0 <= cpu <= 100.0

# Test 4: Memory usage is a valid percentage
def test_memory_range():
    mem = psutil.virtual_memory().percent
    assert 0.0 <= mem <= 100.0

# Test 5: Disk usage is a valid percentage
def test_disk_range():
    disk = psutil.disk_usage('/').percent
    assert 0.0 <= disk <= 100.0

# Test 6: Log file is not empty
def test_csv_not_empty():
    with open("system_log.csv", "r") as f:
        lines = f.readlines()
    assert len(lines) > 1  # header + at least one data row

# Test 7: Alert threshold logic
def test_alert_threshold():
    CPU_THRESHOLD = 80
    MEM_THRESHOLD = 80
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    # System should be healthy (WSL is idle)
    assert cpu < CPU_THRESHOLD
    assert mem < MEM_THRESHOLD

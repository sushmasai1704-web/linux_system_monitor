import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
df = pd.read_csv("system_log.csv", parse_dates=["Timestamp"])

# Plot
fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
fig.suptitle("System Monitor — Performance Analysis", fontsize=14, fontweight="bold")

axes[0].plot(df["Timestamp"], df["CPU%"], color="red", linewidth=1)
axes[0].set_ylabel("CPU %")
axes[0].set_ylim(0, 100)
axes[0].grid(True, alpha=0.3)

axes[1].plot(df["Timestamp"], df["Memory%"], color="blue", linewidth=1)
axes[1].set_ylabel("Memory %")
axes[1].set_ylim(0, 100)
axes[1].grid(True, alpha=0.3)

axes[2].plot(df["Timestamp"], df["Disk%"], color="green", linewidth=1)
axes[2].set_ylabel("Disk %")
axes[2].set_ylim(0, 100)
axes[2].grid(True, alpha=0.3)

plt.xlabel("Time")
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig("system_report.png", dpi=150)
print("Graph saved as system_report.png")

# main.py
import torch
import psutil

if torch.cuda.is_available():
    print("GPU is available:", torch.cuda.get_device_name(0))
else:
    print("Using CPU")

print("CPU usage:", psutil.cpu_percent(), "%")
print("Memory usage:", psutil.virtual_memory().percent, "%")

from chat_interface import run_cli

if __name__ == "__main__":
    run_cli()
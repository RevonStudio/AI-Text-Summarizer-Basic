import shutil
import os

total, used, free = shutil.disk_usage("C:\\")
print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (1024**2)} MiB")

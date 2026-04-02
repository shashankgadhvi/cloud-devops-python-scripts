import psutil
from datetime import datetime # this is the part where we import new modules required for the code
# psutil is basically a predefined library which helps our code communicate with our OS and fetch details

def core_count():
    x = psutil.cpu_count()
    print(f"{x} is the core count.")

def cpu_usage():
    y = psutil.cpu_percent(interval=1)
    print(f"{y} is the % of cpu in usage.")

def memory_usage():
    a = psutil.virtual_memory().total
    b = psutil.virtual_memory().percent
    GB = a/(1024**3)

    print(f"{a} is the total amount of memory used in bytes.")
    print(f"{b} is the amount of memory % used.")
    print(f"memory used in GB: {GB} ")

def disk_usage():
    m = psutil.disk_usage('/').percent
    s = psutil.disk_usage('/').total

    print(f"disk usage in bytes: {s}")
    print(f"disk usage % : {m}")

def system_check():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    if cpu > 80:
        print(f"WARNING ⚠️ : Cpu usage is high: {cpu}% ")
    if mem > 80:
        print(f"WARNING ⚠️ : Memory usage is high: {mem}% ")
    if disk > 80:
        print(f"WARNING ⚠️ : Disk usage is high: {disk}%")
    if cpu <= 80 and mem <= 80 and disk <= 90:
        print("✅ All systems normal.")

def save_health():
    with open("health.txt" , "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        file.write("""--System health: timestamp -- 
        CPU usage: {cpu}%
        Memory usage: {mem}%
        Disk usage: {disk}% """
        )

core_count()
cpu_usage()
memory_usage()
disk_usage()
system_check()
save_health()

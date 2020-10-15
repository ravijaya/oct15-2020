import psutil

print(psutil.cpu_freq())
print()

for core in psutil.cpu_freq(percpu=True):
    print(core)

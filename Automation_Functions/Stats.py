# Stats.py - Shows my system stats like ram, cpu , etc.
# aka how fast is my computer today
import platform



class Stats:
    def __init__(self):
        pass
    def check_stats(self):
        my_system = platform.uname()
 
        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")

if __name__ == '__main__':
    S = Stats()
    S.check_stats()

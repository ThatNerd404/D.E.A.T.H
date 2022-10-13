# Stats.py - Shows my system stats like ram, cpu , etc.
# aka how fast is my computer today
import platform
import psutil


class Stats:
    def __init__(self):
        pass
    def check_stats(self):
        my_system = platform.uname()
        # System info
        System =  my_system.system 
        Node =  my_system.node
        Release = my_system.release
        Version = my_system.version
        Machine = my_system.machine
        Processor = my_system.processor
        
        Physical_cores =  psutil.cpu_count(logical=False)
        Total_cores = psutil.cpu_count(logical=True)

        system_info = {'System':System,'Node':Node,'Release':Release,'Version':Version,'Machine':Machine,'Processor':Processor,
        'Physical_Cores':Physical_cores,'Total_Cores':Total_cores}
        
        cpufreq = psutil.cpu_freq()
        maxfreq = f'{cpufreq.max:.2f}Mhz'
        minfreq = f"{cpufreq.min:.2f}Mhz"
        currentfreq = f"{cpufreq.current:.2f}Mhz"

        Frequency = {"max_freq":maxfreq,"min_freq":minfreq,"current_freq": currentfreq}
        # CPU usage
        cpu_usage = []
        for  i , percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            cpu_usage.append(percentage)
        total_usage = f"{psutil.cpu_percent()}%"
        bat = psutil.sensors_battery()
        battery_left = bat.percent
        battery_plugged = bat.power_plugged
        battery = {"battery_left":battery_left,"battery_plugged":battery_plugged}
        return system_info, Frequency, battery,cpu_usage, total_usage
       
if __name__ == '__main__':
    S = Stats()
    system_info,Frequency ,battery,cpu_usage, total_usage = S.check_stats()
    print(f"System: {system_info['System']}")
    print(f"Node Name: {system_info['Node']}")
    print(f"Relase: {system_info['Release']}")
    print(f"Version: {system_info['Version']}")
    print(f"Machine: {system_info['Machine']}")
    print(f"Processor: {system_info['Processor']}")
    print(f"Physical Cores: {system_info['Physical_Cores']}")
    print(f"Total Cores: {system_info['Total_Cores']}")
    print(f"Max Frequency: {Frequency['max_freq']}")
    print(f"Minimum Frequency: {Frequency['min_freq']}")
    print(f"Current Frequency: {Frequency['current_freq']}")
    for i in range(0,len(cpu_usage)):
        print(f"Core {i} usage: {cpu_usage[i]}%")
    print(f"Total core usage: {total_usage}")
    print(f"Battery left: {battery['battery_left']}%")
    print(f"Battery plugged in: {battery['battery_plugged']}")
    
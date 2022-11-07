# Stats.py - Shows my system stats like ram, cpu , etc.
# aka how fast is my computer today
import platform
import psutil


class Stats:
    def __init__(self):
        pass
    def Check_Stats(self):
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

        System_Info = {'System':System,'Node':Node,'Release':Release,'Version':Version,'Machine':Machine,'Processor':Processor,
        'Physical_Cores':Physical_cores,'Total_Cores':Total_cores}
        
        cpufreq = psutil.cpu_freq()
        maxfreqMhz = f'{cpufreq.max:.2f}Mhz'
        minfreqMhz = f"{cpufreq.min:.2f}Mhz"
        currentfreqMhz = f"{cpufreq.current:.2f}Mhz"

        Frequency = {"max_freq":maxfreqMhz,"min_freq":minfreqMhz,"current_freq": currentfreqMhz}
        # CPU usage
        cpu_usage = []
        for  _ , percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            cpu_usage.append(percentage)
        total_usage = f"{psutil.cpu_percent()}%"
        bat = psutil.sensors_battery()
        battery_left = bat.percent
        battery_plugged = bat.power_plugged
        battery = {"battery_left":battery_left,"battery_plugged":battery_plugged}
        return System_Info, Frequency, battery,cpu_usage, total_usage
       
if __name__ == '__main__':
    S = Stats()
    System_Info,Frequency ,battery,cpu_usage, total_usage = S.Check_Stats()
    print(f"System: {System_Info['System']}")
    print(f"Node Name: {System_Info['Node']}")
    print(f"Relase: {System_Info['Release']}")
    print(f"Version: {System_Info['Version']}")
    print(f"Machine: {System_Info['Machine']}")
    print(f"Processor: {System_Info['Processor']}")
    print(f"Physical Cores: {System_Info['Physical_Cores']}")
    print(f"Total Cores: {System_Info['Total_Cores']}")
    print(f"Max Frequency: {Frequency['max_freq']}")
    print(f"Minimum Frequency: {Frequency['min_freq']}")
    print(f"Current Frequency: {Frequency['current_freq']}")
    for i in range(0,len(cpu_usage)):
        print(f"Core {i + 1} usage: {cpu_usage[i]}%")
    print(f"Total core usage: {total_usage}")
    print(f"Battery left: {battery['battery_left']}%")
    print(f"Battery plugged in: {battery['battery_plugged']}")
    
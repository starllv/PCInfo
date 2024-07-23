import psutil as psu

##cpuPercent = psu.cpu_percent(interval=1)
##cpuFrequency = psu.cpu_freq().current
##memTotal = psu.virtual_memory().total
##memPercent = psu.virtual_memory().percent
##disk_parts = psu.disk_partitions()
##diskInfo = {}
##for part in disk_parts:
##    info = {}
##    total = psu.disk_usage(part.device).total
##    info['Total'] = total
##    percent = psu.disk_usage(part.device).percent
##    info['Percent'] = percent
##    diskInfo[part.device[:2]] = info
##netSent = psu.net_io_counters().bytes_sent
##netReceived = psu.net_io_counters().bytes_recv
##
##print(diskInfo)

##print("CPU Percent: ", cpuPercent, "%")
##print("CPU Frequency: ", cpuFrequency/1000, "Ghz")
##
##print("Memory Total: ", memTotal/1024/1024/1024, "GB")
##print("Memory Percent: ", memPercent, "%")
##
##disk_parts = psu.disk_partitions()
##for part in disk_parts:
##    print("Disk ", part.device[:2] , " Total: ", psu.disk_usage(part.device).total/1024/1024/1024, "GB")
##    print("Disk ", part.device[:2], " Percent: ", psu.disk_usage(part.device).percent, "%")
##
##print("Network Sent: ", netSent/1024, "KBytes")
##print("Network Received: ", netReceived/1024, "KBytes")

class PCInfo:
    def get(self):
        cpuPercent = psu.cpu_percent(interval=1)
        cpuFrequency = psu.cpu_freq().current
        memTotal = psu.virtual_memory().total
        memPercent = psu.virtual_memory().percent
        disk_parts = psu.disk_partitions()
        diskInfo = {}
        for part in disk_parts:
            info = {}
            total = psu.disk_usage(part.device).total
            info['Total'] = total
            percent = psu.disk_usage(part.device).percent
            info['Percent'] = percent
            diskInfo[part.device[:2]] = info
        netSent = psu.net_io_counters().bytes_sent
        netReceived = psu.net_io_counters().bytes_recv

        data = {'CPU Percent': cpuPercent, 'CPUFrequency': cpuFrequency,\
                        'Memory Total': memTotal, 'Memory Percent': memPercent,\
                        'Disk Info': diskInfo,\
                        'Network Sent': netSent, 'Network Received': netReceived}

        return data

import os
import psutil
import threading
def cpu_inform():
    value=psutil.cpu_percent(interval=1)
    if isinstance(value,float): 
        loading="CPU[" + "|"*round(value/2)
        value_str=str(round(value,1)) +"%]"
        print('{:<60}'.format(loading),'{:>6}'.format(value_str),sep="",end="   ")
    else:
        for val in len(value):
            loading=val+"["+"|"*round(value[val])
            value_str=str(round(value[val],1)) +"%]"
            print('{:<60}'.format(loading),'{:>6}'.format(value_str),sep="")
    return

def virtual_memory_inform():
    value=psutil.virtual_memory()
    active="|"*round(value[5]/value[0]*50)
    free="|"*round(value[4]/value[0]*50)
    not_used=str(round((value[0] - value[1])/1024/1024/1024,1))
    total=str(round(value[0]/1024/1024/1024,1))
    stat_inf =not_used+"G/" + total + "G]"
    print('{:<70}'.format("Mem[\033[31m"+active+'\033[32m'+free+'\033[0m'),'{:>10}'.format(stat_inf),sep="",end="   ")
    return

def process_info():
    tasks=str(len(list(psutil.process_iter())))
    threads = str(threading.active_count())
    inform = "Tasks:" + tasks + ",\033[32m"  + threads + "\033[0m thr"
    print('{:<25}'.format(inform))
    return

def load_average_info():
    value = list(map(lambda x: str(round(x,2)),psutil.getloadavg()))
    inform = "Load average:\033[34m" + value[0] +"\033[0m " + value[1] + " " +value[2]
    print('{:<25}'.format(inform)) 


def swap_virtual_memory_inform():
    value=psutil.swap_memory()
    active="|"*round(value[1]/value[0]*50)
    free="|"*round(value[2]/value[0]*50)
    used=str(round(value[1]/1024/1024/1024,1))
    total=str(round(value[0]/1024/1024/1024,1))
    stat_inf=used+"G/" + total + "G]"
    print('{:<70}'.format("Swp[\033[31m"+active+'\033[32m'+free+'\033[0m'),'{:>10}'.format(stat_inf),sep="", end = "   ")
    return

def uptime_info():
   # value=int(psutil.Process(os.getpid()).create_time())
    value = round(float(open("/proc/uptime").read().split()[0]))
    day = str(value // 3600 // 24)
    hours = str(value // 3600 % 24)
    minutes = str(value // 60 % 60)
    seconds = str(value % 60)
    inform = "Uptime: "+ day + " days, " + hours + ":" + minutes + ":" + seconds
    print('{:<20}'.format(inform))
    return

def process_list_info():
    print('{:>6} {:^20} {:^10} {:^10} {:^7} {:^7} {:^10} {:^20}'.format('PID','User','VIRT','RES','CPU%','MEM%','Time','Command'))
    for p in psutil.process_iter():
        print('{:>6}'.format(p.pid),end="")
        print('{:^20}'.format(p.username()),end="")
        virt=p.memory_info()[1]/1024/1024
        print('{:>10.1f}'.format(virt),end="")
        rss = p.memory_info()[0]/1024/1024
        print('{:>10.1f}'.format(rss),end="")
        print('{:>8.1f}'.format(p.cpu_percent()),end="")
        print('{:>8.1f}'.format(p.memory_percent()),end="")
        value = p.cpu_times()[0]
        minut=int(value)//60
        second=round(value - minut*60,2)
        print('{:>10}'.format(str(minut)+":"+str(second)),end="")
        names=p.cmdline()
        if len(names)>0:
            important_name=str(names[0])
            print('{:<20}'.format(" "+important_name))
        else:
            print()
    return

cpu_inform()
process_info()
virtual_memory_inform()
load_average_info()
swap_virtual_memory_inform()
uptime_info()
process_list_info()        
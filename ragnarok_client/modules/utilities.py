import psutil
def ProcessChecker(processName):
    ''' Analysis of a specified process that is running '''

    list = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Go trough all of the processes
           if processName.lower() in pinfo['name'].lower() :
               list.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return list;

import wmi
import socket
import uuid


hostname = socket.gethostname()
IP = socket.gethostbyname(socket.gethostname())
#c = wmi.WMI((hostname))

c = wmi.WMI((hostname))

#Computer info
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
free_space = float(c.Win32_LogicalDisk()[0].Freespace) / 1073741824
disk_space = float(c.Win32_LogicalDisk()[0].Size) / 1073741824


mac_num = hex(uuid.getnode()).replace('0x', '').upper()

#Format the output
mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB


for process in c.Win32_Process(name='explorer.exe'):
    last = process.GetOwner()[2]

print('PC Hostname: {0}'.format(hostname))
print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Used Space: {0} GB'.format(free_space))
print('Free Space: {0} GB'.format(disk_space))
print('Graphics Card: {0}'.format(gpu_info.Name))
print('IP: {0}'.format(IP))
print('Physical Address: {0}'.format(mac))
print('Last user login-on: {0}'.format(last))


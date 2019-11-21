import os

def add_service(port):
    os.system('echo iptables -A INPUT -p tcp --dport {port} -j REJECT'.format(port=port))
    os.system('echo iptables -A INPUT -p udp --dport {port} -j REJECT'.format(port=port))
    service_ports.append(port)

def open_for(ip):
    for port in service_ports:
         os.system('echo iptables -A INPUT -s {ip} -p tcp --dport {port} -j ACCEPT'.format(ip=ip, port=port))
         os.system('echo iptables -A INPUT -s {ip} -p udp --dport {port} -j ACCEPT'.format(ip=ip, port=port))

def close_for(ip):
    for port in service_ports:
         os.system('echo iptables -D INPUT -s {ip} -p tcp --dport {port} -j ACCEPT'.format(ip=ip, port=port))
         os.system('echo iptables -D INPUT -s {ip} -p udp --dport {port} -j ACCEPT'.format(ip=ip, port=port))


service_ports = [] # e.g. [8080]
# assumed for all service ports we have
# `iptables -A INPUT -p tcp --dport PORT -j REJECT`

hidden_ports = [] # e.g. [(443, 444)]


for port in ['8080', '10000']:
    add_service(port)
for ip in ['1.1.1.1']:
    open_for(ip)

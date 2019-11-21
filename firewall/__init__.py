import os

IPTABLES = 'echo iptables -t {table} {cmd}'
PREPEND_CMD = IPTABLES.format(cmd='-I {chain} 1 {rule}')
APPEND_CMD = IPTABLES.format(cmd='-A {chain} {rule}')
DELETE_CMD = IPTABLES.format(cmd='-D {chain} {rule}')

ADD_PORT_REJECT_RULE = APPEND_RULE.format(table='filter', chain='input',
    rule='-p {proto} --dport {port} -j REJECT')

ADD_PORT_IP_ACCEPT_RULE = PREPEND_CMD.format(table='filter', chain='input',
    rule='-p {proto} --dport {port} -j REJECT')
DEL_PORT_IP_ACCEPT_RULE = DELETE_CMD.format(table='filter', chain='input',
    rule='-s {ip} -p {proto} --dport {port} -j ACCEPT')

def add_service(port):
    os.system(ADD_PORT_REJECT_RULE.format(proto='tcp', port=port)
    os.system(ADD_PORT_REJECT_RULE.format(proto='udp', port=port)
    service_ports.append(port)

def open_for(ip):
    for port in service_ports:
         os.system(ADD_PORT_IP_ACCEPT_RULE.format(proto='tcp', ip=ip, port=port))
         os.system(ADD_PORT_IP_ACCEPT_RULE.format(proto='tcp', ip=ip, port=port))

def close_for(ip):
    for port in service_ports:
         os.system(DEL_PORT_IP_ACCEPT_RULE.format(proto='tcp', ip=ip, port=port))
         os.system(DEL_PORT_IP_ACCEPT_RULE.format(proto='tcp', ip=ip, port=port))


service_ports = [] # e.g. [8080]
# assumed for all service ports we have
# `iptables -A INPUT -p tcp --dport PORT -j REJECT`

hidden_ports = [] # e.g. [(443, 444)]

def main():
    os.system(IPTABLES.format(table='filter', cmd='-F'))

    for port in ['8080', '10000']:
        add_service(port)

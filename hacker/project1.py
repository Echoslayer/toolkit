import socket
import termcolor

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f"Port {port} Opened [+]")
    except:
        # print(f"Port {port} Closed [-]")
        pass

def scan_ports(ip_address, ports):
    print(f"IP: {ip_address} Scanning...")
    for port in range(1, int(ports)):
        scan_port(ip_address, port)
        
targets = input(termcolor.colored("[*] Enter Targets To Scan(split by ,): ", "red"))
ports = input(termcolor.colored("[*] Enter how many ports you want to sacn: ", 'green'))
if ',' in targets:
    for target in targets.split(','):
        scan_ports(target, ports)
else:
    scan_ports(targets, ports)
    
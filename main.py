import socket

def scan_ip(ip, ports):
    print(f"Scanning {ip}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            print(f"[+] Port {port} is open")
        except:
            pass
        finally:
            sock.close()

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ")
    ports_to_scan = range(1, 1025)  # Port 1 ilaa 1024
    scan_ip(target_ip, ports_to_scan)

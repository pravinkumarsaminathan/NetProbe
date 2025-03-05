import socket
import threading
import concurrent.futures

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'

# Function to scan a single port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        try:
            service = socket.getservbyport(port)
        except:
            service = RED + "Unknown service" + END
        print("Port " + GREEN + f"{port} " + END + "is open " + MAGENTA + f"({service})" + END)
    except:
        pass
    finally:
        s.close()

# Function to scan a range of ports using a thread pool
def scan_ports(ip, start_port, end_port):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    url = "https://pravin.site"
    banner = """\n\n ██████   █████           █████    ███████████                     █████             
░░██████ ░░███           ░░███    ░░███░░░░░███                   ░░███              
 ░███░███ ░███   ██████  ███████   ░███    ░███ ████████   ██████  ░███████   ██████ 
 ░███░░███░███  ███░░███░░░███░    ░██████████ ░░███░░███ ███░░███ ░███░░███ ███░░███
 ░███ ░░██████ ░███████   ░███     ░███░░░░░░   ░███ ░░░ ░███ ░███ ░███ ░███░███████ 
 ░███  ░░█████ ░███░░░    ░███ ███ ░███         ░███     ░███ ░███ ░███ ░███░███░░░  
 █████  ░░█████░░██████   ░░█████  █████        █████    ░░██████  ████████ ░░██████ 
░░░░░    ░░░░░  ░░░░░░     ░░░░░  ░░░░░        ░░░░░      ░░░░░░  ░░░░░░░░   ░░░░░░  """
    print(banner)
    print(BLUE + f"""                                                                                     
                                                                - \033]8;;{url}\033\\PRAVIN KUMAR\033]8;;\033\\                     
                                                                                     """)
    target_ip = input(YELLOW + "Enter the IP address to scan: " + END)
    start_port = int(input(YELLOW + "Enter the start port: " + END))
    end_port = int(input(YELLOW + "Enter the end port: " + END))
    print("\n")
    scan_ports(target_ip, start_port, end_port)
    print("\n")

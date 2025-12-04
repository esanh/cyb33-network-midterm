# port_scanner.py
"""
Simple TCP port scanner for midterm.
- Scans a range of ports on a target host
- Identifies open ports
- Handles invalid input and errors
"""

import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Return True if port is open, False if closed or unreachable."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        return result == 0  # 0 means success


def scan_range(host: str, start_port: int, end_port: int):
    print(f"[SCANNER] Scanning {host} from port {start_port} to {end_port}")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            if scan_port(host, port):
                print(f"[SCANNER] Port {port} is OPEN")
                open_ports.append(port)
            else:
                print(f"[SCANNER] Port {port} is closed")
        except socket.gaierror:
            print("[SCANNER] Hostname could not be resolved")
            break
        except socket.timeout:
            print(f"[SCANNER] Port {port} timed out")
        except Exception as e:
            print(f"[SCANNER] Error scanning port {port}: {e}")

    print("\n[SCANNER] Scan complete")
    if open_ports:
        print(f"[SCANNER] Open ports: {open_ports}")
    else:
        print("[SCANNER] No open ports found in this range")


def get_int_input(prompt: str) -> int:
    """Ask for an integer and handle invalid input."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("[INPUT] Invalid number, try again")


def main():
    print("=== Simple Port Scanner ===")
    print("Examples:")
    print(" - Host: 127.0.0.1")
    print(" - Host: scanme.nmap.org\n")

    host = input("Enter target host: ").strip()

    start_port = get_int_input("Enter start port (e.g., 1): ")
    end_port = get_int_input("Enter end port (e.g., 1024): ")

    if start_port <= 0 or end_port <= 0 or end_port < start_port:
        print("[INPUT] Invalid port range, please use positive numbers and make sure end >= start")
        return

    scan_range(host, start_port, end_port)


if __name__ == "__main__":
    main()

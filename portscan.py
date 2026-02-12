import nmap

def scan_target(target):
    scanner = nmap.PortScanner()
    print(f"\n Starting scan on: {target}\n")

    # Run service + version detection on ports 1–5000
    scanner.scan(target, '1-5000', '-sV')

    for host in scanner.all_hosts():
        hostname = scanner[host].hostname()
        state = scanner[host].state()

        print(f"Host: {host} ({hostname})")
        print(f"State: {state}")
        print("\n--- Open Ports ---")
        print(f"{'Port':<8} {'State':<10} {'Service':<15} {'Product':<20} {'Version'}")
        print("-" * 70)

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in sorted(ports):
                info = scanner[host][proto][port]

                port_state = info.get('state', 'unknown')
                service = info.get('name', 'unknown')
                product = info.get('product', 'unknown')
                version = info.get('version', 'unknown')

                print(f"{port:<8} {port_state:<10} {service:<15} {product:<20} {version}")

        print("-" * 70)

if __name__ == "__main__":
    target = input("Enter the host or IP to scan: ").strip()
    scan_target(target)


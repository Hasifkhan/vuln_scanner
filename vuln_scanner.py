import socket
import requests

# Function to scan for open ports
def port_scanner(target, port_range):
    print(f"\nScanning ports on {target}...")
    for port in range(*port_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

# Function to test SQL injection vulnerability
def test_sql_injection(target):
    sqli_payload = "' OR '1'='1"
    url = f"{target}?id={sqli_payload}"
    print("\nTesting for SQL Injection...")
    response = requests.get(url)
    if "syntax" in response.text or "mysql" in response.text.lower():
        print("SQL Injection Vulnerability Detected!")
    else:
        print("No SQL Injection Vulnerability Found.")

# Function to grab HTTP headers
def grab_headers(target):
    print("\nGrabbing HTTP headers...")
    response = requests.get(target)
    headers = response.headers
    for header, value in headers.items():
        print(f"{header}: {value}")

# Main execution
if __name__ == "__main__":
    target_url = input("Enter target URL (http://example.com): ")
    target_ip = input("Enter target IP address: ")
    
    # Port scanning (common ports range)
    port_scanner(target_ip, (20, 100))

    # Testing for SQL injection
    test_sql_injection(target_url)

    # Grab HTTP headers
    grab_headers(target_url)

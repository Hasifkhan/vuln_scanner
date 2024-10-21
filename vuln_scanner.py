import socket
import requests
import pyfiglet
from termcolor import colored

# Function to get IP address from URL/Domain
def get_ip_from_url(url):
    try:
        return socket.gethostbyname(url)
    except socket.gaierror:
        print(f"Unable to resolve {url}")
        return None

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

# Function to display name in style
def display_styled_name():
    ascii_banner = pyfiglet.figlet_format("HASIF")  # Replace "vuln_scanner" with your actual name
    colored_banner = colored(ascii_banner, 'green')  # You can change the color
    print(colored_banner)

# Main execution
if __name__ == "__main__":
    # Display your name in a styled format
    display_styled_name()

    # Get inputs from the user
    target_url = input("Enter target URL (http://example.com) or domain name: ").strip()
    target_ip = input("Enter target IP address (leave blank if not known): ").strip()

    # If only URL is provided, get the IP address
    if target_ip == "":
        if "http" not in target_url:
            # Prepend http:// if missing
            target_url = "http://" + target_url

        # Extract domain from URL if needed
        domain = target_url.split("//")[-1].split("/")[0]
        target_ip = get_ip_from_url(domain)
        if not target_ip:
            print("Failed to resolve domain. Exiting.")
            exit()

    print(f"\nUsing IP address: {target_ip}")
    print(f"Using URL: {target_url}")

    # Port scanning (common ports range)
    port_scanner(target_ip, (20, 100))

    # Testing for SQL injection
    test_sql_injection(target_url)

    # Grab HTTP headers
    grab_headers(target_url)

# Vulnerability Scanner

This is a simple Python-based vulnerability scanner that can scan open ports, test for SQL injection vulnerabilities, and grab HTTP headers.

## Features:
- **Port scanning**: Scans common ports to check if they are open.
- **SQL injection test**: Tests a URL for SQL injection vulnerabilities using basic payloads.
- **HTTP header grabbing**: Fetches and displays HTTP headers of the target web server.

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hasifkhan/vuln_scanner.git
   cd vuln_scanner


2. Run the setup.sh script to install dependencies and set up the environment
   ```bash
 	chmod +x setup.sh
 	sudo ./setup.sh	


## Usage:
After installation, you can run the tool using the following command:
 ```bash
	./vuln_scanner.py
		OR
	python3 vuln_scanner.py

You will be prompted to enter the target URL and IP address. The tool will then perform a port scan, test for SQL injection vulnerabilities, and grab the HTTP headers.



## Example 
	Enter target URL (http://example.com): http://testphp.vulnweb.com
	Enter target IP address: 192.168.1.1


#!/bin/bash

# Check if Python3 and pip3 are installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get install python3
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get install python3-pip
fi

# Install required Python libraries
echo "Installing required Python libraries..."
pip3 install requests

# Make the main Python script executable
echo "Making vuln_scanner.py executable..."
chmod +x vuln_scanner.py

echo "Installation complete. You can now run ./vuln_scanner.py"

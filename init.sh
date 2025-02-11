#!/usr/bin/env bash

# Update package list
echo "Updating package list..."
sudo apt update -y

# Install required packages
echo "Installing make..."
sudo apt install make -y

echo "Installing Python 3.12 virtual environment package..."
sudo apt install python3.12-venv -y

echo "Installing tree..."
sudo apt install tree -y

echo "Setup complete!"

#!/bin/bash

read -p "Enter the hostname or IP address: " target

# Linux
if command -v traceroute &> /dev/null; then
  traceroute $target
# Windows
elif command -v tracert &> /dev/null; then
  tracert $target
else
  echo "Error: Traceroute command not found."
fi
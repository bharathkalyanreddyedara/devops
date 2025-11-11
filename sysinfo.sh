#!/bin/bash
# sysinfo.sh - Display basic system information

echo "Current User:"
whoami

echo -e "\nCurrent Date:"
date

echo -e "\nDisk Usage:"
df -h

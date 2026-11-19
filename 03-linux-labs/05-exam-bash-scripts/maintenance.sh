#!/bin/bash

echo "$(date +'%Y-%m-%d %H:%M:%S') - Disk Usage: $(df -h / | tail -n 1 | awk '{print $5}')" >> /var/log/maintenance.log

if [ -d "/tmp/sandbox" ]; then
    rm -rf /tmp/sandbox
fi
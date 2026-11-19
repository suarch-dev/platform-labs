#!/bin/bash

TARGET_DIR="/home/suarch/backup_folder"

if [ -d "$TARGET_DIR" ]; then
    echo "Directory already exists: $TARGET_DIR"
else
    echo "Directory not found. Creating it..."
    mkdir "$TARGET_DIR"
    echo "Directory created successfully!"
fi

# Bash Scripting

This directory contains automation scripts developed for the headless Ubuntu Server.

## 📜 Scripts

### `check_dir.sh`
**Purpose**: Automates directory creation. 
**Logic**: Uses an `if [ -d ... ]` statement to verify if a directory exists before creating it.

### `maintenance.sh`
**Purpose**: Performs routine system maintenance.
**Logic**: 
1.  Appends the current date and disk usage (`df -h /`) to `/var/log/maintenance.log`.
2.  Checks for and removes the `/tmp/sandbox` directory if it exists.

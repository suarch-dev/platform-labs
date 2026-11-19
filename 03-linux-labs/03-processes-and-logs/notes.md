# Processes and System Logs

## Concepts Learned
*   Monitoring processes with `ps aux` and `top`.
*   Terminating processes using `kill <PID>`.
*   Managing systemd services (`systemctl start/stop/status`).
*   Reading system logs with `journalctl`. Used `-u` for specific services and `-f` to follow in real-time.

## Key Commands
```bash
# Find a process
ps aux | grep sleep
# Kill a process
kill 8374
# Check service status
sudo systemctl status ssh
# Read service logs
sudo journalctl -u ssh -n 10


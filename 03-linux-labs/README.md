# Linux Administration Labs

This directory documents my hands-on practice with Linux system administration on a headless Ubuntu Server. The lab environment is a minimal Ubuntu VM provisioned via UTM and managed remotely via SSH, simulating a real-world cloud server workflow.

## 🖥️ Environment
*   **OS**: Ubuntu 24.04 LTS (Minimal Cloud Image)
*   **Virtualization**: UTM (QEMU) on Apple Silicon
*   **Access**: SSH from macOS terminal
*   **User**: `suarch` (with `sudo` privileges)

## 🛠️ Core Commands Mastered

### User & Group Management
| Command | Description | Example |
| :--- | :--- | :--- |
| `adduser` | Creates a new user and home directory. | `sudo adduser devops-test` |
| `usermod -aG` | Adds a user to a supplementary group. | `sudo usermod -aG project-team devops-test` |
| `id` | Displays user and group IDs. | `id devops-test` |

### File Permissions & Ownership
| Command | Description | Example |
| :--- | :--- | :--- |
| `chmod` | Changes file permissions (numeric or symbolic). | `chmod 600 secret.txt` |
| `chown` | Changes file owner and group. | `sudo chown devops-test:project-team secret.txt` |
| `ls -l` | Lists files with detailed permissions. | `ls -l /tmp/sandbox/` |

### Process & Service Management
| Command | Description | Example |
| :--- | :--- | :--- |
| `ps aux` | Lists all running processes. | `ps aux \| grep sleep` |
| `kill` | Terminates a process by its PID. | `kill 8374` |
| `systemctl` | Manages systemd services (start/stop/status). | `sudo systemctl status ssh` |
| `journalctl` | Queries systemd logs. | `sudo journalctl -u ssh -n 10` |

### Networking & Connectivity
| Command | Description | Example |
| :--- | :--- | :--- |
| `ip a` | Shows network interfaces and IP addresses. | `ip a` |
| `ss -tulnp` | Lists open ports and listening processes. | `sudo ss -tulnp` |
| `curl` | Transfers data from a URL (HTTP/HTTPS). | `curl -I https://google.com` |
| `ping` | Tests network connectivity (ICMP). | `ping -c 4 google.es` |

## 📜 Scripts

### `check_dir.sh`
**Purpose**: Automates directory creation and checks if a specific folder exists.
**Logic**: Uses an `if [ -d ... ]` statement to verify the directory's existence before attempting creation.

### `maintenance.sh`
**Purpose**: Performs routine system maintenance.
**Logic**: 
1.  Appends the current date and disk usage (`df -h /`) to `/var/log/maintenance.log`.
2.  Checks for and removes the `/tmp/sandbox` directory if it exists.
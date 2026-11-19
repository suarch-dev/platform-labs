# File Permissions & Ownership

## Concepts Learned
*   **`chmod`**: Changes permissions (Read=4, Write=2, Execute=1).
    *   `600`: Only owner can read/write.
    *   `644`: Owner read/write, group/others read-only.
*   **`chown`**: Changes the owner and group of a file.
*   **Programación defensiva**: Verified permissions by trying to read a file as a different user (`sudo -u <user> cat <file>`).

## Key Commands
```bash
# Change owner and group
sudo chown devops-test:project-team secret.txt
# Change permissions to read/write for owner only
sudo chmod 600 secret.txt
# List details
ls -l

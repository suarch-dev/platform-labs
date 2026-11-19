# User & Group Management

## Concepts Learned
*   Creating users with `adduser` (interactive, creates home directory).
*   Creating groups with `groupadd`.
*   Adding users to groups with `usermod -aG` (the `-a` appends, avoiding removal from other groups).

## Key Commands
```bash
# Create a user
sudo adduser devops-test
# Create a group
sudo groupadd project-team
# Add user to group
sudo usermod -aG project-team devops-test
# Verify user details
id devops-test

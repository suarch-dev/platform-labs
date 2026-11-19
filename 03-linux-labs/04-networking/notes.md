# Linux Networking

## Concepts Learned
*   Checking IP addresses and interfaces with `ip a`.
*   Checking listening ports with `ss -tulnp`.
*   Testing HTTP connectivity with `curl -I` (headers only).
*   Testing ICMP connectivity with `ping -c 4`.

## Key Commands
```bash
# Show IP addresses
ip a
# Show listening ports
sudo ss -tulnp
# Test HTTP connection
curl -I https://google.com
# Test latency
ping -c 4 google.es


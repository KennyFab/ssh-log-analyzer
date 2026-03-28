# SSH Log Analyzer

A Python tool that parses SSH authentication logs and detects brute force login attempts. Built as part of an M.S. in Cybersecurity Engineering portfolio.

## What It Does
- Reads SSH auth log files line by line
- Detects failed login attempts
- Groups attacks by IP address
- Shows how many times each IP attempted to break in

## Why It Matters
Brute force SSH attacks are one of the most common attacks against internet-facing servers. SOC analysts need to quickly identify which IPs are attacking and how many times. This tool automates that triage.

## How To Run It
```bash
python practice.py
```

## Sample Output
```
Failed login attempts found: 9

Attacks by IP:
  192.168.1.105 → 4 attempts
  203.0.113.42  → 2 attempts
  45.33.32.156  → 3 attempts
```

## Skills Demonstrated
- Python: file handling, loops, dictionaries, f-strings
- Security: log analysis, brute force detection
- Tools: git, GitHub, terminal

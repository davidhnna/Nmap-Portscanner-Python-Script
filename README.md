# Python Nmap Port Scanner

A lightweight Python-based port scanning tool built with the
`python-nmap` library.\
This project automates safe network reconnaissance tasks commonly used
in defensive security, system auditing, and learning core networking
concepts.

## 🚀 Features

-   🔍 **Port Scanning (1--5000)** --- Automatically scans a wide range
    of ports
-   🧩 **Service & Version Detection** --- Identifies running services
    and their versions
-   📄 **JSON-Style Structured Output** --- Clean, readable results for
    analysis or logging
-   ⚙️ **Automated Enumeration** --- Loops through port ranges
    efficiently
-   🛡️ **Safe for Learning & Defensive Use** --- Intended for approved
    systems only

## 📂 Project Structure

    /project
    │── scanner.py        # Main port-scanning script
    │── requirements.txt  # python-nmap dependency
    │── README.md

## 🧠 How It Works

1.  The script uses the `python-nmap` wrapper to interface with the Nmap
    engine.\
2.  It scans a target IP for ports **1--5000** (or a user-defined
    range).\
3.  The program collects:
    -   Port state (open/closed/filtered)\
    -   Service name\
    -   Version info (when available)\
4.  Results are formatted into clean, JSON-style output.

## ▶️ Usage

### 1. Install dependencies

``` bash
pip install python-nmap
```

### 2. Run the script

``` bash
python scanner.py
```

You will be prompted for a target IP or hostname.

## ⚠️ Important Note

This tool is for **educational and defensive security purposes only**.\
Use it **only on systems you own or have explicit permission to scan**.

## 📘 What I Learned

-   Network port states and service enumeration\
-   Automating recon workflows with Python\
-   JSON-style data structuring for readable output\
-   Practical defensive security concepts and auditing techniques

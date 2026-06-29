# Data Driven Network Backup Manager

## Overview

This project automates the backup of network device configurations and applies retention rules using YAML-based configuration files. It is designed for environments where device inventory, backup commands, retention policies, and logging settings need to be managed centrally and consistently.

### Key Features

- **Multi-Vendor Support**: Cisco (NX-OS, IOS, WLC) and Juniper (Junos) devices
- **Scheduled Backups**: Daily, weekly, and monthly backup schedules
- **Jump Host Support**: Secure access through bastion/jump hosts
- **Retention Policies**: Automatic cleanup of old backups based on configurable retention counts
- **Comprehensive Logging**: Per-location logging for monitoring and troubleshooting
- **YAML-Based Configuration**: Easy-to-manage configuration files

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)

## Project Structure

```
backup_management/
├── README.md                 # This file
├── docs/configuration        # configuration documentation
├── config/
│   ├── inventory.yaml       # Device inventory and schedules
│   ├── settings.yaml        # Storage paths and retention policies
│   └── vendors.yaml         # Vendor-specific commands and settings
└── engine/
    ├── main.py              # Main backup orchestration script
    ├── backup_engine.py     # Core backup execution logic
    ├── connection.py        # Jump host and device connection manager
    ├── scheduler.py         # Schedule evaluation logic
    ├── retention.py         # Backup retention cleanup
    ├── logger_config.py     # Logging configuration
    └── config.py            # Configuration file paths
```

---

## Prerequisites

Before installing and running the project, make sure you have:

- Python 3.8 or newer
- pip for installing Python dependencies
- Network access to the devices you want to back up
- Valid credentials for the target devices and any jump host

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Network_Backup_Manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the required environment variables:

   Example on Windows PowerShell:

   ```powershell
   $env:JUMPHOST_USERNAME="jumpuser"
   $env:JUMPHOST_PASSWORD="jump-password"
   $env:JUMPHOST_IPADDRESS="10.0.0.10"
   $env:USERNAME="deviceuser"
   $env:PASSWORD="device-password"
   ```

   Example on Linux/macOS:

   ```bash
   export JUMPHOST_USERNAME="jumpuser"
   export JUMPHOST_PASSWORD="jump-password"
   export JUMPHOST_IPADDRESS="10.0.0.10"
   export USERNAME="deviceuser"
   export PASSWORD="device-password"
   ```

## Configuration

The backup behavior is controlled by the YAML files in [config/](config/):

- [config/inventory.yaml](config/inventory.yaml) – add locations, devices, IPs, and backup schedules
- [config/settings.yaml](config/settings.yaml) – define storage paths, log paths, and retention counts
- [config/vendors.yaml](config/vendors.yaml) – define vendor and platform backup command details

For step-by-step examples, see:

- [docs/configuration/inventory.md](docs/configuration/inventory.md)
- [docs/configuration/settings.md](docs/configuration/settings.md)
- [docs/configuration/vendors.md](docs/configuration/vendors.md)

## Running the Application

After configuring the YAML files and environment variables, run:

```bash
python engine/main.py
```

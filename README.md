# Data Driven Network Backup Manager

This project backs up network device configurations and applies retention rules based on YAML configuration files in the config folder.

## What this project does

- Reads device inventory from config/inventory.yaml
- Reads storage and logging settings from config/settings.yaml
- Reads vendor-specific backup commands from config/vendors.yaml
- Connects to devices using environment variables and saves backups to local storage

## Main configuration files

- [config/inventory.yaml](config/inventory.yaml) – add locations, devices, IPs, and backup schedules
- [config/settings.yaml](config/settings.yaml) – define storage paths, log paths, and retention counts
- [config/vendors.yaml](config/vendors.yaml) – define vendor and platform backup command details

## Configuration guide

See the following guides for examples and step-by-step instructions:

- [docs/configuration/inventory.md](docs/configuration/inventory.md)
- [docs/configuration/settings.md](docs/configuration/settings.md)
- [docs/configuration/vendors.md](docs/configuration/vendors.md)

## Environment variables

The backup engine expects these environment variables:

- JUMPHOST_USERNAME
- JUMPHOST_PASSWORD
- JUMPHOST_IPADDRESS
- USERNAME
- PASSWORD

Example on Linux/macOS:

```bash
export JUMPHOST_USERNAME="jumpuser"
export JUMPHOST_PASSWORD="jump-password"
export JUMPHOST_IPADDRESS="10.0.0.10"
export USERNAME="deviceuser"
export PASSWORD="device-password"
```

Example on Windows PowerShell:

```powershell
$env:JUMPHOST_USERNAME="jumpuser"
$env:JUMPHOST_PASSWORD="jump-password"
$env:JUMPHOST_IPADDRESS="10.0.0.10"
$env:USERNAME="deviceuser"
$env:PASSWORD="device-password"
```

## Running the application

Run the main script after editing the YAML files:

```bash
python engine/main.py
```

# Vendor configuration

The file [config/vendors.yaml](../../config/vendors.yaml) defines vendor-specific device details, including the Netmiko device type and the commands used for backup.

## Structure

```yaml
vendors:
  <vendor_name>:
    <platform_name>:
      device_type: <netmiko_device_type>
      pre_commands:
        - "command 1"
      backup_commands:
        - "show running-config"
```

## How to add a new vendor/platform

```yaml
vendors:
  cisco:
    ios:
      device_type: cisco_ios
      pre_commands:
        - "terminal length 0"
      backup_commands:
        - "show running-config"

  arista:
    eos:
      device_type: arista_eos
      pre_commands:
        - "terminal length 0"
      backup_commands:
        - "show running-config"
```

## How to add a new platform for an existing vendor

```yaml
vendors:
  cisco:
    ios:
      device_type: cisco_ios
      pre_commands:
        - "terminal length 0"
      backup_commands:
        - "show running-config"

    asa:
      device_type: cisco_asa
      pre_commands:
        - "terminal length 0"
      backup_commands:
        - "show running-config"
```

## Field descriptions

- `device_type` – the Netmiko device type used for SSH connection
- `pre_commands` – optional commands executed before the backup command
- `backup_commands` – one or more commands whose output is saved to the backup file

## Example with Cisco NX-OS

```yaml
vendors:
  cisco:
    nxos:
      device_type: cisco_nxos
      pre_commands:
        - "terminal length 0"
      backup_commands:
        - "show running-config"
```

## Example with Juniper

```yaml
vendors:
  juniper:
    junos:
      device_type: juniper_junos
      backup_commands:
        - "show configuration | no-more"
```

## Important notes

- The `vendor` and `platform` values in [config/inventory.yaml](../../config/inventory.yaml) must exactly match the vendor and platform names used here.
- `backup_commands` should contain the command or commands whose output you want to capture.
- `pre_commands` is optional and can be omitted if not needed.

# Inventory configuration

The file [config/inventory.yaml](../../config/inventory.yaml) defines the backup inventory. It contains locations, devices, IP addresses, vendors, platforms, and schedules.

## Structure

```yaml
location:
  <location_name>:
    mode: backup_and_retention
    devices:
      - ip: 192.168.0.1
        vendor: cisco
        platform: nxos
        schedule:
          type: daily
```

## How to add a new location

Add a new top-level entry under `location`:

```yaml
location:
  chennai:
    mode: backup_and_retention
    devices:
      - ip: 192.168.0.1
        vendor: cisco
        platform: nxos
        schedule:
          type: daily

  london:
    mode: backup_only
    devices:
      - ip: 10.20.30.40
        vendor: juniper
        platform: junos
        schedule:
          type: weekly
          day: monday
```

## How to add a new device

Add a new list item under `devices` for the desired location:

```yaml
location:
  chennai:
    mode: backup_and_retention
    devices:
      - ip: 192.168.0.1
        vendor: cisco
        platform: nxos
        schedule:
          type: daily

      - ip: 192.168.0.5
        vendor: cisco
        platform: ios
        schedule:
          type: monthly
          date: 15
```

## Supported modes

Each location can use one of the following values:

- `backup_only` – run backups only
- `retention_only` – apply retention only
- `backup_and_retention` – run backups and then apply retention

## Supported schedule types

### Daily

```yaml
schedule:
  type: daily
```

### Weekly

The current script checks `day` for weekly schedules:

```yaml
schedule:
  type: weekly
  day: monday
```

### Monthly

```yaml
schedule:
  type: monthly
  date: 1
```

## Notes

- `ip` is required for every device.
- `vendor` and `platform` must match entries defined in [config/vendors.yaml](../../config/vendors.yaml).
- If `schedule` is omitted, the device will not run unless the logic is updated.

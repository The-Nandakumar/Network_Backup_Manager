# Settings configuration

The file [config/settings.yaml](../../config/settings.yaml) defines storage locations, log files, and retention counts for each location.

## Structure

```yaml
location:
  <location_name>:
    storage_path: "/path/to/backups"
    log_path: "/path/to/logs/file.log"
    retention_count: 10
```

## How to add a new location in settings

```yaml
location:
  chennai:
    storage_path: "/home/yourname/backups/chennai"
    log_path: "/home/yourname/logs/chennai.logs"
    retention_count: 10

  london:
    storage_path: "/home/yourname/backups/london"
    log_path: "/home/yourname/logs/london.logs"
    retention_count: 30
```

## What each field means

- `storage_path` – folder where backup files are written
- `log_path` – file where runtime logs are written
- `retention_count` – maximum number of backup files kept before old files are deleted

## Example

```yaml
location:
  bangalore:
    storage_path: "/home/yourname/backups/bangalore"
    log_path: "/home/yourname/logs/bangalore.logs"
    retention_count: 31
```

## Important notes

- The location name in [config/settings.yaml](../../config/settings.yaml) should match the location name used in [config/inventory.yaml](../../config/inventory.yaml).
- Make sure the parent folders exist or the application will create them automatically for the backup path and log directory.
- A higher `retention_count` keeps more backup files.

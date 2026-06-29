import os
import yaml
import logging
from connection import ConnectionManager
from backup_engine import backup_device
from retention import apply_retention
from scheduler import should_run
from logger_config import setup_logging
from config import INVENTORY_FILE, VENDORS_FILE, SETTINGS_FILE


# ------------------ Load YAML files ------------------


with open(INVENTORY_FILE) as f:
    inventory = yaml.safe_load(f)

with open(VENDORS_FILE) as f:
    vendor_data = yaml.safe_load(f)

with open(SETTINGS_FILE) as f:
    settings = yaml.safe_load(f)

# ------------------ Setup logging ------------------

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Program started")

# ------------------ Connection manager ------------------

# jump_user = input("Enter jump host username: ")
# jump_password = getpass("Enter jump host password: ")

jump_user = os.getenv("JUMPHOST_USERNAME")
jump_password = os.getenv("JUMPHOST_PASSWORD")
jump_host = os.getenv("JUMPHOST_IPADDRESS")

device_user = os.getenv("USERNAME") 
device_password = os.getenv("PASSWORD") 


conn_manager = ConnectionManager(
    jump_host=jump_host,
    jump_user=jump_user,
    jump_password=jump_password
)

# ------------------ Main execution ------------------

for location, data in inventory["location"].items():

    logger.info(f"\nProcessing location: {location}")

    # Get mode (default = both)
    mode = data.get("mode", "backup_and_retention")

    devices = data["devices"]
    location_settings = settings["location"][location]

    storage_path = location_settings["storage_path"]
    retention_count = location_settings["retention_count"]
    log_path = location_settings["log_path"]
    
    log_dir = os.path.dirname(log_path)

    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


    # -------- Mode Handling --------

    if mode == "backup_only":
        logger.info("Mode: Backup Only")

        for device in devices:
            if should_run(device):
                logger.info(f"Running backup for {device['ip']}")
                backup_device(
                        device,
                        vendor_data,
                        conn_manager,
                        location_settings,
                        credentials={
                            "username": device_user,
                            "password": device_password
                        }
                    )
            else:
                logger.info(f"Skipping {device['ip']} due to schedule")


    elif mode == "retention_only":
        logger.info("Mode: Retention Only")
        apply_retention(storage_path, retention_count)

    elif mode == "backup_and_retention":
        logger.info("Mode: Backup + Retention")

        for device in devices:
            if should_run(device):
                logger.info(f"Running backup for {device['ip']}")
               
                backup_device(
                    device,
                    vendor_data,
                    conn_manager,
                    location_settings,
                    credentials={
                        "username": device_user,
                        "password": device_password
                    }
                )
            else:
                logger.info(f"Skipping {device['ip']} due to schedule")
        apply_retention(storage_path, retention_count)

    else:
        logger.info(f"Unknown mode: {mode}")
    
    #   remove handler after location
    logger.removeHandler(file_handler)
    file_handler.close()

import os
from datetime import datetime
import logging
# from getpass import getpass

def backup_device(device, vendor_data, conn_manager, settings, credentials):
    logger = logging.getLogger(__name__)

    ip = device["ip"]
    vendor = device["vendor"]
    platform = device["platform"]

    # get vendor info
    vendor_info = vendor_data["vendors"][vendor][platform]

    device_type = vendor_info["device_type"]
    commands = vendor_info["backup_commands"]
    pre_commands = vendor_info.get("pre_commands", [])

    # username = input(f"Enter username for {ip}: ")
    # password = getpass(f"Enter password for {ip}: ")

    username = credentials["username"]
    password = credentials["password"]

    ssh = conn_manager.connect(
        device_ip=ip,
        username=username,
        password=password,
        device_type=device_type
    )

    if not ssh:
        return

    try:
        # run pre-commands
        for cmd in pre_commands:
            ssh.send_command(cmd)

        output = ""

        # run backup commands
        for cmd in commands:
            output += ssh.send_command(cmd) + "\n"

        # save file
        storage_path = settings["storage_path"]
        os.makedirs(storage_path, exist_ok=True)

        
        timestamp = datetime.now().strftime("%H:%M-%d%m%Y")
        file_name = f"{ip}_{timestamp}.txt"
        file_path = os.path.join(storage_path, file_name)

        with open(file_path, "w") as f:
            f.write(output)

        logger.info(f"Backup success: {ip}")

    finally:
        conn_manager.disconnect(ssh)
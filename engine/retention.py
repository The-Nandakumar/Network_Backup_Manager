import os
import logging

logger = logging.getLogger(__name__)

def apply_retention(storage_path, retention_count):

    logger.info("Starting retention cleanup...")

    # Step 1: get all files
    files = []
    for file_name in os.listdir(storage_path):
        full_path = os.path.join(storage_path, file_name)

        # make sure it's a file (not folder)
        if os.path.isfile(full_path):
            files.append(full_path)

    # Step 2: sort files by modified time (oldest first)
    files.sort(key=os.path.getmtime)

    logger.info(f"Total files found: {len(files)}, Retention count: {retention_count}")

    
    # Step 3: Check if cleanup is needed
    if len(files) <= retention_count:
        logger.info("No files deleted. Retention policy already satisfied.")
        logger.info("Retention cleanup completed.")
        return


    # Step 3: delete old files
    deleted_count = 0
    while len(files) > retention_count:
        old_file = files[0]   # oldest file
        os.remove(old_file)
        logger.info(f"Deleted: {old_file}")

        files.pop(0)  # remove from list
        deleted_count += 1


    logger.info(f"Deleted {deleted_count} file(s) as part of retention cleanup.")
    logger.info("Retention cleanup completed.")

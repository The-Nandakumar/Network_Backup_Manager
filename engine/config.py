import os

# Construct BASE_PATH relative to this file's location
BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "config")

INVENTORY_FILE = os.path.join(BASE_PATH, "inventory.yaml")
VENDORS_FILE = os.path.join(BASE_PATH, "vendors.yaml")
SETTINGS_FILE = os.path.join(BASE_PATH, "settings.yaml")
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def should_run(devices):
    logger.info(f"Checking schedule for {devices['ip']}")
    schedule = devices.get("schedule", {})
    sched_type = schedule.get("type")

    now = datetime.now()

    if sched_type == "daily":
        return True

    elif sched_type == "weekly":
        today = now.strftime("%A").lower()
        return today == schedule.get("day", "").lower()

    elif sched_type == "monthly":
        return now.day == int(schedule.get("date", -1))

    return False
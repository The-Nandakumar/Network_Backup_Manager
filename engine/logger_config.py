import logging

def setup_logging(log_file=None):

    logger = logging.getLogger()   # root logger
    logger.setLevel(logging.INFO)

    
    # ✅ Prevent duplicate handlers
    if logger.handlers:
        return logger


    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(format)

    # ✅ Console (GitHub Actions output)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # ✅ File (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
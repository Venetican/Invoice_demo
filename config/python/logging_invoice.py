import logging
from pathlib import Path
from config_invoice import settings

TMP_FOLDER = Path(settings.APP.REPO) / settings.SUBDIR.TMP
APP_LOGGER = settings.FILES.APP_LOGGER

def setup_logger(
        name: str = None, 
        log_file: str = TMP_FOLDER / APP_LOGGER,
        level: int = logging.DEBUG) -> logging.Logger:
    """Configures and returns a logger instance."""
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Clear existing handlers
    logger = logging.getLogger(name if name else __name__)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Set up file handler with the given formatter
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Create logger and add the file handler to it
    logger = logging.getLogger(name if name else __name__)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger

# Use the logger setup function to get a logger instance for the module
logger = setup_logger()

"""Emit logs
"""

import logging

logger = logging.getLogger(__name__)

def emit_debug_logs():
    """Emit debug logs
    """
    logger.debug("This is a debug log")

def emit_info_logs():
    """Emit info logs
    """
    logger.info("This is an info log")

def emit_warning_logs():
    """Emit warning logs
    """
    logger.warning("This is a warning log")

def emit_error_logs():
    """Emit error logs
    """
    logger.error("This is an error log")
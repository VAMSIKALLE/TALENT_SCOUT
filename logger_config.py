"""
logger_config.py
Central logging setup for the TalentScout Resume Analyzer.
"""

import logging


def get_logger(name: str = "TalentScout") -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Console logging only.
    # Vercel captures console logs automatically.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
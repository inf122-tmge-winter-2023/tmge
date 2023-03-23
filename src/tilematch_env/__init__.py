"""
    :module_name: tilematch_env
    :module_summary: An environment supporting multiplayer tile matching games
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging

LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter('[%(asctime)s|%(name)s|%(levelname)s] - %(message)s')

LOGGER.setLevel(logging.INFO)
LOG_HANDLER.setLevel(logging.INFO)

LOG_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(LOG_HANDLER)

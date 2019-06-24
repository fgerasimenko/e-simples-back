# -*- coding: utf-8 -*-
import logging

from flask import current_app

logger = None


def get_logger():
    if current_app:
        return current_app.logger
    else:
        global logger

        if not logger:
            logger = logging.getLogger(__name__)

        return logger
import logging
import os
import shutil
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_voila():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _voila_command():
        return [
            "voila",
            "--token",
            "--no-browser",
            "--port",
            "{port}",
            "--server_url",
            "/",
            "--base_url",
            "{base_url}voila/",
        ]

    return {
        "command": _voila_command,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {"title": "Voila"},
    }

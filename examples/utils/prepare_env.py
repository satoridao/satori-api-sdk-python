#!/usr/bin/env python

import os
import pathlib
from configparser import ConfigParser


def get_env():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    config_dict = {}
    for key, value in config.items("keys"):
        config_dict[key] = value
    return config_dict


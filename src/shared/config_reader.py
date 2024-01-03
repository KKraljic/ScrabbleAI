"""
The config_reader module provides a singleton Config object,
that provides values from the config.ini file.
"""

import os
from configparser import ConfigParser
from typing import Any


class Config:
    """
    Class for providing values from the config.ini file.
    """
    _instance: ConfigParser = ConfigParser()
    _initialized: bool = False
    _config_path: str = os.path.join(os.getcwd(), 'config.ini')

    @staticmethod
    def _initialize() -> None:
        """
        Reads the content from the config file.
        """
        if not Config._initialized:
            Config._instance.read(Config._config_path)
            Config._initialized = True

    @staticmethod
    def _check_init(func: Any):
        """
        Wrapper for checking if the config was initialized.
        It not, it becomes.
        :param func: Function to be wrapped
        """
        def wrap(*args, **kwargs):
            Config._initialize()
            return func(*args, **kwargs)

        return wrap

    @staticmethod
    def _config_int_default(option: str, default: int, section: str = 'DEFAULT') -> int:
        """
        Static method for retrieving an integer value from the config with a default value.
        :param option: Name of the field in the config.
        :param default: Value that is returned, if the field is invalid or not found.
        :param section: Section in which the field can be found.
        :return: Value of the field
        """
        return int(Config._instance[section][option]) \
            if Config._instance.has_option(section, option) \
            else default

    # Config fields -------------------------------------------------------------

    @staticmethod
    @_check_init
    def board_size() -> int:
        """
        :return: Size of the scrabble board. Default is 15.
        """
        return Config._config_int_default('BoardSize', 15)

    @staticmethod
    @_check_init
    def rack_size() -> int:
        """
        :return: Size of the scrabble rack. Default is 7.
        """
        return Config._config_int_default('RackSize', 7)

    @staticmethod
    @_check_init
    def bag_config_path() -> str:
        """
        :return: Path to the file, where the bag tiles are defined.
        """
        path = os.path.join(os.getcwd(), 'data', Config._instance['DEFAULT']['BagConfigFile'])
        return path if os.path.exists(path) else ''

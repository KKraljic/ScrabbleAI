import configparser
import os


class Config:
    _instance = None

    def __init__(self):
        Config._initialize()

    @staticmethod
    def _initialize():
        if Config._instance is None:
            config = configparser.ConfigParser()
            config.read('config.ini')
            Config._instance = config

    @staticmethod
    def _check_init(func):
        def wrap(*args, **kwargs):
            Config._initialize()
            return func(*args, **kwargs)

        return wrap

    @_check_init
    @staticmethod
    def board_size() -> int:
        return int(Config._instance['DEFAULT']['BoardSize'])

    @_check_init
    @staticmethod
    def rack_size() -> int:
        return int(Config._instance['DEFAULT']['RackSize'])

    @_check_init
    @staticmethod
    def bag_config_path() -> str:
        path = os.path.join(os.getcwd(), 'data', Config._instance['DEFAULT']['BagConfigFile'])
        return path if os.path.exists(path) else ''

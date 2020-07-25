#!/usr/bin/env python3

import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import os
from pathlib import Path
from bundles.actions.Volume import Volume
import threading


class Configurator:
    def __init__(self):
        env_path = str(Path('.')) + '/.env'
        env_path_local = str(Path('.')) + '/.env.local'

        if os.path.exists(env_path_local):
            load_dotenv(dotenv_path=env_path_local)
        elif os.path.exists(env_path):
            load_dotenv(dotenv_path=env_path)


class Application:
    def __init__(self):
        Configurator()

        self.logger = self._init_logs()
        self._volume = Volume(self.logger)

    def _init_logs(self):
        log_level = getattr(logging, os.getenv('LOG_LEVEL').upper(), None)

        logger = logging.getLogger()
        logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

        file_handler = RotatingFileHandler(os.getenv('LOG_PATH'), 'a', 1000000, 1)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        steam_handler = logging.StreamHandler()
        steam_handler.setLevel(log_level)
        steam_handler.setFormatter(formatter)
        logger.addHandler(steam_handler)

        return logger

    def start(self):
        self.logger.info('Start actions Volume management')

        thread = threading.Thread(target=self._volume.start)
        thread.start()



def main():
    application = Application()
    application.start()


if __name__ == '__main__':
    main()

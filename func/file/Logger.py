import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(self.config("level"))

    def set_handler(self):
        from logging.handlers import RotatingFileHandler

        formatter = logging.Formatter(self.formatter())
        handler = RotatingFileHandler(self.file_name(), maxBytes=1024*1024*500, backupCount=2)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @staticmethod
    def config(flag):
        from conf.config import Config
        return Config().logging(flag)

    @staticmethod
    def file_name():
        return f"log\\daily_check.log"

    @staticmethod
    def formatter():
        #return "[%(levelname)s]%(asctime)s::%(module)s::%(funcName)s::%(lineno)s::%(message)s"
        return "[%(levelname)s]%(asctime)s::%(module)s::%(lineno)s::%(message)s"


import logging
import os
from logging.handlers import RotatingFileHandler

from django.conf import settings


class LevelFileHandler(RotatingFileHandler):

    def __init__(
            self,
            filename: str,
            mode: str = "a",
            maxBytes: int = 0,
            backupCount: int = 0,
            encoding: str = 'utf-8'
    ) -> None:
        super().__init__(filename, mode, maxBytes, backupCount)
        self.file_name = filename
        self.mode = mode
        self.maxBytes = maxBytes
        self.backupCount = backupCount
        self.encoding = encoding

    @staticmethod
    def __created_file(file_name: str) -> str:
        """Generate a path for the created file in the current directory"""

        current_dir = settings.LOGGING_ROOT
        return os.path.join(current_dir, file_name)

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        level = record.levelname.lower()
        self.file_name = self.__created_file(f"{record.name}_{level}.log")

        with open(self.file_name, self.mode, encoding = self.encoding) as file:
            file.write(f"{msg}\n")
from enum import Enum

class Status(Enum):
    MAIN_MENU = 'MAIN_MENU'
    INFO = 'INFO'
    DATA = 'DATA'
    SCREENING = 'SCREENING'
    OTHER = 'OTHER'

    def __str__(self):
        return '%s' % self.value
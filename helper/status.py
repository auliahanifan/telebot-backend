import json
import dataclasses
import typing
from enum import Enum

class Status(Enum):
    MAIN_MENU = 'MAIN_MENU'
    INFO = 'INFO'
    DATA = 'DATA'
    SCREENING = 'SCREENING'
    OTHER = 'OTHER'

    def __str__(self):
        return '%s' % self.value

@dataclasses.dataclass
class Screening:
    phone_number: typing.Optional[str] = None
    symptom_high_temp: typing.Optional[bool] = None
    symptom_cough: typing.Optional[bool] = None
    symptom_hard_to_breath: typing.Optional[bool] = None
    symptom_anosmia: typing.Optional[bool] = None
    contact_patient: typing.Optional[bool] = None
    contact_suspect: typing.Optional[bool] = None

    def __str__(self):
        return json.dumps(dataclasses.asdict(self))

    def __repr__(self):
        return json.dumps(dataclasses.asdict(self))

    def to_json(self) -> dict:
        """Convert all dataclass to dictionary
        :return: dict
        """
        return dataclasses.asdict(self)

@dataclasses.dataclass
class ChatStatus:
    status: typing.Optional[Status]
    screening: typing.Optional[Screening] = None

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return json.dumps(dataclasses.asdict(self))

    def __repr__(self):
        return json.dumps(dataclasses.asdict(self))

    def to_json(self) -> dict:
        """Convert all dataclass to dictionary
        :return: dict
        """
        return dataclasses.asdict(self)
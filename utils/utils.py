from enum import Enum
import random
from typing import List

from utils.constants import *
from src.district.district import *


def randomDistance() -> float:
    return random.randrange(1, 10) / 10


def randomDataEnum(data: Enum) -> Enum:
    return random.choice(list(data))


def writeInArchive(listDistricts: List):
    with open("databaseFixed.arff", "w") as arquivo:
        arquivo.write(HEADER_DB)
        for district in listDistricts:
            arquivo.write(district.__repr__())

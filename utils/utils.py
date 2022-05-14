from enum import Enum
import random
from typing import List

from utils.constants import *
from src.district.district import *


def randomDistance() -> float:
    return random.randrange(1, 10) / 10


def randomDataEnum(data: Enum) -> Enum:
    return random.choice(list(data))


def generalizeValue(value: float) -> str:

    if (value <= 1 and value > 0.75):
        return 'otimo'
    if (value <= 0.75 and value > 0.5):
        return 'bom'
    if (value <= 0.5 and value > 0.25):
        return 'ruim'
    return 'pessimo'

# def generalizeValue(value: float) -> str:

#     if (value <= 1 and value > 0.666666667):
#         return 'otimo'
#     if (value <= 0.666666667 and value > 0.333333333):
#         return 'bom'
#     return 'ruim'


def writeInArchive(listDistricts: List):
    with open("databaseFixed.arff", "w") as arquivo:
        arquivo.write(HEADER_DB)
        for district in listDistricts:
            arquivo.write(district.__repr__())


def writeInArchiveID3(listDistricts: List):
    with open("databaseFixed.arff", "w") as arquivo:
        arquivo.write(HEADER_DB_ID3)
        for district in listDistricts:
            arquivo.write(district.writeID3())

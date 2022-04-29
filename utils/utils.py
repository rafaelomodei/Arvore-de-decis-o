from enum import Enum
import random
from typing import List

from utils.constants import *
from src.district.district import *


def randomPrice() -> int:
    return random.randint(MIM_PRICE, MAX_PRICE)


def chanceAcceptingVariationRatio(value, maxValue) -> int:
    return abs(proportion(value, maxValue) - 1)


def randomDistance() -> int:
    return random.randint(MIM_DISTANCE, MAX_DISTANCE)


def randomDataEnum(data: Enum) -> Enum:
    return random.choice(list(data))


def proportion(value: float, maxValue: int) -> float:
    return ((100 * value) / maxValue) / 100


# def sumWeights(sewer: float, topography: float, utilization: float, conservation: float, pavimentation: float, price: float, distanceUTFPR: float, centralSquareDistance: float, chanceAcceptancePrice: float) -> float:
#     sum: float = sewer + topography\
#         + utilization + conservation\
#         + pavimentation + price\
#         + distanceUTFPR + centralSquareDistance\
#         + chanceAcceptancePrice
#     return sum


# def chanceGeneralAcceptance(sewer: float, topography: float, utilization: float, conservation: float, pavimentation: float, price: float, distanceUTFPR: float, centralSquareDistance: float, chanceAcceptancePrice: float) -> int:
#     _accepted: int = 0

#     sumGeneralWeights = sumWeights(sewer, topography, utilization, conservation, pavimentation,
#                                    price, distanceUTFPR, centralSquareDistance, chanceAcceptancePrice)

#     proportionSumWeights = proportion(sumGeneralWeights, 1000)

#     if (random.random() < proportionSumWeights):
#         _accepted = 1

#     return _accepted

def writeInArchive(listDistricts: List):
    with open("databaseFixed.arff", "w") as arquivo:
        arquivo.write(HEADER_DB)
        for district in listDistricts:
            arquivo.write(district.__repr__())
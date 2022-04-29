from faker import Faker

from utils.enums import *
from utils.utils import *

faker = Faker(['pt_BR'])


class District:
    name: str
    sewer: Enum
    topography: Enum
    utilization: Enum
    conservation: Enum
    pavimentation: Enum
    price: int
    distanceUTFPR: int
    centralSquareDistance: int
    chanceAcceptancePrice: int
    chanceGeneralAcceptance: int

    def __init__(self) -> None:
        self.name = faker.bairro()
        self.sewer = randomDataEnum(Sewer)
        self.topography = randomDataEnum(Topography)
        self.utilization = randomDataEnum(Utilization)
        self.conservation = randomDataEnum(Conservation)
        self.pavimentation = randomDataEnum(Pavimentation)
        self.price = randomPrice()
        self.distanceUTFPR = randomDistance()
        self.centralSquareDistance = randomDistance()
        self.chanceAcceptancePrice = chanceAcceptingVariationRatio(
            self.price, MAX_PRICE)
        # self.chanceGeneralAcceptance = chanceGeneralAcceptance(self.sewer.value, self.topography.value, self.utilization.value, self.conservation.value,
        #                                                        self.pavimentation.value, self.price, self.distanceUTFPR, self.centralSquareDistance, self.chanceAcceptancePrice)
        self.chanceGeneralAcceptanceA()

    def __str__(self) -> None:
        values: str = f'Nome: {self.name} \n' \
            + f'Esgoto: {self.sewer.name} \n' \
            + f'Topografia: {self.topography.name} \n'\
            + f'Utilização: {self.utilization.name} \n'\
            + f'Conservação: {self.conservation.name} \n'\
            + f'Pavimentação: {self.pavimentation.name} \n'\
            + f'Preço: {self.price} m2 \n'\
            + f'Distancia da UTFPR: {self.distanceUTFPR} km\n'\
            + f'Distancia da praça central: {self.centralSquareDistance} km\n'\
            + f'Chace de aceitacao por preco: {self.chanceAcceptancePrice} % \n'\
            + f'Chance de aceitação geral: {self.chanceGeneralAcceptance} \n'
        return values

    def __repr__(self) -> str:

        values: str = f'{self.topography.name},'\
            + f'{self.utilization.name},'\
            + f'{self.conservation.name},'\
            + f'{self.sewer.name},'\
            + f'{self.pavimentation.name},'\
            + f'{self.price},'\
            + f'{self.distanceUTFPR},'\
            + f'{self.centralSquareDistance},'\
            + f'{self.chanceAcceptancePrice},'\
            + f'{self.chanceGeneralAcceptance}\n'
        return values

    def sumWeights(self) -> float:
        sum: float = self.sewer.value + self.topography.value\
            + self.utilization.value + self.conservation.value\
            + self.pavimentation.value + self.price\
            + self.distanceUTFPR + self.centralSquareDistance\
            + self.chanceAcceptancePrice
        return sum


    def chanceGeneralAcceptanceA(self) -> None:
        _accepted: int = 0

        sumGeneralWeights = self.sumWeights()

        proportionSumWeights = proportion(sumGeneralWeights, 1000)

        if (random.random() < proportionSumWeights):
            _accepted = 1
        self.chanceGeneralAcceptance = _accepted

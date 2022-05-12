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
    accessToHealth: Enum
    securityLevel: Enum
    firefighter: Enum
    internetOptions: Enum
    operatorSignal: Enum
    leisureArea: Enum
    mobility: Enum
    location: Enum
    consumePower: Enum
    price: float
    distanceUTFPR: float
    centralSquareDistance: float
    supplyAndDemand: float

    def __init__(self) -> None:
        self.name = faker.bairro()
        self.sewer = randomDataEnum(Sewer)
        self.topography = randomDataEnum(Topography)
        self.utilization = randomDataEnum(Utilization)
        self.conservation = randomDataEnum(Conservation)
        self.pavimentation = randomDataEnum(Pavimentation)
        self.accessToHealth = randomDataEnum(AccessToHealth)
        self.securityLevel = randomDataEnum(SecurityLevel)
        self.firefighter = randomDataEnum(Firefighter)
        self.internetOptions = randomDataEnum(InternetOptions)
        self.operatorSignal = randomDataEnum(OperatorSignal)
        self.leisureArea = randomDataEnum(LeisureArea)
        self.mobility = randomDataEnum(Mobility)
        self.location = randomDataEnum(Location)
        self.consumePower = randomDataEnum(ConsumePower)
        self.centralSquareDistance = randomDistance() * 10
        self.distanceUTFPR = randomDistance() * 10 
        self.priceSquareMeter()
        self.calcSupplyAndDemand()

    def __str__(self) -> None:
        values: str = f'Nome: {self.name} \n' \
            + f'Esgoto: {self.sewer.name} \n' \
            + f'Topografia: {self.topography.name} \n'\
            + f'Utilização: {self.utilization.name} \n'\
            + f'Conservação: {self.conservation.name} \n'\
            + f'Pavimentação: {self.pavimentation.name} \n'\
            + f'Acesso a saúde: {self.accessToHealth.name} \n'\
            + f'Nível de segurança: {self.securityLevel.name} \n'\
            + f'Bombeiro: {self.firefighter.name} \n'\
            + f'Opções de internet: {self.internetOptions.name} \n'\
            + f'Sinal de operadora: {self.operatorSignal.name} \n'\
            + f'Área para lazer: {self.leisureArea.name} \n'\
            + f'Mobilidade: {self.mobility.name} \n'\
            + f'Localização: {self.location.name} \n'\
            + f'Poder de consulmo: {self.consumePower.name} \n'\
            + f'Oferta e procura: {self.supplyAndDemand} \n'\
            + f'Preço: {self.price} m2 \n'\
            + f'Distancia da UTFPR: {self.distanceUTFPR} km\n'\
            + f'Distancia da praça central: {self.centralSquareDistance} km\n'

        return values

    def __repr__(self) -> str:

        values: str = f'{self.topography.name}, '\
            + f'{self.utilization.name}, '\
            + f'{self.conservation.name}, '\
            + f'{self.sewer.name}, '\
            + f'{self.pavimentation.name}, '\
            + "{:.2f}, ".format(self.price)\
            + f'{self.distanceUTFPR}, '\
            + f'{self.centralSquareDistance}\n'
            # + "{:.2f}, ".format(self.price)\
            # + f'{self.accessToHealth.name}, '\
            # + f'{self.securityLevel.name}, '\
            # + f'{self.firefighter.name}, '\
            # + f'{self.internetOptions.name}, '\
            # + f'{self.operatorSignal.name}, '\
            # + f'{self.leisureArea.name}, '\
            # + f'{self.mobility.name}, '\
            # + f'{self.location.name}, '\
            # + "{:.2f}, ".format(self.supplyAndDemand)\
            # + f'{self.consumePower.name}\n'

        return values

    def basicItems(self) -> float:
        _totalAttributes: int = 7

        sum: float = self.topography.value\
            + self.utilization.value\
            + self.conservation.value\
            + self.pavimentation.value\
            + self.sewer.value\
            + self.distanceUTFPR\
            + self.centralSquareDistance
            # + self.consumePower.value\
            # + self.accessToHealth.value\
            # + self.securityLevel.value\
            # + self.firefighter.value\
            # + self.internetOptions.value\
            # + self.operatorSignal.value\
            # + self.leisureArea.value\
            # + self.mobility.value\
            # + self.location.value

        return sum / _totalAttributes

    def priceSquareMeter(self) -> None:
        _totalAttributes: int = 7

        sum: float = self.topography.value\
            + self.utilization.value\
            + self.conservation.value\
            + self.sewer.value\
            + self.pavimentation.value\
            + self.distanceUTFPR\
            + self.centralSquareDistance
            # + self.consumePower.value\
            # + self.mobility.value\
            # + self.location.value\

        result: float = sum / _totalAttributes

        self.price = result * 10

    def unemploymentRate(self) -> float:
        _totalAttributes: int = 2

        sum: float = self.consumePower.value + self.utilization.value

        return sum / _totalAttributes

    def calcSupplyAndDemand(self) -> None:
        _totalAttributes: int = 3

        sum: float = self.basicItems() + self.unemploymentRate() + self.price

        result = sum / _totalAttributes

        self.supplyAndDemand = result

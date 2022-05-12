from enum import Enum


class Topography(Enum):
    aclive: float = 0.3
    declive: float = 0.4
    plano: float = 0.9
    irregular: float = 1


class Utilization(Enum):
    residencial: float = 0.5
    comercial: float = 0.75
    terreno: float = 1


class Conservation(Enum):
    otimo: float = 1
    bom: float = 0.75
    regular: float = 0.5
    mau: float = 0


class Sewer(Enum):
    sim: int = 1
    nao: int = 0


class Pavimentation(Enum):
    poliedrico: float = 0.5
    irregular: float = 0
    asfalto: float = 1


class AccessToHealth(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class SecurityLevel(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class Firefighter(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class InternetOptions(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class OperatorSignal(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class LeisureArea(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class Mobility(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class Location(Enum):
    ruim: float = 0.1
    bom: float = 0.5
    otimo: float = 1


class ConsumePower(Enum):
    baixo: float = 0.1
    medio: float = 0.5
    alto: float = 1

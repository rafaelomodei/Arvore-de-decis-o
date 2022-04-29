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

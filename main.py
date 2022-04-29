from typing import List

from src.district.district import District
from utils.utils import writeInArchive


def main():

    listDistricts: List[District] = list()

    for index in range(10000):
        listDistricts.append(District())

    for district in listDistricts:
        print(district)
    
    # writeInArchive(listDistricts)


if __name__ == "__main__":
    main()

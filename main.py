from typing import List

from src.district.district import District
from utils.utils import writeInArchive, writeInArchiveID3


def main():

    listDistricts: List[District] = list()

    for index in range(10000):
        listDistricts.append(District())

    for district in listDistricts:
        print(district)

    # writeInArchive(listDistricts)
    writeInArchiveID3(listDistricts)



if __name__ == "__main__":
    main()

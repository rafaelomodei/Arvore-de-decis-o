MIM_DISTANCE: int = 1
MAX_DISTANCE: int = 20

MIM_PRICE: int = 100
MAX_PRICE: int = 900

HEADER_DB = f'@relation avaliation\n\n'\
            + f"@attribute topografia {{aclive, declive, plano, irregular}}\n"\
            + f'@attribute utilizacao {{residencial, comercial, terreno}}\n'\
            + f'@attribute conservacao {{otimo, bom, regular, mau}}\n'\
            + f'@attribute esgoto {{sim, nao}}\n'\
            + f'@attribute pavimentacao {{poliedrico, asfalto, irregular}}\n'\
            + f'@attribute preco numeric\n'\
            + f'@attribute distanciaUTFPR numeric\n'\
            + f'@attribute distanciaPracaCentral numeric\n'\
            + f'@attribute chaceAceitarPreco numeric\n'\
            + f'@attribute chaceAceitacaoGeral {{0,1}}\n\n'\
            + f'@data\n'
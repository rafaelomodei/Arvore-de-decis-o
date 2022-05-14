# Arvore-de-decisao – SISTEMAS INTELIGENTES APLICADOS

## Sobre

#### Objetivo
O objetivo deste trabalho é montar e testar uma base de dados  com informações de bairros, para o uso em três tipos de algoritmos de Árvore de Decisão, dentre eles estão ID3, CART e C4.5, utilizando o software Weka (EIBE; HALL; WITTEN, 2016), o qual foi desenvolvido pela Universidade de Waikato, da Nova Zelândia. O ambiente de trabalho Weka é uma coleção de algoritmos de aprendizado de máquina e ferramentas para pré-processamento de dados. É projetado para testar rapidamente os métodos existentes em novos conjuntos de dados de maneiras flexíveis (Idem).
Mais especificamente, esse trabalho consiste em aplicar os conhecimentos adquiridos na disciplina de  Sistemas Inteligentes, com o foco em algoritmos de árvore de decisão para auxiliar na avaliação de bairros fictícios na cidade de Santa Helena.

#### Árvore de Decisão
Árvore de decisão é um classificador simbólico representado como estrutura de árvore, onde cada nó interno indica o teste em um atributo, cada ramo representa um resultado do teste, e os nós terminais representam classes ou distribuições de classe. O topo da árvore representa a raiz e os nós terminais, as folhas (MOTTA, 2004).

## Algoritimos

#### ID3
O algoritmo ID3 se orienta por uma heurística, que são soluções baseadas em algum tipo de conhecimento prévio sobre as propriedades dos dados, onde se procura a solução do problema (OEIRAS, 2020).

Através do Ganho de Informação e Entropia o algoritmo saberá qual melhor atributo escolher. A heurística ID3 usa o conceito de entropia para formular o ganho de informação na escolha de um atributo particular para o próximo nó na árvore de decisão.

* Entropia: A física usa o termo entropia para descrever a quantidade de desordem associada a um sistema. Na teoria da informação, este termo tem um significado semelhante — ele mede o grau de desordem de um conjunto de dados. A heurística ID3 usa este conceito para encontrar o próximo melhor atributo de um dado para ser utilizado como nó de uma árvore de decisão.

#### CART
Técnica não-paramétrica que produz árvores de classificação ou regressão, dependendo se as árvores são categóricas ou numéricas, respectivamente.

#### C4.5
Algoritmo para geração de árvores de decisão, sucessor do algoritmo ID3. O algoritmo C4.5 considera atributos numéricos e categóricos.


## Montagem da Base de Dados

Para obter qual bairro é o mais adequado, foi gerado uma base de dados, com 10.000 instâncias de bairros diferentes e suas características. Foi desenvolvido um algoritmo em python para criação da base de dados, composta por 18 atributos que medem a qualidade do bairro, na Tabela 1 abaixo segue a lista dos atributos:


<h2 align="center">Autores<h3/>

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/jefersoncmn"><img style="border-radius: 50%;" src="./public/jefersonphoto.jpeg" width="100px;" alt=""/><br/><sub><b>Jeferson Carlos Martin</b></sub></a><br /><a href="https://github.com/jefersoncmn" title="Jeferson Carlos Martin"></a>
    <td align="center"><a href="https://github.com/rafaelomodei"><img style="border-radius: 50%;" src="./public/rafaelphoto.jfif" width="100px;" alt=""/><br/><sub><b>Rafael Geovani Omodei</b></sub></a><br /><a href="https://github.com/rafaelomodei" title="Jeferson Carlos Martin"></a>
    </td>
</table>


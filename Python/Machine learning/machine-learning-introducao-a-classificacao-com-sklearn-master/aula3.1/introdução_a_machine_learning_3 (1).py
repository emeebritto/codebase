#INSTALA seaborn

!pip install seaborn==0.9.0

#======================================
#IMPORT PANDAS AS PD

import pandas as pd

#======================================
#LER CSV DA URL USANDO PANDAS

uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
dados = pd.read_csv(uri)

#======================================
#VER A 5 PRIMEIRAS LINHAS DO CSV

dados.head()

#======================================
#RENOMEA AS COLUNAS DO CSV

a_renomear = {
    'expected_hours' : 'horas_esperadas',
    'price' : 'preco',
    'unfinished' : 'nao_finalizado'
}
dados = dados.rename(columns = a_renomear)

#======================================
#CRIA UMA NOVA COLUNA finalizado BASEADA NA nao_finalizado.
#(INVERTENDO OS VALORES)

troca = {
    0 : 1,
    1 : 0
}
dados['finalizado'] = dados.nao_finalizado.map(troca)

#======================================
#VER AS 5 PRIMEIRAS LINHAS

dados.head()

#======================================
#VER AS 5 ÚLTIMAS LINHAS

dados.tail()

#======================================
#IMPORTA seaborn RENOMEANDO PARA sns

import seaborn as sns

#======================================
#DESENHA UM GRAFICO BASEADO NOS DADOS
# x="horas_esperadas"
# y="preco"
# data=dados (O DATAFRAME)

sns.scatterplot(x="horas_esperadas", y="preco", data=dados)

#======================================
#DIFERENCIA AS CORES DO GRAFICO, USANDO hue BASEADO NA COLUNA finalizado

sns.scatterplot(x="horas_esperadas", y="preco", hue="finalizado", data=dados)

#======================================
#PLOT RELATIVO - DOIS GRAFICO, COM UM GRAFICO EXCLUSIVO DA COLUNA finalizado

sns.relplot(x="horas_esperadas", y="preco", hue="finalizado", col="finalizado", data=dados)

#======================================
#DIVIDE OS DADOS PARA AS VARIÁVEIS

x = dados[['horas_esperadas', 'preco']]
y = dados['finalizado']

#======================================
#IMPORTS

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#======================================
#SEED DEFAULT

SEED = 20

#======================================
#DISTRIBUI DADOS PARA AS VARIÁVEIS DE TREINO E TESTE

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y,
                                                         random_state = SEED, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#======================================
#INICIALIZA

modelo = LinearSVC()

#======================================
#TREINA

modelo.fit(treino_x, treino_y)

#======================================
#TESTA

previsoes = modelo.predict(teste_x)

#======================================
#VERIFICA A TAXA DE ACERTOS

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#======================================
#IMPORTA numpy as np

import numpy as np

#======================================
#GERA UMA LISTA (array) COM VÁRIOS UMS

previsoes_de_base = np.ones(540)

#======================================
#COMPARA A TAXA DE ACERTOS

acuracia = accuracy_score(teste_y, previsoes_de_base) * 100
print("A acurácia do algoritmo de baseline foi %.2f%%" % acuracia)

#======================================
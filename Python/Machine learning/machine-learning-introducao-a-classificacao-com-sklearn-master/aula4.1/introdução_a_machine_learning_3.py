!pip install seaborn==0.9.0

import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
dados = pd.read_csv(uri)
dados.head()

a_renomear = {
    'expected_hours' : 'horas_esperadas',
    'price' : 'preco',
    'unfinished' : 'nao_finalizado'
}
dados = dados.rename(columns = a_renomear)
dados.head()

troca = {
    0 : 1,
    1 : 0
}
dados['finalizado'] = dados.nao_finalizado.map(troca)
dados.head()

dados.tail()

import seaborn as sns

sns.scatterplot(x="horas_esperadas", y="preco", data=dados)

sns.scatterplot(x="horas_esperadas", y="preco", hue="finalizado", data=dados)

sns.relplot(x="horas_esperadas", y="preco", hue="finalizado", col="finalizado", data=dados)

x = dados[['horas_esperadas', 'preco']]
y = dados['finalizado']

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

SEED = 5
np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

modelo = LinearSVC() # OU LinearSVC(random_state=SEED) # FIXA A SEED DIRETAMENTE
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

import numpy as np
previsoes_de_base = np.ones(540)
acuracia = accuracy_score(teste_y, previsoes_de_base) * 100
print("A acurácia do algoritmo de baseline foi %.2f%%" % acuracia)

#======================================
#GERA GRAFICO BASEADO NOS testes

sns.scatterplot(x="horas_esperadas", y="preco", hue=teste_y, data=teste_x)

#======================================
#DISTRIBUI OS VALORES MAX E MIN PARA AS VERIÁVEIS

x_min = teste_x.horas_esperadas.min()
x_max = teste_x.horas_esperadas.max()
y_min = teste_x.preco.min()
y_max = teste_x.preco.max()
print(x_min, x_max,y_min,y_max)

#======================================
#MONTA UM RANGE DO VALOR MIN ATÉ O MAX, DIVIDINDO EM 100 ESPAÇOS
#E SOMANDO PROPOCIONALMENTE

pixels = 100
eixo_x = np.arange(x_min, x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min, y_max, (y_max - y_min) / pixels)

#======================================
#MESCLA O EIXO_X E O EIXO_Y, USANDO c_, FORMANDO UM GRID (meshgrid)

xx, yy = np.meshgrid(eixo_x, eixo_y)
pontos = np.c_[xx.ravel(), yy.ravel()] # c_ CONCATENA
pontos

#======================================
#TESTA O RESULTADO PARA TODOS OS PONTOS

Z = modelo.predict(pontos)

#======================================
#REDIMENCIONA Z BASEADO NO xx.shape

Z = Z.reshape(xx.shape)

#======================================
#IMPORTA pyplot AS plt

import matplotlib.pyplot as plt

#======================================
#ADICIONA CONTORNO AO GRAFICO # DECISION BOUNDARY
# alpha = opacidade

plt.contourf(xx, yy, Z, alpha=0.3)

#======================================
#EXIBI GRAFICO
# c = cor
# s = size (tamanho dos pontos)

plt.scatter(teste_x.horas_esperadas, teste_x.preco, c=teste_y, s=1)

#======================================
#==============OUTRA AULA==============

### Estimadores não lineares e support vector machine ###

#======================================
#IMPORTS

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC #ESTIMADOR NÃO LINEAR
from sklearn.metrics import accuracy_score

#======================================
#DEFINE UMA SEED DEFAULT NO NUMPY

SEED = 5
np.random.seed(SEED)

#======================================
#DISTRIBUI VARIAÁVEIS DE TREINO

raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#======================================
#INICIA ESCALADOR

scaler = StandardScaler()

#======================================
#TREINA ESCALADOR

scaler.fit(raw_treino_x)

#======================================
#RE-ESCALA O DIMENSÕES

treino_x = scaler.transform(raw_treino_x) #RETORNA UM ARRAY DE ARRAY
teste_x = scaler.transform(raw_teste_x) #RETORNA UM ARRAY DE ARRAY

#======================================
#INICIA O NOVO MODELO SVC (não linear)

modelo = SVC()

#======================================
#TREINA

modelo.fit(treino_x, treino_y)

#======================================
#TESTA

previsoes = modelo.predict(teste_x)

#======================================
#VERIFICA A TAXA DE ACERTO

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#======================================
#DISTRIBUI PONTOS MIN E MAX
# OBS: como o valor contido no teste_x é um array de array,
# para capiturar os valores min e max, segue uma nova maneira

data_x = teste_x[:,0]
data_y = teste_x[:,1]

x_min = data_x.min()
x_max = data_x.max()
y_min = data_y.min()
y_max = data_y.max()

#======================================
#GERA RANGE DE PONTOS NO GRAFICO, GERANDO EIXOS

pixels = 100
eixo_x = np.arange(x_min, x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min, y_max, (y_max - y_min) / pixels)

#======================================
#UNIFICA OS EIXOS, GERANDO PONTOS GRAFICOS

xx, yy = np.meshgrid(eixo_x, eixo_y)
pontos = np.c_[xx.ravel(), yy.ravel()]

#======================================
#TESTA

Z = modelo.predict(pontos)

#======================================
#REDIMENSIONA

Z = Z.reshape(xx.shape)

#======================================
#MONTA GRAFICO

import matplotlib.pyplot as plt

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(data_x, data_y, c=teste_y, s=1)

#======================================
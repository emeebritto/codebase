#======================================
#INSTALAÇÕES

!pip install graphviz==0.10
!apt-get install graphviz

#======================================
#IMPORTA PD

import pandas as pd

#======================================
#LER E EXIBI CSV DA URL

uri = "https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv"
dados = pd.read_csv(uri)

dados.head() #EXIBI

#======================================
#RENOMEA AS COLUNAS

a_renomear = {
    'mileage_per_year' : 'milhas_por_ano',
    'model_year' : 'ano_do_modelo',
    'price' : 'preco',
    'sold' : 'vendido'
}
dados = dados.rename(columns=a_renomear)

#======================================
#CRIA UMA NOVA COLUNA BASEADA NO vendido,
#E ADICIONA NO LUGAR DA MESMA

a_trocar = {
    'no' : 0,
    'yes' : 1
}
dados.vendido = dados.vendido.map(a_trocar)

#======================================
dados.head() #EXIBI
#======================================
#EXIBI IDADE COM BASE NO ATUAL ANO

from datetime import datetime

ano_atual = datetime.today().year
dados['idade_do_modelo'] = ano_atual - dados.ano_do_modelo

#======================================
dados.head() #EXIBI
#======================================
#CRIA COLUNA MILHAS POR ANO
# 1 MILHA = 1.60KM

dados['km_por_ano'] = dados.milhas_por_ano * 1.60934#KM
#======================================
#REMOVE COLUNAS
# axis=1 #EIXO VERTICAL DA TABELA (COLUNAS)
# O DEFAULT É HORIZONTAL (LINHAS)

dados = dados.drop(columns = ["Unnamed: 0", "milhas_por_ano","ano_do_modelo"], axis=1)

#======================================
#IMPORTS

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#======================================
#DISTRIBUI DADOS PARA VARIÁVEIS

x = dados[["preco", "idade_do_modelo","km_por_ano"]]
y = dados["vendido"]

#======================================
#DEFINE SEED DEFAULT

SEED = 5
np.random.seed(SEED)

#======================================
#CRIA VARIÁVEIS DE TREINO E TESTE

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#======================================
#CRIA, TREINA E TESTA COM LinearSVC

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#=====================================
#CRIA ESTIMADOR BOBO (BASELINE)

from sklearn.dummy import DummyClassifier

dummy_stratified = DummyClassifier()
dummy_stratified.fit(treino_x, treino_y)
acuracia = dummy_stratified.score(teste_x, teste_y) * 100

print("A acurácia do dummy stratified foi %.2f%%" % acuracia)

from sklearn.dummy import DummyClassifier

dummy_mostfrequent = DummyClassifier()
dummy_mostfrequent.fit(treino_x, treino_y)
acuracia = dummy_mostfrequent.score(teste_x, teste_y) * 100

print("A acurácia do dummy mostfrequent foi %.2f%%" % acuracia)

#====================================
#CRIA, TREINA E TESTA COM SVC
# necessario re-escalar

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

SEED = 5
np.random.seed(SEED)
raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

scaler = StandardScaler()
scaler.fit(raw_treino_x)
treino_x = scaler.transform(raw_treino_x)
teste_x = scaler.transform(raw_teste_x)

modelo = SVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#=====================================
#visualizando as decisões de um estimador
#=====================================
#IMPORTS

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#=====================================
#SEED DEFAULT

SEED = 5
np.random.seed(SEED)

#=====================================
#VARIÁVEIS DE TREINO E TESTE

raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#=====================================
#INICIALIZA DecisionTreeClassifier COM PROFUNDIDADE 3

modelo = DecisionTreeClassifier(max_depth=3)

#=====================================
#TREINA

modelo.fit(raw_treino_x, treino_y)

#=====================================
#TESTA

previsoes = modelo.predict(raw_teste_x)

#=====================================
#VERIFICA TAXA DE ACERTOS

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#=====================================
#VISUALIZANDO AS DECISÕES
#=====================================
#IMPORTS 

from sklearn.tree import export_graphviz
import graphviz

#=====================================
#ATRIBUI AS COLUNAS PARA UMA VARIÁVEL

features = x.columns

#=====================================
# out_file | PARA SALVAR EM UM ARQUIVO
# export_graphviz | DEVOLVE UM FORMATO DE UM GRAFICO (NÃO VISUALIZAVEL)
# feature_names | DEFINE O NOME DAS FEATURES
# filled | PREENCHIDO (COR)
# rounded | AREDONDADO
# class_names | PARA EXIBIR AS CLASSES (O DEFAULT NÃO MOSTRA)

dot_data = export_graphviz(modelo, out_file=None,
                           filled = True, rounded = True,
                           feature_names = features,
                          class_names = ["não", "sim"])
#=====================================
#GERA A VISUALIZAÇÃO GRAFICA BASEADA NO dot_data

grafico = graphviz.Source(dot_data)
grafico


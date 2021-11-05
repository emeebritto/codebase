### Lendo dados da internet e manipulando os mesmos ###

#======================================
#IMPORTA PANDAS. (RENOMEANDO PARA PD)

import pandas as pd

#======================================
#LER O CSV USANDO URL

uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dados = pd.read_csv(uri)

#======================================
#VISUALIZA UM RESUMO COM 5 LINHAS. (O HEAD)

dados.head()

#======================================
#RENOMEA COLUNAS DO CSV

mapa = {
    "home" : "principal",
    "how_it_works" : "como_funciona",
    "contact" : "contato",
    "bought" : "comprou"
}
dados = dados.rename(columns = mapa)

#======================================
#DISTRIBUI OS DADOS PARA VARIÁVEIS

x = dados[["principal","como_funciona","contato"]]
x.head()

y = dados["comprou"]
y.head()

#======================================
#DIVIDE OS DADOS PARA VARIÁVEIS DE TREINO E TESTE

dados.shape

treino_x = x[:75]
treino_y = y[:75]
teste_x = x[75:]
teste_y = y[75:]

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#======================================
#IMPORTA LinearSVC E accuracy_score

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

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
#CALCULA TAXA DE ACERTOS - CODE DO FRAMEWORK

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#======================================
#======================================
#======================================
#======================================

### Estratificando splits ###

"""# Usando a biblioteca para separar treino e teste"""

#======================================
#IMPORTA train_test_split

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#======================================
#DEFINE SEED DEFAULT

SEED = 20

#======================================
#DIVIDE VARIÁVEIS DE TREINO E TESTE - USANDO train_test_split

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state = SEED, test_size = 0.25)
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
#VERIFICA TAXA DE ACERTOS, USANDO accuracy_score

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

#======================================

treino_y.value_counts() #NUMERO DE APARIÇÕES DE CADA ELEMENTOS NO ARRAY

teste_y.value_counts() #NUMERO DE APARIÇÕES DE CADA ELEMENTOS NO ARRAY

#======================================
#RECODE DAS LINHA 88 - 100 | USANDO stratify PARA DEIXAR PROPOCIONAL

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

SEED = 20

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y,
                                                         random_state = SEED, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

#======================================
#CODE COM VALORES DAS CLASSES PROPOCIONAIS

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

treino_y.value_counts()

teste_y.value_counts()

#======================================


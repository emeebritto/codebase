#=================================
import pandas as pd
#=================================
#IMPORTA CSV

resultados_exames = pd.read_csv("Dataset-master/exames.csv")
resultados_exames.head() #VISUALIZA

#=================================
#IMPORTA train_test_split

from sklearn.model_selection import train_test_split
from numpy import random

#=================================
#GERA UM NUMERO RANDOMICO BASEADO NA SEED

SEED = 123143
random.seed(SEED)

#=================================

valores_exames = resultados_exames.drop(columns=['id', 'diagnostico'])
diagnostico = resultados_exames.diagnostico

#=================================
#CRIA VARIAVEIS DE TREINO E TESTE

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames, 
                                                        diagnostico)

#=================================

treino_.head()

#=================================
#IMPORTA RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier

#=================================
#INICIALIZA

classificador = RandomForestClassifier(n_estimators = 100)

#=================================
#TREINA

classificador.fit(treino_x, treino_y)

#=================================
#TESTA, JÁ OBTENDO O SCORE

print(classificador.score(teste_x,teste_y))

#=================================

###OBTEMOS UM ERRO: UM DAS COLUNAS (33) DO DATAFRAME
###ESTÁ COM VALORES NaN.

#=================================
#isnull | DEVOLVE TRUE PARA ONDE ESTIVER SEM VALORES

resultados_exames.isnull().sum()

#=================================

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from numpy import random

SEED = 123143
random.seed(SEED)

valores_exames = resultados_exames.drop(columns=['id', 'diagnostico'])
diagnostico = resultados_exames.diagnostico

#=================================
#REMOVE A COLUNA 33 (QUE NÃO POSSUE VALOR)

valores_exames_v1 = valores_exames.drop(columns="exame_33")

#=================================

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v1, 
                                                        diagnostico,
                                                        test_size = 0.3)


classificador = RandomForestClassifier(n_estimators = 100)
classificador.fit(treino_x, treino_y)
print("Resultado da classificação %.2f%%" %(classificador.score(teste_x,teste_y)*100))

#=================================

from sklearn.dummy import DummyClassifier

SEED = 123143
random.seed(SEED)

classificador_bobo = DummyClassifier(strategy= "most_frequent")
classificador_bobo.fit(treino_x, treino_y)
print("Resultado da classificação boba %.2f%%" %(classificador_bobo.score(teste_x, teste_y)*100))


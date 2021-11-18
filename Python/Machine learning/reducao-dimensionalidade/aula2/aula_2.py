import pandas as pd

resultados_exames = pd.read_csv("Dataset-master/exames.csv")
resultados_exames.head()

from sklearn.model_selection import train_test_split
from numpy import random

SEED = 123143
random.seed(SEED)

valores_exames = resultados_exames.drop(columns=['id', 'diagnostico'])
diagnostico = resultados_exames.diagnostico

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames, 
                                                        diagnostico)

treino_.head()

from sklearn.ensemble import RandomForestClassifier

classificador = RandomForestClassifier(n_estimators = 100)
classificador.fit(treino_x, treino_y)
print(classificador.score(teste_x,teste_y))

resultados_exames.isnull().sum()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from numpy import random

SEED = 123143
random.seed(SEED)

valores_exames = resultados_exames.drop(columns=['id', 'diagnostico'])
diagnostico = resultados_exames.diagnostico
valores_exames_v1 = valores_exames.drop(columns="exame_33")

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v1, 
                                                        diagnostico,
                                                        test_size = 0.3)



classificador = RandomForestClassifier(n_estimators = 100)
classificador.fit(treino_x, treino_y)
print("Resultado da classificação %.2f%%" %(classificador.score(teste_x,teste_y)*100))

from sklearn.dummy import DummyClassifier

SEED = 123143
random.seed(SEED)

classificador_bobo = DummyClassifier(strategy= "most_frequent")
classificador_bobo.fit(treino_x, treino_y)
print("Resultado da classificação boba %.2f%%" %(classificador_bobo.score(teste_x, teste_y)*100))

valores_exames_v1.head()



#=================================================
#=================================================
#=================================================
#=================================================

import seaborn as sns
import matplotlib.pyplot as plt

#JUNTA OS DADOS

dados_plot = pd.concat([diagnostico, valores_exames_v1],axis = 1)
dados_plot.head() #VISUALIZA

#===================================
#Desvincule um DataFrame do formato largo para o longo

dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                    var_name="exames",
                    value_name='valores')
dados_plot.head()

#===================================

plt.figure(figsize=(10, 10))

#===================================

sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
               data = dados_plot)

#===================================

plt.xticks(rotation = 90)

#===================================

#PERCEBEMOS QUE O GRÁFICO NÃO ESTÁ PADRONIZADO

#===================================

from sklearn.preprocessing import StandardScaler

#===================================
#INICIALIZA PADRONIZADOR

padronizador = StandardScaler()

#===================================
#DEFINE BASE

padronizador.fit(valores_exames_v1)

#===================================
#PADRONIZA

valores_exames_v2 = padronizador.transform(valores_exames_v1)

#===================================
#DEFINE DATAFRAME

valores_exames_v2 = pd.DataFrame(data = valores_exames_v2,
                                columns=valores_exames_v1.keys())

#===================================

dados_plot = pd.concat([diagnostico, valores_exames_v2.iloc[:,0:10]],axis = 1)
dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                    var_name="exames",
                    value_name='valores')
plt.figure(figsize=(10, 10))
sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
               data = dados_plot, split= True)
plt.xticks(rotation = 90)

#===================================

def grafico_violino(valores, inicio, fim):
    
    
    dados_plot = pd.concat([diagnostico, valores.iloc[:,inicio:fim]],axis = 1)
    dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                         var_name="exames",
                         value_name='valores')
    plt.figure(figsize=(10, 10))
    sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
                   data = dados_plot, split= True)
    plt.xticks(rotation = 90)

#===================================

grafico_violino(valores_exames_v2, 10, 21)

grafico_violino(valores_exames_v2, 21, 32)

valores_exames_v3 = valores_exames_v2.drop(columns=["exame_29", "exame_4"])

def classificar(valores):
    SEED = 1234
    random.seed(SEED)
    treino_x, teste_x, treino_y, teste_y = train_test_split(valores, 
                                                        diagnostico,
                                                        test_size = 0.3)

    classificador = RandomForestClassifier(n_estimators = 100)
    classificador.fit(treino_x, treino_y)
    print("Resultado da classificação %.2f%%" %(classificador.score(teste_x,teste_y)*100))

classificar(valores_exames_v3)


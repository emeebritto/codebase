#=====================================

from collections import Counter
import pandas as pd

#=====================================
#LER CSV

df = pd.read_csv('busca.csv')

#=====================================
#DIVIDE DADOS DO CSV

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

#=====================================
#TRANSFORMA STRINGS EM VALORES BINÁRIOS

Xdummies_df = pd.get_dummies(X_df)

#=====================================
#A COLUNA Y NÃO POSSUI STRING, NÃO SENDO NECESSARIO A FUNÇÃO

Ydummies_df = Y_df

#=====================================
#OBTEM ARRAY DOS VALORES

X = Xdummies_df.values
Y = Ydummies_df.values

#=====================================
#DEFINE QUANTIDADE DE DADOS PARA TREINO E TESTE

porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = int(porcentagem_de_teste * len(Y))
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste

#=====================================
#DEFINE DADOS DE TREINO

# 0 até 799
treino_dados = X[0:tamanho_de_treino]
treino_marcacoes = Y[0  :tamanho_de_treino]

#=====================================
#DEFINE DADOS DE TESTE

# 800 até 899
fim_de_teste = tamanho_de_treino + tamanho_de_teste
teste_dados = X[tamanho_de_treino:fim_de_teste]
teste_marcacoes = Y[tamanho_de_treino:fim_de_teste]

#=====================================
#DEFINE DADOS DE VALIDAÇÃO

# 900 até 999
validacao_dados = X[fim_de_teste:]
validacao_marcacoes = Y[fim_de_teste:]

#=====================================
#FUNÇÃO - TREINA E TESTA COM VALIDAÇÃO

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
	modelo.fit(treino_dados, treino_marcacoes)

	resultado = modelo.predict(teste_dados)
	acertos = (resultado == teste_marcacoes)
	total_de_acertos = sum(acertos)
	total_de_elementos = len(teste_dados)

	taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

	msg = "Taxa de acerto do algoritmo {0}: {1}".format(nome, taxa_de_acerto)

	print(msg)

	return taxa_de_acerto

#=====================================

from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

if resultadoMultinomial > resultadoAdaBoost:
    vencedor = modeloMultinomial
else:
    vencedor = modeloAdaBoost

resultado = vencedor.predict(validacao_dados)
acertos = (resultado == validacao_marcacoes)
total_de_acertos = sum(acertos)
total_de_elementos = len(validacao_marcacoes)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
print(msg)

#=====================================
# a eficácia do algoritmo que chuta tudo um único valor

acerto_base = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)

#=====================================

total_de_elementos = len(validacao_dados)
print("Total de teste: %d" % total_de_elementos)
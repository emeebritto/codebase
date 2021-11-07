# [é gordinho?, tem perninha curta?, faz auau?]

#========================================
#DEFINE OS DADOS

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

#========================================
#DEFINE LABEL (CLASSES)

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1, 1, 1, -1, -1, -1]

#========================================
#IMPORTS

from sklearn.naive_bayes import MultinomialNB

#========================================
#INICIALIZA O MultinomialNB

modelo = MultinomialNB()

#========================================
#TREINA, USANDO DADOS E LABEL

modelo.fit(dados, marcacoes)

#========================================
#PREPARA TESTES

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [1, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]

#========================================
#O RESULTADO VERDADEIRO

marcacoes_teste = [-1, 1, 1]

#========================================
#TESTA

resultado = modelo.predict(teste)

#========================================
#CALCULA ACERTOS

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

#========================================

print(resultado)
print(taxa_de_acerto)

# MONTA OS ELEMENTOS A SER ANALISADOS. (com suas respectivas features);

# features (1 sim, 0 não)
# pelo longo?
# perna curta?
# faz auau?
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

#======================================
#MONTA O TREINO.

# 1 => porco, 0 => cachorro
#TREINO_X = DADOS
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
#TREINO_Y = CLASSES (INSTRUÇÃO - DO QUE É)
treino_y = [1,1,1,0,0,0] # labels / etiqueta

#======================================
#IMPORTA sklearn

from sklearn.svm import LinearSVC

#======================================
#INICIALIZA

model = LinearSVC()

#======================================
#TREINA

model.fit(treino_x, treino_y)

#======================================
#TESTA

animal_misterioso = [1,1,1]
model.predict([animal_misterioso])

#=> array([0])

#======================================
#TESTE SEQUENCIAL

misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0, 1, 1] # RESULTADO VERDADEIRO;

previsoes = model.predict(teste_x)

#=> array([0, 1, 0])

#======================================
#CALCULA TAXA DE ACERTOS - CODE MANUAL

corretos = (previsoes == teste_y).sum() #SOMA O NUMERO DE VERDADEIROS
total = len(teste_x)
taxa_de_acerto = corretos/total 
print("Taxa de acerto %.2f" % (taxa_de_acerto * 100))

#=> Taxa de acerto 66.67

#======================================
#CALCULA TAXA DE ACERTOS - CODE DO FRAMEWORK

from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(teste_y, previsoes)
print("Taxa de acerto %.2f" % (taxa_de_acerto * 100))

#=> Taxa de acerto 66.67

#======================================
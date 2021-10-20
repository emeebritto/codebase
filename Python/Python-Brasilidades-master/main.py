from Cpf_Cnpj_factory import Documento, DocCpf, DocCnpj
from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from Acesso_cep import BuscaEndereco
import requests

#Rodando exemplo da factory Cpf/Cnpj
exemplo_cnpj = '35379838000112'
exemplo_cpf = '15316264754'

print('Passando um CPF como argumento na classe Factory: {}'.format(exemplo_cpf))
documento = Documento.cria_documento(exemplo_cpf)
print('Chamando o metodo formata do produto retornado da Factory:')
print(documento)

print('Passando um CNPJ como argumento na classe Factory: {}'.format(exemplo_cnpj))
documento1 = Documento.cria_documento(exemplo_cnpj)
print('Chamando o metodo formata do produto retornado da Factory:')
print(documento1)

print('')
print('')
print('')

#Rodando exemplo de validação e formatação de um telefone BR
telefone_sem_cod_pais = '7926481234'
telefone_com_cod_pais = '5579998855214'
fone_objeto = TelefonesBr(telefone_sem_cod_pais)
fone_objeto1 = TelefonesBr(telefone_com_cod_pais)

print('Validando e imprimindo exemplo de telefone sem o código do pais {}'.format(telefone_sem_cod_pais))
print(fone_objeto)
print('Validando e imprimindo exemplo de telefone com o código do pais {}'.format(telefone_com_cod_pais))
print(fone_objeto1)

print('')
print('')
print('')

#Criando a data do dia e imprimindo o dia e mes por extenso
data = DatasBr()
print('Criando a data do dia e imprimindo o dia e mes por extenso')
print('Dia: {}'.format(data.dia_cadastro_extenso()))
print('Mes: {}'.format(data.mes_cadastro_extenso()))
print('Somando 7 dias a data de cadastro: ')
print(data.tempo_cadastro())

print('')
print('')
print('')

#Rodando exemplo de buscador de Cep
cep = '49020700'
objeto_cep = BuscaEndereco(cep)
print('Buscando e imprimindo dados do CEP: {}'.format(cep))
r = requests.get('https://viacep.com.br/ws/49020700/json/')
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print('Bairro: {} \n'
      'Cidade: {} \n'
      'Estado: {}'.format(bairro,cidade,uf)
      )





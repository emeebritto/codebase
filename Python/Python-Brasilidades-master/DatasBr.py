from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.data_cadastro = datetime.today()

    def mes_cadastro_extenso(self):
        lista_meses = [
            'janeiro', 'fevereiro', 'março',
            'abril', 'maio', 'junho', 'julho',
            'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'
        ]
        mes_cadastro = self.data_cadastro.month - 1
        return lista_meses[mes_cadastro]

    def dia_cadastro_extenso(self):
        lista_dias_semana = [
            'segunda-feira', 'terça-feira', 'quarta-feira',
            'quinta-feira', 'sexta-feira', 'sábado', 'domingo'
        ]
        indice_dia = self.data_cadastro.weekday()
        return lista_dias_semana[indice_dia]

    def format_data(self):
        data_formatada = self.data_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def __str__(self):
        return self.format_data()

    def tempo_cadastro(self):
        tempo_cadastro = timedelta(days=7) + self.data_cadastro
        return tempo_cadastro

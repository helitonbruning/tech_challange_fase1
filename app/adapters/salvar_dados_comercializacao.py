import pandas as pd
from app.infraestructure.postgresql_db import Database


class SalvarDadosComercializacao:
    def __init__(self):
        self.links = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
        self.db = Database()

    def salvar_dados_comercializacao(self):

        try:
            # Ler o arquivo CSV
            range_colunas = [str(ano) for ano in range(1970, 2023)]
            nomes_colunas = ['controle', 'produto', ]
            df = pd.read_csv(self.links, sep=";", header=None, names=nomes_colunas + range_colunas)

            # Salvar o DataFrame no banco de dados
            self.db.save_dataframe_to_table(df, "comercializacao")
        except Exception as e:
            raise e

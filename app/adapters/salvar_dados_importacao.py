import pandas as pd
from app.infraestructure.postgresql_db import Database


class SalvarDadosImportacao:
    def __init__(self):
        self.links = [
            "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"
    ]
        self.db = Database()

    def salvar_dados_importacao(self):

        try:
            df = pd.DataFrame()
            for link in self.links:
                df_link = pd.read_csv(link, sep=";", header=0, usecols=lambda column: column != "Id")
                df = pd.concat([df, df_link], ignore_index=True)

            # Salvar o DataFrame no banco de dados
            self.db.save_dataframe_to_table(df, "importacao")
        except Exception as e:
            raise e

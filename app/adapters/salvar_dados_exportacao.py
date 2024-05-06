import pandas as pd
from app.infraestructure.postgresql_db import Database


class SalvarDadosExportacao:
    def __init__(self):
        self.links = [
            "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
            "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"
    ]
        self.db = Database()

    def salvar_dados_exportacao(self):

        try:
            df = pd.DataFrame()
            for link in self.links:
                df_link = pd.read_csv(link, sep=";", header=0, usecols=lambda column: column != "Id")
                df = pd.concat([df, df_link], ignore_index=True)

            # Salvar o DataFrame no banco de dados
            self.db.save_dataframe_to_table(df, "exportacao")
        except Exception as e:
            raise e

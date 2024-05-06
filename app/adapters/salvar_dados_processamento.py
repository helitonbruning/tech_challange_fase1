import pandas as pd
from app.infraestructure.postgresql_db import Database


class SalvarDadosProcessamento:
    def __init__(self):
        self.links = [
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
    ]
        self.db = Database()

    def salvar_dados_processamento(self):

        try:
            df = pd.DataFrame()

            for link in self.links:
                df_link = pd.read_csv(link, sep="\t", usecols=lambda column: column != "id")
                df = pd.concat([df, df_link], ignore_index=True)

            # Salvar o DataFrame no banco de dados
            self.db.save_dataframe_to_table(df, "processamento")
        except Exception as e:
            raise e

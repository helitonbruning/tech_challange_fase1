import pandas as pd
from app.infraestructure.postgresql_db import Database

class SalvarDadosProducao:
    def __init__(self):
        self.links = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
        self.db = Database()

    def salvar_dados_producao(self):
        try:
            # Ler o arquivo CSV
            df = pd.read_csv(self.links, sep=";", usecols=lambda column: column != "id")

            # Salvar o DataFrame no banco de dados
            self.db.save_dataframe_to_table(df, "producao")
            return {"message": "Dados salvos com sucesso!"}
        except Exception as e:
            raise e

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
import pandas as pd

# URL de conexão com o banco de dados
DATABASE_URL = "postgresql://heliton:12345678@34.66.192.159:5432/api-embrapa"

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    def close_session(self, session):
        session.close()

    def save_dataframe_to_table(self, df: pd.DataFrame, table_name: str):
        try:
            session = self.get_session()
            print(table_name)
            df.to_sql('projeto_empbrapa.'+table_name, con=self.engine, if_exists='append', index=False)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            self.close_session(session)

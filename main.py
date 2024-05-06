from fastapi import FastAPI
from fastapi import HTTPException

from app.adapters.salvar_dados_producao import SalvarDadosProducao
from app.adapters.salvar_dados_processamento import SalvarDadosProcessamento
from app.adapters.salvar_dados_comercializacao import SalvarDadosComercializacao
from app.adapters.salvar_dados_importacao import SalvarDadosImportacao
from app.adapters.salvar_dados_exportacao import SalvarDadosExportacao


# Iniciando a aplicação FastAPI
app = FastAPI()


@app.get("/salvar_dados_producao")
async def salvar_dados_producao():

    try:
        producao = SalvarDadosProducao()

        producao.salvar_dados_producao()
        return {"message": "Dados salvos com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salvar_dados_processamento")
async def salvar_dados_processamento():
    try:
        processamento = SalvarDadosProcessamento()

        processamento.salvar_dados_processamento()
        return {"message": "Dados salvos com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salvar_dados_comercialiacao")
async def salvar_dados_comercialiacao():
    try:
        comercializacao = SalvarDadosComercializacao()

        comercializacao.salvar_dados_comercializacao()
        return {"message": "Dados salvos com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salvar_dados_importacao")
async def salvar_dados_importacao():
    try:
        importacao = SalvarDadosImportacao()

        importacao.salvar_dados_importacao()
        return {"message": "Dados salvos com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salvar_dados_exportacao")
async def salvar_dados_exportacao():
    try:
        exportacao = SalvarDadosExportacao()

        exportacao.salvar_dados_exportacao()
        return {"message": "Dados salvos com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

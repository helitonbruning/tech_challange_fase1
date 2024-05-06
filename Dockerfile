# Use a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY  . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a aplicação será executada
EXPOSE 8000

# Comando para iniciar o servidor da aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


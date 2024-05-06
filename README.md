# API de Gestão de Dados Embrapa

Esta é uma API desenvolvida com o framework FastAPI para lidar com a gestão de dados relacionados à produção, processamento, comercialização, importação e exportação de produtos agrícolas.

## Descrição

A API oferece endpoints para interagir com diferentes aspectos da gestão de dados Embrapa:

- **Salvar Dados de Produção**: Endpoint para salvar dados relacionados à produção Embrapa.
- **Salvar Dados de Processamento**: Endpoint para salvar dados relacionados ao processamento de produtos Embrapa.
- **Salvar Dados de Comercialização**: Endpoint para salvar dados relacionados à comercialização de produtos Embrapa.
- **Salvar Dados de Importação**: Endpoint para salvar dados relacionados à importação de produtos Embrapa.
- **Salvar Dados de Exportação**: Endpoint para salvar dados relacionados à exportação de produtos Embrapa.

## Requisitos

- Python 3.7 ou superior
- Instalação das dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/api-gestao-dados-agricolas.git

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt

## Uso

1. Inicie o servidor FastAPI:

   ```bash
   uvicorn main:app --reload

2. Acesse a documentação interativa da API em http://localhost:8000/docs para visualizar os endpoints disponíveis e testá-los.

## Exemplos de Uso
1. Salvar Dados de Produção:
```bash
GET /salvar_dados_producao
```

2. Salvar Dados de Processamento:
```bash
GET /salvar_dados_processamento
```

3. Salvar Dados de Comercialização:
```bash
GET /salvar_dados_comercializacao
```

4. Salvar Dados de Importação:
```bash
GET /salvar_dados_importacao
```

5. Salvar Dados de Exportação:
```bash
GET /salvar_dados_exportacao
```

# Para fazer o deploy dessa API em AWS com Docker, você pode seguir os passos abaixo:

1. Dockerfile: Crie um arquivo Dockerfile na raiz do seu projeto para definir como sua aplicação será containerizada.

2. Construir a imagem Docker: No terminal, navegue até a pasta do seu projeto e execute o seguinte comando para construir a imagem Docker:

3. Testar a imagem localmente: Depois de construir a imagem, você pode testá-la localmente.

4. Configurar AWS: Faça login na sua conta AWS e vá para o Console do ECS (Elastic Container Service) para configurar seu cluster, repositório de contêineres, e outros recursos necessários.

5. Enviar a imagem Docker para o ECR (Elastic Container Registry): Depois de configurar o repositório de contêineres, você pode enviar sua imagem Docker para o ECR.

   5.1 Fazer login no ECR
   ```bash
   aws ecr get-login-password --region regiao_da_sua_conta | docker login --username AWS --password-stdin id_da_sua_conta.dkr.ecr.regiao_da_sua_conta.amazonaws.com
   ```
   5.2 Tag da imagem Docker
   ```bash
   docker tag nome_da_sua_imagem:tag id_da_sua_conta.dkr.ecr.regiao_da_sua_conta.amazonaws.com/nome_do_seu_repositorio:tag
   ```
   5.3 Enviar a imagem para o ECR
   ```bash
   docker push id_da_sua_conta.dkr.ecr.regiao_da_sua_conta.amazonaws.com/nome_do_seu_repositorio:tag
   ```
   
6. Configurar o ECS: No Console do ECS, crie um novo serviço ECS e defina o tipo de tarefa como "Fargate" (ou "EC2" se preferir gerenciar suas próprias instâncias EC2).

7. Configurar o serviço ECS: Durante a configuração do serviço ECS, selecione o repositório de contêineres que você criou anteriormente no ECR e especifique a imagem Docker que você enviou.

8. Configurar porta e balanceador de carga: Certifique-se de configurar corretamente as portas de entrada e saída do seu serviço ECS e, se necessário, configure um balanceador de carga para encaminhar o tráfego para o seu serviço.

9. Implantar o serviço ECS: Após configurar todas as opções necessárias, implante o serviço ECS. Isso criará e iniciará os contêineres em conformidade com as configurações que você especificou.

10. Testar a API: Após a implantação bem-sucedida, você pode testar sua API acessando o URL fornecido pelo balanceador de carga do ECS.

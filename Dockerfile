# Usando a imagem oficial do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos necessários para o contêiner
COPY . .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar os testes
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
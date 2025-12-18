# 1. Imagem base com Python
FROM python:3.11-slim

# 2. Diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia dependências primeiro (cache eficiente)
COPY requirements.txt .

# 4. Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o resto da aplicação
COPY . .

# 6. Expõe a porta da API
EXPOSE 8000

# 7. Comando para subir a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

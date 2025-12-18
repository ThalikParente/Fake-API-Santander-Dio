# Fake API - Santander (DIO)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🎯 Objetivo do Projeto

Este projeto foi criado para solucionar um desafio encontrado durante o bootcamp **Santander Dev Week 2023** da [Digital Innovation One (DIO)](https://www.dio.me/). A API original fornecida para o desafio, disponível no repositório [santander-dev-week-2023-api](https://github.com/digitalinnovationone/santander-dev-week-2023-api), encontra-se fora do ar, impossibilitando a conclusão das atividades propostas.

Com o auxílio de pesquisas e de assistentes de IA, desenvolvi esta "Fake API" utilizando **Python** e **FastAPI** para simular o comportamento da API original. O objetivo é que este repositório sirva como uma solução alternativa não apenas para mim, mas também para futuros desenvolvedores que enfrentarem o mesmo problema, permitindo que todos possam realizar e concluir o desafio com sucesso.

## 💻 Como Executar o Projeto

Existem duas maneiras de executar esta API em sua máquina local. A primeira, utilizando Docker, é a mais recomendada pela simplicidade. A segunda é através de um ambiente Python local.

### Passo 0: Clone o Repositório

Independentemente do método escolhido, o primeiro passo é clonar este repositório:
```bash
git clone https://github.com/SEU-USUARIO/fake-api-dio-santander.git
cd fake-api-dio-santander
```
> **Atenção:** Lembre-se de substituir `SEU-USUARIO` pelo seu nome de usuário do GitHub.

---

### ✅ Método 1: Com Docker (Recomendado)

Este método é ideal se você já tem o Docker instalado, pois ele cuida de todo o ambiente para você.

1.  **Pré-requisito:** Ter o Docker e o Docker Compose instalados em sua máquina.

2.  **Execute o comando:** Na raiz do projeto, execute o seguinte comando para construir a imagem e iniciar o contêiner:
    ```bash
    docker compose up
    ```

Pronto! O servidor da API já estará rodando.

---

### ✅ Método 2: Ambiente Python Local (Sem Docker)

Se você não possui o Docker, pode executar a API diretamente com Python.

1.  **Pré-requisito:** Ter o Python 3 instalado.

2.  **Crie um ambiente virtual (Opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:** Utilize o `pip` para instalar as bibliotecas necessárias que estão no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie a API:** Use o `uvicorn` para carregar o servidor. A flag `--reload` faz com que o servidor reinicie automaticamente a cada alteração no código.
    ```bash
    uvicorn app:app --reload
    ```

---

### 🚀 Acessando a API

Após iniciar o servidor por qualquer um dos métodos, a API estará disponível em sua máquina. Você pode acessar a documentação interativa (Swagger UI) através do seguinte link no seu navegador:

**http://127.0.0.1:8000/docs**

Lá, você poderá ver todos os *endpoints* disponíveis e testá-los diretamente.

## 📦 Endpoints da API

A API simula as operações básicas de um CRUD (Create, Read, Update, Delete) para usuários:

*   `GET /users`: Retorna uma lista de todos os usuários.
*   `GET /users/{user_id}`: Retorna os detalhes de um usuário específico.
*   `POST /users`: Cria um novo usuário.
*   `PUT /users/{user_id}`: Atualiza os dados de um usuário existente.
*   `DELETE /users/{user_id}`: Remove um usuário.

## 📄 Dados

Os dados dos usuários são armazenados no arquivo `data.json`. Você pode modificar este arquivo para adicionar, editar ou remover usuários conforme sua necessidade para os testes.

---

Feito com ❤️ por um dev para outros devs!
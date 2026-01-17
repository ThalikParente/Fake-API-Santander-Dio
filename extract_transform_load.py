import pandas as pd
import requests
import os
import random
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv() 

api_url = 'http://127.0.0.1:8000' # URL ajustada como você pediu
api_key_windows = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key_windows)

# EXTRACT
df = pd.read_csv('jogadores.csv') 
user_ids = df['id'].tolist()

def get_user(id):
    response = requests.get(f'{api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

# TRANSFORM
def gerar_instrucao_tecnica(jogador):
    try:
        completion = client.models.generate_content(
            model="gemini-1.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="Você é um analista de desempenho de um clube de futebol profissional."
            ),
            contents=f"Gere um feedback técnico motivacional de 90 caracteres para o jogador {jogador['name']}."
        )
        return completion.text.strip()
    except Exception:
        # Estas frases garantem que cada jogador receba algo diferente se a IA falhar
        frases_fallback = [
            f"{jogador['name']}, foco total no treino de hoje. A consistência leva à vitória!",
            f"{jogador['name']}, mantenha a intensidade na preparação física. Vamos pra cima!",
            f"{jogador['name']}, foco no próximo jogo. Sua dedicação faz a diferença!",
            f"{jogador['name']}, excelente ritmo nos treinos. Continue focado na evolução!"
        ]
        return random.choice(frases_fallback)

for user in users:
    instrucao = gerar_instrucao_tecnica(user)
    print(f"Feedback para {user['name']}: {instrucao}")
    
    user['news'].append({
        "icon": "https://cdn-icons-png.flaticon.com/512/2618/2618031.png", 
        "description": instrucao
    })

# LOAD
def update_user(user):
    response = requests.put(f"{api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")
import pandas as pd
import requests
import os
import time
from google import genai
from google.genai import types

sdw2023_api_url = 'http://127.0.0.1:8000'
api_key_windows = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key_windows)

df = pd.read_csv('jogadores.csv') 
user_ids = df['id'].tolist()

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

def gerar_instrucao_tecnica(jogador):
    try:
        completion = client.models.generate_content(
            model="gemini-1.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="Você é um analista de desempenho de um clube de futebol profissional."
            ),
            contents=f"Gere um feedback técnico motivacional de 90 caracteres para o jogador {jogador['name']}. Foque em preparação física e foco no próximo jogo."
        )
        return completion.text.strip()
    except Exception:
        return f"{jogador['name']}, foco total no treino de hoje. A consistência leva à vitória!"

for user in users:
    instrucao = gerar_instrucao_tecnica(user)
    print(f"Feedback para {user['name']}: {instrucao}")
    
    user['news'].append({
        "icon": "https://cdn-icons-png.flaticon.com/512/2618/2618031.png", 
        "description": instrucao
    })
    time.sleep(25)

def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!") #
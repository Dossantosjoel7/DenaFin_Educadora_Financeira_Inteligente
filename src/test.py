import sys
sys.path.append("/usr/lib/python3/dist-packages")
sys.path.append("/home/dossantosjoel7/.local/lib/python3.12/site-packages")


import requests

# A mesma configuração do teu app.py
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "hf.co/unsloth/gemma-4-12b-it-GGUF:UD-Q4_K_XL"

payload = {
    "model": MODELO,
    "prompt": "Responde apenas com a palavra 'Conectado'.",
    "stream": False
}

print("A enviar pedido para o Ollama...")

try:
    resposta = requests.post(OLLAMA_URL, json=payload)
    resposta.raise_for_status() # Dispara um alerta se o erro for 404 ou 500
    
    texto_ia = resposta.json().get('response', '')
    print(f"\n✅ Sucesso absoluto! O Ollama respondeu: {texto_ia}")
    
except requests.exceptions.ConnectionError:
    print("\n❌ ERRO: O Python não encontrou o Ollama. Confirma se executaste 'ollama serve' no terminal.")
except Exception as e:
    print(f"\n❌ ERRO DESCONHECIDO: {e}")
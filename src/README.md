
# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar o Ollama ([https://ollama.com](https://ollama.com))
# 2. Descarregar o modelo local quantizado (Gemma 12B)
ollama pull hf.co/unsloth/gemma-4-12b-it-GGUF:UD-Q4_K_XL

# 3. Testar se o modelo funciona diretamente no terminal
ollama run hf.co/unsloth/gemma-4-12b-it-GGUF:UD-Q4_K_XL "Olá, quem és tu?"
````

## Código Completo

Todo o código-fonte principal, a lógica de injeção de contexto (RAG) e a configuração da interface encontram-se no ficheiro `src/app.py`.

## Como Executar a Aplicação

```
# 1. Instalar as dependências do Python
pip install streamlit pandas requests

# 2. Garantir que o serviço do Ollama está a correr
# (Se não estiver a rodar em background, abre um terminal dedicado para este comando)
ollama serve

# 3. Arrancar a aplicação Streamlit (certifica-te que estás na raiz do projeto)
streamlit run src/app.py
```

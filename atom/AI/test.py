from llama_cpp import Llama

llm = Llama(model_path="/usr/bin/ollama")
response = llm("What can you do?")
print(response)

import requests  # Importa a biblioteca requests, que serve para fazer requisições HTTP

# Variável chamada url e guarda nela um texto (endereço da API)
url = "https://rickandmortyapi.com/api/character"

# Faz uma requisição GET (método para buscar dados) para a URL
# Volta uma resposta HTTP, que fica guardada na variável resposta
resposta = requests.get(url)

# Converte o conteúdo da resposta para um formato que o Python entende (JSON é um formato de dados muito usado em APIs)
# Variável que guarda todo o conteúdo da API
dados = resposta.json()

# dados["results"] → lista de personagens
# [0] → primeiro personagem
# ["name"] → nome do personagem

# * Importar biblioteca
# * Guardar valor em variável
# * Chamar função/método
# * Entender dicionário, lista, misturar lista + dicionário

# Desafio 1: imprimir o nome e o status
print("Nome:", dados["results"][2]["name"])
print("Status:", dados["results"][2]["status"])

# Desafio 2: pegar os 5 primeiros personagens da lista
for i in dados["results"][:5]:
    print(i["name"])

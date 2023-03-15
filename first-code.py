# A Calabouço Discos é uma loja de vinis que resiste ao digital com albuns clássicos de lendas do rock. Os albuns são catalogados por: id, ano, artista, genero, titulo, preço. Os clientes são armazenados com: id, nome e idade. E as vendas da loja são armazenadas da seguinte maneira: id, id_cliente, ids_albuns (que é uma lista de IDs com os albuns que a pessoa comprou), total_da_venda.

# Utilizando dicionários, crie um código para registrar as vendas e ao final apresentar o fechamento do dia, apresentando as vendas uma a uma.

# Plus1: Quantas vendas foram realizadas?
# Plus2: Qual foi o faturamento total da loja?
# Plus3: Qual cliente mais gastou?
# Plus4: Qual foi a maior compra?
# Plus5: Qual é o album mais vendido?
# Plus6: Quais sao os generos mais comprados pelas faixas de idade abaixo:
  # - 18 a 25 anos
  # - 25 a 35 anos
  # - 35 a 55 anos
  # - acima de 55 anos

# Primeiros dicionários (antes do json):
# dict_albuns = {
#   "111" : {"ano"      : "1983",
#           "artista"   : "Billy_Idol",
#           "genero"    : "post_punk",
#           "titulo"    : "rebel_yell", 
#           "preco"     : 230.50,
#           "quantidade": 25
#      },
#   "222" : {"ano"      : "1990",
#           "artista"   : "Iggy_Pop",
#           "genero"    : "pop_rock",
#           "titulo"    : "candy", 
#           "preco"     : 155.90,
#           "quantidade": 35
#          },
#   "333" : {"ano"      : "1997",
#           "artista"   : "Prodigy",
#           "genero"    : "eletronico",
#           "titulo"    : "the_fat_of_the_land", 
#           "preco"     : 161.90,
#           "quantidade": 20
#          },
#   "444" : {"ano"      : "1984",
#           "artista"   : "Madonna",
#           "genero"    : "pop_rock",
#           "titulo"    : "like_a_virgin", 
#           "preco"     :  215.85,
#           "quantidade": 15
#          },
# }
# dict_clientes = {
#   "0101" : {"nome"  : "Joao",
#             "idade" : 19   
#       },
#   "0202" : {"nome"  : "Pedro",
#             "idade" : 22 
#       },
#   "0303" : {"nome"  : "Maria",
#             "idade" : 36    
#       },
#   "0404" : {"nome"  : "Pamela",
#             "idade" : 55
#       },
#   "0505" : {"nome"  : "Julia",
#             "idade" : 42
#        },
#   "0606" : {"nome"  : "Camila",
#             "idade" :  18   
#       },
#   "0707" : {"nome"  : "Roberto",
#             "idade" : 29
#       },
#   "0808" : {"nome"  : "Renato",
#             "idade" : 34
#        },
#   "0909" : {"nome"  : "Eduardo",
#             "idade" : 44   
#       },
#   "1010" : {"nome"  : "Carla",
#             "idade" : 60
#        }
# }
# dict_vendas = {
#   1 : {"id_loja"         : "sul",
#        "id_cliente"      : "0101",
#        "id_album"        : ["111","222"]
#        },
#   2 : {"id_loja"         : "norte",
#        "id_cliente"      : "0202",
#        "id_album"        : ["333"]
#        },
#   3 : {"id_loja"         : "leste",
#        "id_cliente"      : "0303",
#        "id_album"        : ["444","111","333","222"]
#        },
#   4 : {"id_loja"         : "centro",
#        "id_cliente"      : "0404",
#        "id_album"        : ["444","333","222"]
#        },
#   5 : {"id_loja"         : "oeste",
#        "id_cliente"      : "0505",
#        "id_album"        : ["333","222"]
#        },
#   6 : {"id_loja"         : "norte",
#        "id_cliente"      : "0606",
#        "id_album"        : ["444","111"]
#        },
#   7 : {"id_loja"         : "centro",
#        "id_cliente"      : "0707",
#        "id_album"        : ["444","222"]
#        },
#   8 : {"id_loja"         : "sul",
#        "id_cliente"      : "0808",
#        "id_album"        : ["444","333"]
#        },
#   9 : {"id_loja"         : "leste",
#        "id_cliente"      : "0909",
#        "id_album"        : ["111","333"]
#        },
#   10 : {"id_loja"         : "oeste",
#        "id_cliente"       : "1010",
#        "id_album"         : ["444","111","333"]
#        },
#   11 : {"id_loja"         : "norte",
#        "id_cliente"       : "0909",
#        "id_album"         : ["444"]
#        },
# }

import json
import datetime

#Função para gravar novos dados nos arquivos Json:
def grava_arquivo(filename, dict_json):
  with open(filename, "w") as arquivo:
    json.dump(dict_json, arquivo, indent = 4)

#Função para carregar os dados que já estão salvos:
def carrega_json(filename):
  try:
    with open(filename) as arquivo:
      dict_json = json.load(arquivo)
  except:
    dict_json = {}
  return dict_json

def cadastra_album():
  dict_albuns  = carrega_json("albuns.json")
  id_album     = input('Digite o ID do album (Ex.: "111"): ')
  while id_album in dict_albuns:
    print(f"ID {id_album} já cadastrado. Digite outro")
    id_album   = input('Digite o ID do album (Ex.: "111"): ')
  ano          = input("Digite o ano: ")
  artista      = input("Digite o artista: ")
  genero       = input("Digite o genero: ")
  titulo       = input("Digite o título: ")
  preco        = float(input("Digite o preço: "))
  quantidade   = int(input("Digite a quantidade: "))
  dict_albuns[id_album] = {"ano"       : ano,
                          "artista"    : artista,
                          "genero"     : genero,
                          "titulo"     : titulo,
                          "preco"      : preco,
                          "quantidade" : quantidade
                          }
  grava_arquivo("albuns.json", dict_albuns)
#cadastra_album()
  
def cadastra_cliente():
  dict_clientes  = carrega_json("clientes.json")
  id_cliente     = input('Digite o ID do cliente (Ex.: "0101"): ')
  while id_cliente in dict_clientes:
    print(f"ID {id_cliente} já cadastrado. Digite outro")
    id_cliente   = input('Digite o ID do cliente (Ex.: "0101"): ')
  nome           = input("Digite o nome: ")
  idade          = int(input("Digite a idade: "))
  dict_clientes[id_cliente] = {"nome":nome, 
                               "idade":idade}
  grava_arquivo("clientes.json", dict_clientes)
#cadastra_cliente()

def entrada_estoque(id_album):
  dict_albuns  = carrega_json("albuns.json")
  entrada = int(input("Quantas unidades: "))
  dict_albuns[id_album]["quantidade"] += entrada
  grava_arquivo("albuns.json",dict_albuns)
#entrada_estoque("101")

def cadastra_venda():
  dict_vendas  = carrega_json("vendas.json")    
  dict_albuns  = carrega_json("albuns.json")
  dict_clientes  = carrega_json("clientes.json")
  id_venda     = (len(dict_vendas))+1
  data_venda = datetime.date.today().strftime("%d/%m/%Y")
  id_loja      = input("Digite o ID da loja: ")
  filiais      = ['norte', 'leste', 'centro', 'oeste', 'sul']
  while id_loja not in filiais:
    print(f"\tLoja {id_loja} não existe. Favor digitar um ID válido")
    id_loja    = input("Digite o ID da loja: ")
  id_cliente   = input('Digite o ID do cliente (Ex.: "0101"): ')
  if id_cliente not in dict_clientes:
      print("\tCliente não cadastrado.")
      cadastro = input("Deseja cadastrar agora? S ou N: ")
      if cadastro.lower() == "s":
        cadastra_cliente()
      else:
        while id_cliente not in dict_clientes:
          print("\tRealize o cadastro e depois registre a compra")
          id_cliente   = input('Digite o ID do cliente (Ex.: "0101"): ')
  albuns       = int(input("Digite quantos albuns foram comprados: "))
  id_album     = []
  for albun in range(albuns):
    id         = input('Digite o ID do album (Ex.: 111): ')
    while id not in dict_albuns:
      print("\tAlbum não encontrato. Digite um ID de album válido: ")
      id         = input('Digite o ID do album (Ex.: 111): ')
    id_album.append(id)
    while dict_albuns[id]["quantidade"] <= 0:
      print("Album fora de estoque. Atualize o estoque")
      id = input('Digite o ID do album (Ex.: 111): ')
    dict_albuns[id]["quantidade"] -= 1 #Debitando as vendas das quantidades
    grava_arquivo("albuns.json",dict_albuns)
  dict_vendas[id_venda] = {"id_loja":id_loja,
                           "data": data_venda,
                           "id_cliente":id_cliente, 
                           "id_album":id_album}
  #Adicionando a chave "total_da_venda" automaticamente:
  for vendas in dict_vendas: 
    venda = 0
    for album in dict_vendas[vendas]["id_album"]:
      preco = dict_albuns[album]["preco"]
      venda += preco
    dict_vendas[vendas]["total_da_venda"] = venda

  grava_arquivo("vendas.json", dict_vendas)
#cadastra_venda()

#Adicionando a chave "total_da_venda" automaticamente antes do json:
# for vendas in dict_vendas: 
#   venda = 0
#   for album in dict_vendas[vendas]["id_album"]:
#     preco = dict_albuns[album]["preco"]
#     venda += preco
#   dict_vendas[vendas]["total_da_venda"] = venda

#################################################################

#Transformando o dicionário em string
# dict_albuns_string_json = json.dumps(dict_albuns) #DUMPS
# dict_clientes_string_json = json.dumps(dict_clientes)
# dict_vendas_string_json = json.dumps(dict_vendas)

#Salvando os dicionáros em um arquivo json
# with open("albuns.json", "w") as arquivo:
#   json.dump(dict_albuns, arquivo, indent=4) #DUMP
# with open("clientes.json","w") as arquivo:
#   json.dump(dict_clientes, arquivo, indent=4)
# with open("vendas.json","w") as arquivo:
#   json.dump(dict_vendas, arquivo, indent=4)

#DUMPS = pegando uma coleção e transformando em string
#DUMP = Pegando uma coleção e salvando em arquivo json

#Arquivo: dump, load
#String: dumps, loads (dump string e load string)
#################################################################
  
# Utilizando dicionários, crie um código para apresentar o fechamento do dia, apresentando as vendas uma a uma.

def relatorio_vendas():
  print("*** Fechamento ***")
  dict_vendas  = carrega_json("vendas.json")    
  dict_clientes  = carrega_json("clientes.json")
  dict_albuns  = carrega_json("albuns.json")
  for vendas in dict_vendas: 
    loja = dict_vendas[vendas]["id_loja"]
    data = dict_vendas[vendas]["data"]
    id_cliente = dict_vendas[vendas]["id_cliente"]
    nome = dict_clientes[id_cliente]["nome"]
    valor_compra = dict_vendas[vendas]["total_da_venda"]
    print(f"""
    Cliente: {nome}
    Loja: {loja.capitalize()}
    Data: {data}
    Valor da Compra: R$ {round(valor_compra,2)}""")
    for albuns in dict_vendas[vendas]["id_album"]:
      nome_album = dict_albuns[albuns]["titulo"].replace("_"," ")
      print(f"\tAlbum: {nome_album.title()}")

relatorio_vendas()

# Relatório de um dia específico:
def relatorio_por_dia(day):
  print(f"\n*** Fechamento dia: {day} ***")
  dict_vendas  = carrega_json("vendas.json")    
  dict_clientes  = carrega_json("clientes.json")
  dict_albuns  = carrega_json("albuns.json")
  for vendas in dict_vendas:
    data = dict_vendas[vendas]["data"]
    if day == data:
      loja = dict_vendas[vendas]["id_loja"]
      id_cliente = dict_vendas[vendas]["id_cliente"]
      nome = dict_clientes[id_cliente]["nome"]
      valor_compra = dict_vendas[vendas]["total_da_venda"]
      print(f"""
        Cliente: {nome}
        Loja: {loja.capitalize()}
        Data: {data}
        Valor da Compra: R$ {round(valor_compra,2)}""")
      for albuns in dict_vendas[vendas]["id_album"]:
        nome_album = dict_albuns[albuns]["titulo"].replace("_"," ")
        print(f"\t\tAlbum: {nome_album.title()}")

relatorio_por_dia("25/02/2023")

dict_vendas  = carrega_json("vendas.json")    
dict_clientes  = carrega_json("clientes.json")
dict_albuns  = carrega_json("albuns.json")

def search(dict_json, chave, valor):
  list_resultado = []
  for i in dict_json:
    if dict_json[i].get(chave) == valor:
      list_resultado.append({i:dict_json[i]})
  return list_resultado

def get_by_title(x):
  return search(dict_albuns, 'titulo', x)

def get_by_year(x):
  return search(dict_albuns, 'ano', x)
  
def get_by_id(x):
  return dict_albuns.get(x)

def get_by_artist(x):
  return search(dict_albuns, 'artista', x)

def get_by_gender(x):
  return search(dict_albuns, 'genero', x)
#print(get_by_gender("pop_rock"))
  
# Plus1: Quantas vendas foram realizadas?
print(f"\nTotal de vendas realizadas: {len(dict_vendas)}\n")

# Plus1.2: Quantos albuns existem na loja?
print(f"Total de albuns vendidos pela loja: {len(dict_albuns)}\n")

# Plus2: Qual foi o faturamento total da loja?
def faturamento_total():
  dict_vendas  = carrega_json("vendas.json") 
  total = 0
  for venda in dict_vendas:
    vendas = dict_vendas[venda]["total_da_venda"]
    total += vendas
  print(f"O total de faturamento de todas as lojas foi de: R$ {round(total,2)}\n")
faturamento_total()

# Plus2.2: Qual foi o faturamento total de cada filial
def faturamento_lojas():
  dict_vendas  = carrega_json("vendas.json")    
  lista_filiais = [] #Criando uma lista com todas as filiais
  for venda in dict_vendas:
    lista_filiais.append(dict_vendas[venda]["id_loja"])
  lista_filiais = set(lista_filiais) #Transformando em SET para não repetir as filiais
  for loja in lista_filiais:
    total_loja = 0
    for venda in dict_vendas:
      id_loja = dict_vendas[venda]["id_loja"]
      if id_loja == loja:
        faturamentos = dict_vendas[venda]["total_da_venda"]
        total_loja += faturamentos
    print(f"\tTotal de Faturamento Loja {loja.capitalize()}: R$ {round(total_loja,2)}")
faturamento_lojas()

#Plus 2.3: Para filtrar o faturamento de uma filial específica 
def faturamento_loja(filial):
  dict_vendas  = carrega_json("vendas.json")    
  lista_filiais = [] #Criando uma lista com todas as filiais
  for venda in dict_vendas:
    lista_filiais.append(dict_vendas[venda]["id_loja"])
  lista_filiais = set(lista_filiais) #Transformando em SET para não repetir as filiais
  for loja in lista_filiais:
    if loja == filial:
      total_loja = 0
      for venda in dict_vendas:
        id_loja = dict_vendas[venda]["id_loja"]
        if id_loja == loja:
          faturamento = dict_vendas[venda]["total_da_venda"]
          total_loja += faturamento
      print(f"\nTotal de Faturamento Loja {loja.capitalize()}: R$ {round(total_loja,2)}")
faturamento_loja("oeste")

#Quanto foi vendido por cada dia:
def venda_total_por_dia():
  dict_vendas  = carrega_json("vendas.json")    
  import numpy as np 
  print("\n*** Faturamento total por dia ***") 
  lista_datas = [] 
  for venda in dict_vendas:
    lista_datas.append(dict_vendas[venda]["data"])
  lista_datas = np.unique(np.array(lista_datas))
  for dia in lista_datas:
    total_dia = 0
    for venda in dict_vendas:
      data = dict_vendas[venda]["data"]
      if dia == data:
        faturamento = dict_vendas[venda]["total_da_venda"]
        total_dia += faturamento
    print(f"Total de Faturamento no dia {dia}: R$ {round(total_dia,2)}")
venda_total_por_dia()

#Quanto foi vendido em um dia específico:
def venda_por_dia(day):
  dict_vendas  = carrega_json("vendas.json")    
  import numpy as np 
  print("\n*** Faturamento por dia ***") 
  lista_datas = [] 
  for venda in dict_vendas:
    lista_datas.append(dict_vendas[venda]["data"])
  lista_datas = np.unique(np.array(lista_datas))
  for dia in lista_datas:
    if dia == day:
      total_dia = 0
      for venda in dict_vendas:
        data = dict_vendas[venda]["data"]
        if dia == data:
          faturamento = dict_vendas[venda]["total_da_venda"]
          total_dia += faturamento
      print(f"Total de Faturamento no dia {dia}: R$ {round(total_dia,2)}")
venda_por_dia("26/02/2023")
  
# Plus3: Qual cliente mais gastou?
def maior_cliente():
  dict_vendas  = carrega_json("vendas.json")    
  dict_clientes  = carrega_json("clientes.json")
  maior = 0
  for cliente in dict_vendas: 
    faturamento_cliente = dict_vendas[cliente]["total_da_venda"]
    if faturamento_cliente > maior:
      maior = faturamento_cliente
      id = dict_vendas[cliente]["id_cliente"]
      id_venda = cliente
      nome = dict_clientes[id]["nome"]
  print(f"\nO cliente que mais gastou foi: {nome} | ID da Venda: {id_venda} | Valor: R$ {round(maior,2)}\n")
maior_cliente()

# Plus4: Qual foi a maior compra?
def maior_venda():
  dict_vendas  = carrega_json("vendas.json")    
  dict_albuns  = carrega_json("albuns.json")
  maior_compra = 0
  for compra in dict_vendas:
    valor_compra = dict_vendas[compra]["total_da_venda"]
    if valor_compra > maior_compra:
      id_compra = compra
      maior_compra = valor_compra
      discos = dict_vendas[compra]["id_album"]
  print(f"A maior compra foi a {id_compra}ª no valor de R$ {round(maior_compra,2)} com os albuns: ")
  for albuns in discos:
    artista = dict_albuns[albuns]["artista"].replace("_"," ")
    nome_album = dict_albuns[albuns]["titulo"].replace("_"," ")
    print(f"\tAlbum: {nome_album.title()} | Artista: {artista}")
maior_venda()
    
# Plus5: Qual é o album mais vendido?
def album_mais_vendido():
  dict_vendas  = carrega_json("vendas.json")    
  dict_albuns  = carrega_json("albuns.json")
  print("\n*** Albuns mais Vendido ***")
  albuns = []
  for album in dict_albuns:
    titulo = dict_albuns[album]["titulo"].replace("_"," ")
    albuns.append(titulo)
    
  for titulo in albuns:
    total_titulo = 0
    for compra in dict_vendas:
      discos_vendidos = dict_vendas[compra]["id_album"]
      for album in discos_vendidos:
        nome_album = dict_albuns[album]["titulo"].replace("_"," ")
        if nome_album == titulo:
          total_titulo += 1
    print(f"{titulo.title()}: {total_titulo}")
album_mais_vendido()
    
# Plus6: Quais sao os generos mais comprados pelas faixas de idade abaixo:
  # - 18 a 25 anos
  # - 25 a 35 anos
  # - 35 a 55 anos
  # - acima de 55 anos
print("\n*** Generos Mais Comprados Pelas Faixas de Idade ***")
primeira_faixa = []
segunda_faixa = []
terceira_faixa = []
quarta_faixa = []
for sales in dict_vendas:
  id_cliente = dict_vendas[sales]["id_cliente"]
  idade = dict_clientes[id_cliente]["idade"]
  albuns = dict_vendas[sales]["id_album"]
  for album in albuns:
    genero = dict_albuns[album]["genero"].replace("_"," ")
    if idade > 17 and idade <= 24:
      primeira_faixa.append(genero)
    elif idade >= 25 and idade <= 34:
      segunda_faixa.append(genero)
    elif idade >= 35 and idade <= 55:
      terceira_faixa.append(genero)
    elif idade > 55:
      quarta_faixa.append(genero)

#Para confirmar quantas vezes cada genero aparece:
# print(f"Primeira Faixa (18 a 25 anos): {primeira_faixa}\n") 
# print(f"Segunda Faixa (25 a 35 anos): {segunda_faixa}\n")
# print(f"Terceira Faixa (35 a 55 anos): {terceira_faixa}\n")
# print(f"Quarta Faixa (acima de 55 anos): {quarta_faixa}\n")

#Criando uma lista com todos os generos:
generos = []
for albuns in dict_albuns:
  genero = dict_albuns[albuns]["genero"].replace("_"," ")
  generos.append(genero)
generos = set(generos) #Set para não repetir os generos
#Criando um dicionário com as faixas etarias usando as listas criadas acima:
faixa_etaria = {
          "Primeira Faixa (18 a 25 anos)": primeira_faixa, 
          "Segunda Faixa (25 a 35 anos)": segunda_faixa,
          "Terceira Faixa (35 a 55 anos)": terceira_faixa,
          "Quarta Faixa (acima de 55 anos)": quarta_faixa
}
#Cruzando as duas informações (generos e faixa etaria):
for faixa, values in faixa_etaria.items():
  print(f"\n{faixa}:")
  for gender in generos:
    print(f"{gender.title()} : {values.count(gender)}")

#Quantas unidades de cada album disponível em estoque:
def estoque_atual():
  dict_albuns  = carrega_json("albuns.json")
  print("\n*** Estoque atualizado ***") 
  for album in dict_albuns:
    estoque = dict_albuns[album]["quantidade"]
    titulo = dict_albuns[album]["titulo"].replace("_", " ")
    artista = dict_albuns[album]["artista"].replace("_", " ")
    print(f"{album} - {titulo.title()} ({artista.title()}): {estoque}")
estoque_atual()

def menu():
  escolha = input("\n1 - Cadastrar Album | 2 - Cadastrar Cliente | 3 - Cadastrar Venda: ")
  if escolha == "1":
    cadastra_album()
  elif escolha == "2":
    cadastra_cliente()
  elif escolha == "3":
    cadastra_venda()
  else:
    print("Opção Inválida")

#menu()
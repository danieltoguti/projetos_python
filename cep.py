
import requests as Req 

cep = input('Escreva o cep: ')

url = f'http://viacep.com.br/ws/{cep}/json'

endereco = Req.get(url).json()

logradouro = endereco['logradouro']
cidade = endereco['localidade']
estado = endereco['uf']
print(f'{logradouro}, {cidade} - {estado}')
'''

d = {"gato" : 5, "cachorro": 6, "galinha": 12}
print(d["gato"])

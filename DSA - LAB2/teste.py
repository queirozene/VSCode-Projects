from urllib.request import urlopen
import json

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')

dados = json.loads(response)
dados = json.loads(response)[0]

titulo = dados['title']
url = dados['url']
duracao = dados['duration']
visualizacoes = dados['stats_number_of_plays']
data_upload = dados['upload_date']
id = dados['id']

print ('Título: ', dados['title'])
print ('URL: ', dados['url'])
print ('Duração: ', dados['duration'])
print ('Número de Visualizações: ', dados['stats_number_of_plays'])
#E ai pessoal antes de rodar esse codigo vc precisa ter o Python instalado
#depois você instala o module request e bs4 
#o modulo do Json já vem instaado quando se instala o Python
#já vou logo adiantando que não funcionou, não conseguir fazer, perdão por qualquer coisa
#mas vlw pela oportunidade, não sabia fazer nada do que vocês me passaram, mas acho que aprendi alguma coisa
import requests #importação do modulo request
#Não conseguir usar ReGex, porém usei o bs4 no lugar para localizar o paragrafo
from bs4 import BeautifulSoup #importação do modulo bs4 
#importação do modulo Json
import json

# Nessa parte eu criei um variavel, usando o metodo, get do requests, para obter da url do G1 o conteudo 
# que estavamos querendo pegar no caso o titulo e subtitulo da pagina

r = requests.get('https://g1.globo.com/')
#depois de pegar o com a requisção o conteudo da pagina e uso o bs4 para colocar esse conteudo 
#de uma forma que eu entenda, então e pego o conteudo da pagína e apresento com a linguagem html
#por que se eu tentar printar assim eu vou ter o conteudo em uma lingaugem que eu não consiga decifrar 
#e colocando em html eu consigo achar também o titulo e sub titulo que preciso,uso uma variavel para armazenar esse conteudo
portal = BeautifulSoup(r.content, 'html.parser')

#Agora eu faço um procura no html usando o find do bs4 procurando um tag especifica que possua uma 
#class especifica que defini, pra isso tive que ir no portal G1 e ver o codigo Html, uso uma variavel para armazenar esse valor 
titulo = portal.find('a', attrs={'class':'feed-post-link'})
#faço o  mesmo com o subtitulo
stitulo = portal.find('div', attrs={'class':'feed-post-body-resumo'})
#depois de ter feito isso tem o retorno o codigo html com o titulo e subtitulo uso uma variavel para armazenar esse valor 
#ai eu transformo eles em text, usando duas variaveis para pegar o conteudo das 2
tf = titulo.text
sf = stitulo.text
#ai nessa parte eu travei, por que não conseguir converte esse texto do titulo e subtitulo em Json
#tentei usar um dicinario, mas não conseguir fazer o print
note = { tf, sf}
print(json.load(note))

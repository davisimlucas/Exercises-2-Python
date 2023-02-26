'''
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
The article is long, so it is split up between 4 pages. 
Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.
(Hint: The post here describes in detail how to use the 
BeautifulSoup and requests libraries through the solution of the exercise posted here.)
This will just print the full text of the article to the screen. 
It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
'''
import requests 
from bs4 import BeautifulSoup

# declarar a url do artigo
url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

# gerar lista vazia onde entrará o texto do artigo
text = []

# looping for para que o programa passe por todas as páginas do artigo
for i in range(1, 5):
    # if para "raspar" os conteúdos da primeira página do artigo 
    if i == 1:
        page_url = url
    # caso page_url não seja 1, atualizar para as outras páginas com o "?page" (especifica qual página)
    else:
        page_url = url + '?page' + str(i)

    # biblioteca requests para solicitar o conteúdo HTML da página da web correspondente à URL do artigo.
    response = requests.get(page_url)
    # Crie um objeto BeautifulSoup com o conteúdo da página da web solicitada e especifique o analisador HTML a ser usado
    soup = BeautifulSoup(response.content, 'html.parser')
    # localizar a tag HTML que contém o corpo do artigo com o find(). passe o nome da tag (div) e o valor do atributo de classe
    # extrair o texto da tag HTML que contém o corpo do artigo com o .get_text()  
    page_text = soup.find(class_ = 'BodyWrapper-csjEHZ bKuzuQ body body__container article__body').get_text()

    # adicionar à lista cada tesxto extraido de cada página
    text.append(page_text)

# usar a função join() para unir os elementos de texto da list text 
print(" ".join(map(str, text)))


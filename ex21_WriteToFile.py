'''
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, use the code from the solution), 
and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.
Extras:
Ask the user to specify the name of the output file that will be saved.
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
article_text = " ".join(map(str, text))

with open('article.txt', 'w') as f:
    f.write(article_text)
    





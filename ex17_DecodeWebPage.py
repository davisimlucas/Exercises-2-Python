'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

requisicao = requests.get(url)

#<h3 class="indicate-hover css-vf1hbp">Resisting Iran’s Hijab Law, Women Are Letting Their Hair Flow Uncovered</h3>
soup = BeautifulSoup(requisicao.content, 'html.parser')

titles = soup.find_all("h2", {"class": "css-1cmu9py e1voiwgp0"})

for title in titles: 
    print(title.text)


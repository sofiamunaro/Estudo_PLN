#stemming:reduzir a palavra ao seu radical (correram --> corr)
#lematização: reduzir a palavra a sua forma base (correram --> correr)
#lematizador leva em consideração a categoria gramatical das palavras para determinar o lema
#lematizador é mais preciso e eficiente

import requests
from bs4 import BeautifulSoup as bs
import spacy

url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
response = requests.get(url)
soup = bs(response.text, "html.parser")
paragraphs = soup.find_all("p")
page_text = "\n".join([p.get_text() for p in paragraphs])

nlp = spacy.load("pt_core_news_sm")
documento = nlp(page_text)

#se o token for um verbo, retorna ele lematizado
tokens = [token.lemma_ for token in documento if token.pos_ == "VERB" and not(token.is_stop)]
print(tokens)

#.pos dá a classe gramatical
for token in documento:
    if token.is_alpha:
        print(token.text + ':' + token.pos_)


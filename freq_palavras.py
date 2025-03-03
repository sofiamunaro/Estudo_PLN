import requests
from bs4 import BeautifulSoup as bs
import spacy
import nltk #biblioeteca de pln
import matplotlib.pyplot as plt

url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
response = requests.get(url)
soup = bs(response.text, "html.parser")
paragraphs = soup.find_all("p")
page_text = "\n".join([p.get_text() for p in paragraphs])

nlp = spacy.load("pt_core_news_sm")
#possibilidade de adicionar stopwords
#nlp.Defaults.stop_words.add('dados')

documento = nlp(page_text)

tokens = []
for token in documento:
    if token.pos_ == "VERB" and token.is_alpha and not(token.is_stop):
        tokens.append(str.lower(token.lemma_))
    elif not(token.pos_ == "VERB") and token.is_alpha and not(token.is_stop):
        tokens.append(str.lower(token.text))

frequencia = nltk.FreqDist(tokens) #cria um dicionario com o token e sua frequencia
for chave,valor in frequencia.items():
    print(chave + ':' + str(valor))

frequencia.plot(30,cumulative=False) #mostra as 30 palavras mais frequentes
plt.show()
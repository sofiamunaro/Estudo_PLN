import requests
from bs4 import BeautifulSoup as bs
import spacy
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
response = requests.get(url)
soup = bs(response.text, "html.parser")
paragraphs = soup.find_all("p")
page_text = "\n".join([p.get_text() for p in paragraphs])

nlp = spacy.load("pt_core_news_sm")
documento = nlp(page_text)

tokens = []
for token in documento:
    if token.pos_ == "VERB" and token.is_alpha and not(token.is_stop):
        tokens.append(str.lower(token.lemma_))
    elif not(token.pos_ == "VERB") and token.is_alpha and not(token.is_stop):
        tokens.append(str.lower(token.text))

frequencia = nltk.FreqDist(tokens)

#criação da nuvem
nuvem = WordCloud(background_color='white')
nuvem = nuvem.generate(" ".join(tokens))
plt.imshow(nuvem)
plt.show()
